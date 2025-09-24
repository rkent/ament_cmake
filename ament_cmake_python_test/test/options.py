"""
Options used to generate test packages from a template.
"""

DEFAULT_OPTIONS = {
  'name': 'SET_ME',
  'version': None,
  'description': 'SET_ME',
  'setup_cfg': None,
  'destination': None,
  'symlink_install': False,
  'python_subdir': None,
  'has_python': True,
  'has_python_before': False, # This will only make sense when both python and msg are in the same package
  'has_msg': False,
  'scripts_destination': None,
  'subpackage': None,  # name of a subpackage to create inside the main package
}

TESTS_OPTIONS = [
  {
    'name': 'python_package',
    'description': 'Package with python code',
  },
  {
    'name': 'msg_package',
    'description': 'Package with only msg files',
    'has_msg': True,
    'has_python': False,
  },
  {
    'name': 'python_package_symlink',
    'description': 'Package with python code, installed with symlink in build',
    'symlink_install': True,
  },
  {
    'name': 'python_package_rename',
    'description': 'Package with python code, installed from alternate directory name',
    'python_subdir': 'renamed_dir',
  },
  {
    'name': 'python_package_version',
    'description': 'Package with python code, specifying version in ament_python_install_package',
    'version': '6.7.89',
  },
  {
    'name': 'python_package_setup',
    'description': 'Package with python code, using setup.cfg for metadata',
    'setup_cfg': 'config/setup.cfg',
  },
  {
    'name': 'python_package_destination',
    'description': 'Package with python code, installed to alternate destination',
    'destination': 'new_destination',
  },
  {
    'name': 'python_package_with_scripts',
    'description': 'Package with python code',
    'scripts_destination': 'lib/python_package_with_scripts',
  },
  #{
  #  'name': 'msg_package_with_subpackage',
  #  'description': 'Package with only msg files and a subpackage',
  #  'has_msg': True,
  #  'has_python': False,
  #  'subpackage': 'under_msg_package'
  #},
  #{
  #  'name': 'python_package_with_subpackage',
  #  'description': 'Package with a subpackage',
  #  'subpackage': 'under_package'
  #},
]


def get_options():
  """
  # extend the options to include combinations of msg and python
  """
  tests_options = []
  for options in TESTS_OPTIONS:
    options = DEFAULT_OPTIONS | options
    tests_options.append(options)

    if options['name'].startswith('python_package'):
      msg_options = options.copy()
      msg_options['name'] += '_with_msg'
      msg_options['description'] += 'and msg files'
      msg_options['has_msg'] = True
      tests_options.append(msg_options)
    elif options['name'].startswith('msg_package'):
      py_options = options.copy()
      py_options['name'] += '_with_python_before'
      py_options['description'] += ' and python code before msg'
      py_options['has_python_before'] = True
      tests_options.append(py_options)
  return tests_options
