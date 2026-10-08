
#################################
ament_cmake_gmock.ament_add_gmock
#################################

.. module:: ament_cmake_gmock.ament_add_gmock


.. function:: ament_add_gmock(target **kwargs)


   .. note:: This is a macro, and so does not introduce a new scope.

   Add a gmock.
   
   Call add_executable(target ARGN), link it against the gmock library
   and register the executable as a test.
   
   :param target: the target name which will also be used as the test name
   :type target: string
   :param ARGN: the list of source files
   :type ARGN: list of strings
   :param RUNNER: the path to the test runner script (default: see ament_add_test).
   :type RUNNER: string
   :param TIMEOUT: the test timeout in seconds,
     default defined by ``ament_add_test()``
   :type TIMEOUT: integer
   :param WORKING_DIRECTORY: the working directory for invoking the
     executable in, default defined by ``ament_add_test()``
   :type WORKING_DIRECTORY: string
   :param SKIP_LINKING_MAIN_LIBRARIES: if set skip linking against the gmock
     main libraries
   :type SKIP_LINKING_MAIN_LIBRARIES: option
   :param SKIP_TEST: if set mark the test as being skipped
   :type SKIP_TEST: option
   :param ENV: list of env vars to set; listed as ``VAR=value``
   :type ENV: list of strings
   :param APPEND_ENV: list of env vars to append if already set, otherwise set;
     listed as ``VAR=value``
   :type APPEND_ENV: list of strings
   :param APPEND_LIBRARY_DIRS: list of library dirs to append to the appropriate
     OS specific env var, a la LD_LIBRARY_PATH
   :type APPEND_LIBRARY_DIRS: list of strings
   
   @public
   

