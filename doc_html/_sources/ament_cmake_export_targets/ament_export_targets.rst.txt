
###############################################
ament_cmake_export_targets.ament_export_targets
###############################################

.. module:: ament_cmake_export_targets.ament_export_targets


.. function:: ament_export_targets(**kwargs)


   .. note:: This is a macro, and so does not introduce a new scope.

   Export targets to downstream packages.
   
   Each export name must have been used to install targets using
   ``install(TARGETS ... EXPORT name NAMESPACE my_namespace ...)``.
   The ``install(EXPORT ...)`` invocation is handled by this macros.
   
   :param HAS_LIBRARY_TARGET: if set, an environment variable will be defined
     so that the library can be found at runtime
   :type HAS_LIBRARY_TARGET: option
   :keyword NAMESPACE: the exported namespace for the target if set. 
      The default is the value of ``${PROJECT_NAME}::``.
      This is an advanced option. It should be used carefully and clearly documented
      in a usage guide for any package that makes use of this option.
   :type NAMESPACE: string
   :param ARGN: a list of export names
   :type ARGN: list of strings
   
   @public
   

