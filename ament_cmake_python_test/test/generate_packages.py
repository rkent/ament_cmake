"""
Generate python packages for testing. This is not run automatically, but should be
run manually when the test packages need to be regenerated.
"""

import filecmp
import os
from pathlib import Path
import shutil
import sys
import subprocess

from jinja2 import Template

from options import get_options, DEFAULT_OPTIONS


def create_package(options, package_dir):
  print(f"Generating package {options['name']}")
  # print(f"  options: {options}")
  template_dir = Path(__file__).parent / 'pkg_template'
  python_subdir = options['python_subdir'] or options['name']

  package_dir.mkdir(parents=True)

  install_options = ''
  if options['has_msg']:
    shutil.copytree(template_dir / 'msg', package_dir / 'msg')

  if options['has_python'] or options['has_python_before']:
    ignore_patterns = shutil.ignore_patterns('*.jinja')
    shutil.copytree(template_dir / 'package_directory', package_dir / python_subdir, ignore=ignore_patterns)
    template = Template(Path.read_text(template_dir / 'package_directory' / '__init__.py.jinja'))
    Path.write_text(package_dir / python_subdir / '__init__.py', template.render(options))

  if options['version']:
    install_options += f' VERSION {options["version"]}'

  if options['setup_cfg']:
    (package_dir / options['setup_cfg']).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(template_dir / options['setup_cfg'], package_dir / (Path(options['setup_cfg']).parent))
    install_options += f' SETUP_CFG {options["setup_cfg"]}'

  if options['scripts_destination']:
    scripts_dir = template_dir / 'python_scripts'
    shutil.copytree(scripts_dir, package_dir / python_subdir, dirs_exist_ok=True)
    template = Template(Path.read_text(template_dir / 'setup.cfg.jinja'))
    Path.write_text(package_dir / 'setup.cfg', template.render(options))
    install_options += f' SCRIPTS_DESTINATION {options["scripts_destination"]}'

  if options['destination']:
    install_options += f' DESTINATION {options["destination"]}'

  # The python package has a name that differs from the name in package.xml
  if options['python_subdir']:
    install_options += f' PACKAGE_DIR {options["python_subdir"]}'

  # The package has a subdirectory with a subpackage
  if options['subpackage']:
    sub_package_dir = package_dir / options['subpackage']
    sub_options = DEFAULT_OPTIONS | { 'name': options['subpackage'], 'description': f'Subpackage of {options["name"]}' }
    create_package(sub_options, sub_package_dir)

  options['install_options'] = install_options
  template = Template(Path.read_text(template_dir / 'package.xml.jinja'))
  Path.write_text(package_dir / 'package.xml', template.render(options))
  template = Template(Path.read_text(template_dir / 'CMakeLists.txt.jinja'))
  Path.write_text(package_dir / 'CMakeLists.txt', template.render(options))


def main():
  packages_dir = Path(__file__).parent / 'packages' / 'generated'
  shutil.rmtree(packages_dir, ignore_errors=True)

  for test_options in get_options():
    package_dir = packages_dir / test_options['name']
    create_package(test_options, package_dir)


if __name__ == '__main__':
  main()
