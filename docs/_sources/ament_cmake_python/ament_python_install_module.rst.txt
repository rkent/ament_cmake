
##############################################
ament_cmake_python.ament_python_install_module
##############################################

.. module:: ament_cmake_python.ament_python_install_module


.. function:: ament_python_install_module()


   .. note:: This is a macro, and so does not introduce a new scope.

   Install a Python module.
   
   :param module_file: the Python module file
   :type MODULE_FILE: string
   :param DESTINATION_SUFFIX: the base package to install the module to
     (default: empty, install as a top level module)
   :type DESTINATION_SUFFIX: string
   :param SKIP_COMPILE: if set do not compile the installed module
   :type SKIP_COMPILE: option
   


.. function:: _ament_cmake_python_install_module(module_file **kwargs)

   

