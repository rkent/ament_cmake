
###############################################
ament_cmake_pytest.ament_get_pytest_cov_version
###############################################

.. module:: ament_cmake_pytest.ament_get_pytest_cov_version


.. function:: ament_get_pytest_cov_version(var **kwargs)

   Check if the Python module `pytest-cov` was found and get its version if it is.
   
   :param var: the output variable name
   :type var: string
   :param PYTHON_EXECUTABLE: Python executable used to check the version
     It defaults to the CMake executable target Python3::Interpreter.
   :type PYTHON_EXECUTABLE: string
   
   @public
   

