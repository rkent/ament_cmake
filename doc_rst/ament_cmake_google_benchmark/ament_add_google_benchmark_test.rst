
############################################################
ament_cmake_google_benchmark.ament_add_google_benchmark_test
############################################################

.. module:: ament_cmake_google_benchmark.ament_add_google_benchmark_test


.. function:: ament_add_google_benchmark_test(target **kwargs)

   Add an existing executable using google benchmark as a test.
   
   Register an executable created with ament_add_google_benchmark_executable() as
   a test.
   If the specified target does not exist the registration is skipped.
   
   :param target: the target name which will also be used as the test name
   :type target: string
   :param RUNNER: the path to the test runner script (default: see
     ament_add_test).
   :type RUNNER: string
   :param TIMEOUT: the test timeout in seconds,
     default defined by ``ament_add_test()``
   :type TIMEOUT: integer
   :param WORKING_DIRECTORY: the working directory for invoking the
     executable in, default defined by ``ament_add_test()``
   :type WORKING_DIRECTORY: string
   :param RUN_PARALLEL: if set allow the test to be run in parallel
     with other tests
   :type RUN_PARALLEL: option
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
   

