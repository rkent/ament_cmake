
#######################################################
ament_cmake_export_libraries.ament_export_library_names
#######################################################

.. module:: ament_cmake_export_libraries.ament_export_library_names


.. function:: ament_export_library_names(**kwargs)


   .. note:: This is a macro, and so does not introduce a new scope.

   Export library names to downstream packages.
   The libraries are either searched in the paths passed in as
   LIBRARY_DIRS or if none are specified in the default locations.
   
   :param ARGN: a list of library names.
   :type ARGN: list of strings
   :param LIBRARY_DIRS: an optional list of search paths.
   :type LIBRARY_DIRS: list of paths
   
   @public
   

