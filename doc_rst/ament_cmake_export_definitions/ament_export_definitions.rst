
#######################################################
ament_cmake_export_definitions.ament_export_definitions
#######################################################

.. module:: ament_cmake_export_definitions.ament_export_definitions


.. function:: ament_export_definitions()


   .. note:: This is a macro, and so does not introduce a new scope.

   Export definitions to downstream packages.
   
   Each package name must be find_package()-able with the exact same case.
   Additionally the exported variables must have a prefix with the same case
   and the suffixes must be INCLUDE_DIRS and LIBRARIES.
   
   :param ARGN: a list of definitions
   :type ARGN: list of strings
   
   @public
   

