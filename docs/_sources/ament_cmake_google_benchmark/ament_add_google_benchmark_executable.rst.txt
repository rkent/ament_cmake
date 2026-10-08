
##################################################################
ament_cmake_google_benchmark.ament_add_google_benchmark_executable
##################################################################

.. module:: ament_cmake_google_benchmark.ament_add_google_benchmark_executable


.. function:: ament_add_google_benchmark_executable(target)


   .. note:: This is a macro, and so does not introduce a new scope.

   Add an executable using google benchmark.
   
   Call add_executable(target ARGN) and link it against the google benchmark
   libraries.
   It does not register the executable as a test.
   
   If google benchmark is not available the specified target is not being created
   and therefore the target existence should be checked before being used.
   
   :param target: the target name which will also be used as the test name
   :type target: string
   :param ARGN: the list of source files
   :type ARGN: list of strings
   :param SKIP_LINKING_MAIN_LIBRARIES: if set skip linking against the google
     benchmark main libraries
   :type SKIP_LINKING_MAIN_LIBRARIES: option
   
   @public
   


.. function:: _ament_add_google_benchmark_executable(target **kwargs)

   

