"""
Test building python packages with colcon
"""

import filecmp
import os
from pathlib import Path
import shutil
import sys
import subprocess

from jinja2 import Template
import pytest

from options import DEFAULT_OPTIONS, get_options

PWD = Path(os.environ.get('PWD'))
SOURCE_DIR = Path(__file__).parent.parent
PYTHON_INSTALL_DIR = Path(os.environ.get('PYTHON_INSTALL_DIR'))
PYEGG_VERSION = os.environ.get('PYEGG_VERSION')
AMENT_PREFIX_PATH = os.environ.get('AMENT_PREFIX_PATH', '')
CMAKE_PREFIX_PATH = os.environ.get('CMAKE_PREFIX_PATH', '')
CMAKE_COMMAND = os.environ.get('CMAKE_COMMAND', 'cmake')

AMENT_PYTHON_TEST_PACKAGE = "ament_python_test_package"
AMENT_PYTHON_TEST_PACKAGE_OVERLAY = AMENT_PYTHON_TEST_PACKAGE + "_overlay"


@pytest.fixture(scope='module')
def module_dir(tmp_path_factory):
    return tmp_path_factory.getbasetemp()


def do_build_package(package_dir, module_dir, options):
  build_dir = module_dir / 'build' / options['name']
  build_dir.mkdir(parents=True, exist_ok=True)

  configure_command = [CMAKE_COMMAND, '-S', package_dir, '-B', build_dir, '--install-prefix', str(module_dir / 'install' / options['name'])]
  if options['symlink_install']:
    configure_command.append('-DAMENT_CMAKE_SYMLINK_INSTALL=1')
  print(f"Configuring package {options['name']} with command: {configure_command}")
  result = subprocess.run(configure_command, text=True)
  assert result.returncode == 0, f"cmake configure failed for package {options['name']}"

  build_command = ['cmake', '--build', str(build_dir)]
  print(f"Building package {options['name']} with command: {build_command}")
  result = subprocess.run(build_command, text=True)
  assert result.returncode == 0, f"cmake build failed for package {options['name']}"

  install_command = ['cmake', '--install', str(build_dir)]
  print(f"Installing package {options['name']} with command: {install_command}")
  result = subprocess.run(install_command, text=True)
  assert result.returncode == 0, f"cmake install failed for package {options['name']}"


def do_test_package(module_dir, package_name, options):
  install_base = module_dir / 'install'
  if options['destination']:
    install_path = install_base / package_name / options['destination'] / package_name
  else:
    install_path = install_base / package_name / PYTHON_INSTALL_DIR / package_name
  print(f"install_path for package {package_name}: {install_path}")
  assert install_path.exists(), f"install path does not exist for {package_name}: {install_path}"
  assert (install_path / '__init__.py').exists(), f"missing __init__.py in {install_path}"

  if options['has_python'] or options['has_python_before']:
    assert Path.read_text (install_path / '__init__.py').startswith(f"# This is {package_name}"), \
          f"__init__.py should be from {package_name} python package"

  if options['has_msg']:
    assert(install_path/ 'msg').is_dir(), f"There should be a msg directory in {install_path}"

  if options['symlink_install']:
      print(f"Testing symlink install in package {package_name}")
      assert (install_path / '__init__.py').is_symlink(), "__init__.py should be a symlink"

  if options['version']:
      print(f"Testing version: {options['version']} IN EGG-INFO in package {package_name}")
      version = options['version']
      egg_info_dir = install_base / package_name / PYTHON_INSTALL_DIR / f'{package_name}-{version}-{PYEGG_VERSION}.egg-info'
      assert egg_info_dir.exists(), f"egg-info dir does not exist for {package_name}: {egg_info_dir}"
      egg_info_file = egg_info_dir / 'PKG-INFO'
      assert Path.read_text(egg_info_file).find(f"Version: {version}") != -1, \
        f"egg-info file should contain 'Version: {version}'"

  if options['setup_cfg']:
      print(f"Testing setup.cfg metadata in package {package_name}")
      print(f"  options: {options}")
      version = options['version'] or "0.0.0"
      egg_info_dir = install_base / package_name / PYTHON_INSTALL_DIR / f'{package_name}-{version}-{PYEGG_VERSION}.egg-info'
      assert egg_info_dir.exists(), f"egg-info dir does not exist for {package_name}: {egg_info_dir}"
      egg_info_file = egg_info_dir / 'PKG-INFO'
      assert Path.read_text(egg_info_file).find(f"Keywords: test_of_ament_cmake_python") != -1, \
        f"egg-info file should contain 'Keywords: test_of_ament_cmake_python' specified in setup.cfg"

  if options['scripts_destination']:
      print(f"Testing script installed in package {package_name}")
      script_path = install_base / package_name / options['scripts_destination'] / 'do_something'
      assert script_path.exists(), f"script do_something does not exist for {package_name}: {script_path}"


