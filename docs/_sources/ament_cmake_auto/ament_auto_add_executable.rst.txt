
##########################################
ament_cmake_auto.ament_auto_add_executable
##########################################

.. module:: ament_cmake_auto.ament_auto_add_executable


.. function:: ament_auto_add_executable(target **kwargs)


   .. note:: This is a macro, and so does not introduce a new scope.

   Add an executable target.
   
   All arguments of the CMake function ``add_executable()`` can be
   used beside the custom arguments ``DIRECTORY`` and
   ``NO_TARGET_LINK_LIBRARIES``.
   
   :param target: the name of the executable target
   :type target: string
   :param DIRECTORY: the directory to recursively glob for source
     files with the following extensions: c, cc, cpp, cxx
   :type DIRECTORY: string
   :param NO_TARGET_LINK_LIBRARIES: if set skip linking against
     ``${PROJECT_NAME}_LIBRARIES``
   :type NO_TARGET_LINK_LIBRARIES: option
   
   Append the target to the ``${PROJECT_NAME}_EXECUTABLES`` variable.
   
   @public
   

