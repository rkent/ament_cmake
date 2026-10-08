
#####################################################
ament_cmake_export_link_flags.ament_export_link_flags
#####################################################

.. module:: ament_cmake_export_link_flags.ament_export_link_flags


.. function:: ament_export_link_flags()


   .. note:: This is a macro, and so does not introduce a new scope.

   Export link flags to downstream packages.
   
   Each package name must be find_package()-able with the exact same case.
   Additionally the exported variables must have a prefix with the same case
   and the suffixes must be INCLUDE_DIRS and LIBRARIES.
   
   :param ARGN: a list of link flags
   :type ARGN: list of strings
   
   @public
   

