
########################################
ament_cmake_pytest.ament_add_pytest_test
########################################

.. module:: ament_cmake_pytest.ament_add_pytest_test


.. function:: ament_add_pytest_test(testname path **kwargs)

   Add a pytest test.
   
   :param testname: the name of the test
   :type testname: string
   :param path: the path to a file or folder where ``pytest`` should be invoked
     on
   :type path: string
   :param NOCAPTURE: disable pytest output capturing.
     Sets the pytest option '-s'.
   :type NOCAPTURE: option
   :param SKIP_TEST: if set mark the test as being skipped
   :type SKIP_TEST: option
   :param PYTHON_EXECUTABLE: Python executable used to run the test.
     It defaults to the CMake executable target Python3::Interpreter.
   :type PYTHON_EXECUTABLE: string
   :param RUNNER: the path to the test runner script (default: see ament_add_test).
   :type RUNNER: string
   :param TIMEOUT: the test timeout in seconds,
     default defined by ``ament_add_test()``
   :type TIMEOUT: integer
   :param WERROR: If ON, then treat warnings as errors. Default: OFF.
   :type WERROR: bool
   :param WORKING_DIRECTORY: the working directory for invoking the
     command in, default defined by ``ament_add_test()``
   :type WORKING_DIRECTORY: string
   :param ENV: list of env vars to set; listed as ``VAR=value``
   :type ENV: list of strings
   :param APPEND_ENV: list of env vars to append if already set, otherwise set;
     listed as ``VAR=value``
   :type APPEND_ENV: list of strings
   :param APPEND_LIBRARY_DIRS: list of library dirs to append to the appropriate
     OS specific env var, a la LD_LIBRARY_PATH
   :type APPEND_LIBRARY_DIRS: list of strings
   
   @public
   


.. data:: AMENT_CMAKE_PYTEST_WITH_COVERAGE


   .. note:: 

      
      This variable is a user-editable option,
      meaning it appears within the cache and can be
      edited on the command line by the :code:`-D` flag.
      

   

   :Help text: "Generate coverage information for Python tests"

   :Default value: ${coverage_default}

   :type: bool

