
###################################################
ament_cmake_export_libraries.ament_export_libraries
###################################################

.. module:: ament_cmake_export_libraries.ament_export_libraries


.. function:: ament_export_libraries()


   .. note:: This is a macro, and so does not introduce a new scope.

   Export libraries to downstream packages.
   
   :param ARGN: a list of libraries.
     Each element might either be an absolute path to a library, a
     CMake library target, or a CMake imported libary target.
     Note that this macro is not needed for interface library targets.
     If a plain library name is passed it will be redirected to
     ament_export_library_names().
   :type ARGN: list of strings
   
   @public
   

