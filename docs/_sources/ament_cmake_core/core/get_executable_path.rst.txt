
#########################################
ament_cmake_core.core/get_executable_path
#########################################

.. module:: ament_cmake_core.core/get_executable_path


.. function:: get_executable_path(var target_or_path **kwargs)

   Get the path to an executable at build or configure time.
   
   The argument target_or_path may either be a path to an executable (such as
   PYTHON_EXECUTABLE), or an executable target (such as Python3::Interpreter).
   If the argument is an executable target then its location will be returned.
   otherwise the original argument will be returned unmodified.
   
   Use CONFIGURE when an executable is to be run at configure time, such as when
   using execute_process().
   The returned value will be the path to the process.
   Use BUILD when an executable is to be run at build or test time, such as
   when using add_custom_command() or add_test().
   The returned value will be either a path or a generator expression that
   evaluates to the path of an executable target.
   
   :param var: the output variable name
   :type var: string
   :param target_or_path: imported executable target or a path to an executable
   :param target_or_path: string
   
   @public
   

