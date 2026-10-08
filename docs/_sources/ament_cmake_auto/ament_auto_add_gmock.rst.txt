
#####################################
ament_cmake_auto.ament_auto_add_gmock
#####################################

.. module:: ament_cmake_auto.ament_auto_add_gmock


.. function:: ament_auto_add_gmock(target **kwargs)


   .. note:: This is a macro, and so does not introduce a new scope.

   Add a gmock with all found test dependencies.
   
   Call add_gmock(target ARGN), link it against the gmock libraries
   and all found test dependencies.
   
   If gmock is not available the specified target is not being created and
   therefore the target existence should be checked before being used.
   
   :param target: the target name which will also be used as the test name
   :type target: string
   :param ARGN: the list of source files and parameters
   :type ARGN: list of strings
   
   @public
   

