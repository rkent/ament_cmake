
#################################################
ament_cmake_libraries.ament_libraries_deduplicate
#################################################

.. module:: ament_cmake_libraries.ament_libraries_deduplicate


.. function:: ament_libraries_deduplicate(VAR)


   .. note:: This is a macro, and so does not introduce a new scope.

   Deduplicate libraries.
   
   If the list contains duplicates only the last value is kept.
   
   :param VAR: the output variable name
   :type VAR: string
   :param ARGN: a list of libraries.
     Each element might either a build configuration keyword or a library.
   :type ARGN: list of strings
   
   @public
   