def test_from_options(module_dir):
  #print("Environment: ")
  #for name, value in os.environ.items():
  #    print(f"{name}={value}")
  # assert False
  
  # delete any existing package directory
  packages_dir = SOURCE_DIR / 'test' / 'packages' / 'generated'

  # Create test packages from template
  for options in get_options():
    package_dir = packages_dir / options['name']
    print(f'Generating package {options["name"]} from {package_dir}')
    do_build_package(package_dir, module_dir, options)


def not_test_ament_python_test_package(module_dir) -> None:
    do_build_package(module_dir, AMENT_PYTHON_TEST_PACKAGE, source_prefix=SOURCE_DIR / 'test')
    print(f"Checking installed package files for {AMENT_PYTHON_TEST_PACKAGE}")
    print(f"SOURCE_DIR / 'test' / AMENT_PYTHON_TEST_PACKAGE: {SOURCE_DIR / 'test' / AMENT_PYTHON_TEST_PACKAGE}")
    print(f"module_dir / 'install' / AMENT_PYTHON_TEST_PACKAGE: {module_dir / 'install' / AMENT_PYTHON_TEST_PACKAGE}")
    test_dircmp =filecmp.dircmp(
        SOURCE_DIR / 'test' / AMENT_PYTHON_TEST_PACKAGE / AMENT_PYTHON_TEST_PACKAGE,
        module_dir / 'install' / AMENT_PYTHON_TEST_PACKAGE / PYTHON_INSTALL_DIR / AMENT_PYTHON_TEST_PACKAGE
    )
    assert not test_dircmp.left_only, \
        f"Files only in source package: {test_dircmp.left_only}"
    assert not test_dircmp.right_only, \
        f"Files only in installed package: {test_dircmp.right_only}"
    assert not test_dircmp.diff_files, \
        f"Two python packages should match after install: {test_dircmp.diff_files}"


def not_test_ament_python_test_package_with_overlay(module_dir) -> None:
    compare_dir = module_dir / 'compare'
    do_build_package(module_dir, AMENT_PYTHON_TEST_PACKAGE_OVERLAY, source_prefix=SOURCE_DIR / 'test')

    INSTALL_DIR = module_dir / 'install' / AMENT_PYTHON_TEST_PACKAGE_OVERLAY / PYTHON_INSTALL_DIR
    shutil.copytree(SOURCE_DIR / 'test' / AMENT_PYTHON_TEST_PACKAGE / AMENT_PYTHON_TEST_PACKAGE, compare_dir, dirs_exist_ok=True)
    shutil.copytree(SOURCE_DIR / 'test' / AMENT_PYTHON_TEST_PACKAGE_OVERLAY / AMENT_PYTHON_TEST_PACKAGE_OVERLAY, compare_dir, dirs_exist_ok=True)
    test_dircmp =  filecmp.dircmp(compare_dir, INSTALL_DIR / AMENT_PYTHON_TEST_PACKAGE_OVERLAY)
    assert not test_dircmp.left_only, \
        "Files only in source package overlay"
    assert not test_dircmp.right_only, \
        "Files only in installed package overlay"
    assert not test_dircmp.diff_files, \
        "Two overlaid python packages should match after install"


def not_test_python_double_version(module_dir) -> None:
  package_name = 'python_package_double_version'
  do_build_package(module_dir, package_name, source_prefix=SOURCE_DIR / 'test')

  # This package installs two versions of the same package with different names and version numbers.
  install_base = module_dir / 'install' / package_name / PYTHON_INSTALL_DIR
  for additional_name in [package_name, 'some_other_name']: 
    install_path = install_base / additional_name
    print(f"install_path for package {additional_name}: {install_path}")
    assert install_path.exists(), f"install path should exist for {package_name}: {install_path}"
    assert (install_path / '__init__.py').exists(), f"missing __init__.py in {install_path}"
    print(f"Testing version IN EGG-INFO in package {package_name}")
    version = "1.2.34" if additional_name == package_name else "5.6.78"
    egg_info_dir = module_dir / 'install' / package_name / PYTHON_INSTALL_DIR / f'{additional_name}-{version}-{PYEGG_VERSION}.egg-info'
    assert egg_info_dir.exists(), f"egg-info dir should exist for {package_name}: {egg_info_dir}"
    egg_info_file = egg_info_dir / 'PKG-INFO'
    assert Path.read_text(egg_info_file).find(f"Version: {version}") != -1, \
      f"egg-info file should contain 'Version: {version}'"


