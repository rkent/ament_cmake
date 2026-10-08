
###############################
ament_cmake_test.ament_add_test
###############################

.. module:: ament_cmake_test.ament_add_test


.. function:: ament_add_test(testname **kwargs)

   Add a test.
   
   A test is expected to generate a JUnit result file
   ${AMENT_TEST_RESULTS_DIR}/$PROJECT_NAME}/${testname}.xml.
   Failing to do so is considered a failed test.
   
   :param testname: the name of the test
   :type testname: string
   :param COMMAND: the command including its arguments to invoke
   :type COMMAND: list of strings
   :param OUTPUT_FILE: the path of the file to pipe the output to
   :type OUTPUT_FILE: string
   :param RUNNER: the path to the test runner script (default: run_test.py).
   :type RUNNER: string
   :param TIMEOUT: the test timeout in seconds, default: 60
   :type TIMEOUT: integer
   :param WORKING_DIRECTORY: the working directory for invoking the
     command in, default: CMAKE_CURRENT_BINARY_DIR
   :type WORKING_DIRECTORY: string
   :param GENERATE_RESULT_FOR_RETURN_CODE_ZERO: generate a test result
     file when the command invocation returns with code zero
     command in, default: FALSE
   :type GENERATE_RESULT_FOR_RETURN_CODE_ZERO: option
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
   :param SKIP_RETURN_CODE: return code signifying that the test has been
     skipped and did not fail OR succeed
   :type SKIP_RETURN_CODE: integer
   
   @public
   


.. function:: "${testname}"(COMMAND ${cmd_wrapper} WORKING_DIRECTORY "${ARG_WORKING_DIRECTORY}")


   .. warning:: This is a CTest test definition, do not call this manually. Use the "ctest" program to execute this test.

   

