
#########################################################
ament_cmake_target_dependencies.ament_target_dependencies
#########################################################

.. module:: ament_cmake_target_dependencies.ament_target_dependencies


.. function:: ament_target_dependencies(target **kwargs)

   Add the interface targets or definitions, include directories and libraries
   of packages to a target.
   
   Each package name must have been find_package()-ed before.
   Additionally the exported variables must have a prefix with the same case
   and the suffixes must be either _INTERFACES or _DEFINITIONS, _INCLUDE_DIRS,
   _LIBRARIES, _LIBRARY_DIRS, and _LINK_FLAGS.
   If _INTERFACES is not empty it will be used exclusively, otherwise the other
   variables are being used.
   If _LIBRARY_DIRS is not empty, _LIBRARIES which are not absolute paths already
   will be searched in those directories and their absolute paths will be used instead.
   
   :param target: the target name
   :type target: string
   :param ARGN: a list of package names, which can optionally start
     with a SYSTEM keyword, followed by an INTERFACE or PUBLIC keyword.
     If it starts with a SYSTEM keyword, it will be used in
     target_include_directories() calls.
     If it starts (or follows) with an INTERFACE or PUBLIC keyword,
     this keyword will be used in the target_*() calls.
   :type ARGN: list of strings
   
   @public
   

