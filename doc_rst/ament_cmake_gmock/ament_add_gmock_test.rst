
######################################
ament_cmake_gmock.ament_add_gmock_test
######################################

.. module:: ament_cmake_gmock.ament_add_gmock_test


.. function:: ament_add_gmock_test(target **kwargs)

   Add an existing executable using gmock as a test.
   
   Register an executable created with ament_add_gmock_executable() as a test.
   If the specified target does not exist the registration is skipped.
   
   :param target: the target name which will also be used as the test name
     if TEST_NAME is not set
   :type target: string
   :param RUNNER: the path to the test runner script (default: see ament_add_test).
   :type RUNNER: string
   :param TIMEOUT: the test timeout in seconds,
     default defined by ``ament_add_test()``
   :type TIMEOUT: integer
   :param WORKING_DIRECTORY: the working directory for invoking the
     executable in, default defined by ``ament_add_test()``
   :type WORKING_DIRECTORY: string
   :param TEST_NAME: the name of the test
   :type TEST_NAME: string
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
   

