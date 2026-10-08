
###############################################
ament_cmake_python.ament_python_install_package
###############################################

.. module:: ament_cmake_python.ament_python_install_package


.. function:: ament_python_install_package()


   .. note:: This is a macro, and so does not introduce a new scope.

   Install a Python package (and its recursive subpackages)
   
   :param package_name: the Python package name
   :type package_name: string
   :param PACKAGE_DIR: the path to the Python package directory (default:
     <package_name> folder relative to the CMAKE_CURRENT_LIST_DIR)
   :type PACKAGE_DIR: string
   :param VERSION: the Python package version (default: package.xml version)
   :param VERSION: string
   :param SETUP_CFG: the path to a setup.cfg file (default:
     setup.cfg file at CMAKE_CURRENT_LIST_DIR root, if any)
   :param SETUP_CFG: string
   :param DESTINATION: the path to the Python package installation
     directory (default: PYTHON_INSTALL_DIR)
   :type DESTINATION: string
   :param SCRIPTS_DESTINATION: the path to the Python package scripts'
     installation directory, scripts (if any) will be ignored if not set
   :type SCRIPTS_DESTINATION: string
   :param SKIP_COMPILE: if set do not byte-compile the installed package
   :type SKIP_COMPILE: option
   


.. function:: _ament_cmake_python_install_package(package_name **kwargs)

   

