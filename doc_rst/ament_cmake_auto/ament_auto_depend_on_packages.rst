
##############################################
ament_cmake_auto.ament_auto_depend_on_packages
##############################################

.. module:: ament_cmake_auto.ament_auto_depend_on_packages


.. function:: ament_auto_depend_on_packages(target **kwargs)

   Make a target depend on everything provided by another CMake package.
   
   This function is intended to be used internally by ament_cmake_auto.
   
   :param target: the name of the target
   :type target: string
   :param SYSTEM: Optional. If given, and if a package provides old
     style standard CMake variables instead of modern CMake targets, then
     the include directories from this dependency will be treated as system
     includes.
     This property has no effect if the package being depended upon provides
     modern CMake targets.
   :type SYSTEM: None
   :param SCOPE: Optional. If given it must be one of PUBLIC, PRIVATE, or INTERFACE.
     See target_link_libraries() documentation for more info about SCOPE. If unset
     then it defaults to unset for CMake functions that support that, and PUBLIC for
     functions that don't.
   :type SCOPE: string
   :param PACKAGES: a list of package names
   :type PACKAGES: list of strings
   
   @private
   

