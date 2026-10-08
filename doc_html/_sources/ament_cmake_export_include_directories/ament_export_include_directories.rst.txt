
#######################################################################
ament_cmake_export_include_directories.ament_export_include_directories
#######################################################################

.. module:: ament_cmake_export_include_directories.ament_export_include_directories


.. function:: ament_export_include_directories()


   .. note:: This is a macro, and so does not introduce a new scope.

   Export include directories to downstream packages.
   
   Relative paths will be exported before absolute paths.
   Non existing absolute paths will result in warning.
   
   :param ARGN: a list of include directories where each value might
     be either an absolute path or path relative to the
     CMAKE_INSTALL_PREFIX.
   :type ARGN: list of strings
   
   @public
   

