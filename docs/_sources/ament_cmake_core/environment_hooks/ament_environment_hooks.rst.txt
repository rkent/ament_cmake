
##########################################################
ament_cmake_core.environment_hooks/ament_environment_hooks
##########################################################

.. module:: ament_cmake_core.environment_hooks/ament_environment_hooks


.. function:: ament_environment_hooks()

   Register environment hooks.
   
   Each file can either be a plain file (ending with a supported extensions)
   or a template which is expanded using configure_file() (ending in
   '.<ext>.in') with @ONLY.
   
   :param ARGN: a list of environment hook files
   :type ARGN: list of strings
   
   @public
   

