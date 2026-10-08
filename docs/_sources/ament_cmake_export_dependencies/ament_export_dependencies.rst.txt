
#########################################################
ament_cmake_export_dependencies.ament_export_dependencies
#########################################################

.. module:: ament_cmake_export_dependencies.ament_export_dependencies


.. function:: ament_export_dependencies()


   .. note:: This is a macro, and so does not introduce a new scope.

   Export dependencies to downstream packages.
   
   Each package name must be find_package()-able with the exact same case.
   Additionally the exported variables must have a prefix with the same case
   and the suffixes must be INCLUDE_DIRS and LIBRARIES.
   
   :param ARGN: a list of package names
   :type ARGN: list of strings
   
   @public
   

