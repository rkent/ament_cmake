
###################################
ament_cmake_pytest.ament_has_pytest
###################################

.. module:: ament_cmake_pytest.ament_has_pytest


.. function:: ament_has_pytest(var **kwargs)

   Check if the Python module `pytest` was found.
   
   :param var: the output variable name
   :type var: string
   :param QUIET: suppress the CMake warning if pytest is not found, if not set
     and pytest was not found a CMake warning is printed
   :type QUIET: option
   :param PYTHON_EXECUTABLE: Python executable used to check for pytest
     It defaults to the CMake executable target Python3::Interpreter.
   :type PYTHON_EXECUTABLE: string
   
   @public
   

