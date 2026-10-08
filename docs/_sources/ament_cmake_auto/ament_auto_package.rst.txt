
###################################
ament_cmake_auto.ament_auto_package
###################################

.. module:: ament_cmake_auto.ament_auto_package


.. function:: ament_auto_package(**kwargs)


   .. note:: This is a macro, and so does not introduce a new scope.

   Export information, install files and targets, execute the
   extension point ``ament_auto_package`` and invoke
   ``ament_package()``.
   
   :param INSTALL_TO_PATH: if set, install executables to `bin` so that
     they are available on the `PATH`.
     By default they are being installed into `lib/${PROJECT_NAME}`.
     It is currently not possible to install some executable into `bin`
     and some into `lib/${PROJECT_NAME}`.
     Libraries are not affected by this option.
     They are always installed into `lib` and `dll`s into `bin`.
   :type INSTALL_TO_PATH: option
   :param INSTALL_TO_SHARE: a list of directories to be installed to the
     package's share directory
   :type INSTALL_TO_SHARE: list of strings
   :param ARGN: any other arguments are passed through to ament_package()
   :type ARGN: list of strings
   
   Export all found build dependencies which are also run
   dependencies.
   If the package has an include directory install all recursively
   found header files (ending in h, hh, hpp, hxx) and export the
   include directory.
   Export and install all library targets and install all executable
   targets.
   
   @public
   

