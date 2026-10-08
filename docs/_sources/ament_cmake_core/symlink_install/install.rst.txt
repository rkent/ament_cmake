
########################################
ament_cmake_core.symlink_install/install
########################################

.. module:: ament_cmake_core.symlink_install/install


.. function:: install(signature)

   Overwrite CMake install command to use symlinks instead of copying resources.
   
   :param signature: one of the CMake keywords used to choose between the
     different install signatures, e.g. DIRECTORY, FILES, PROGRAMS, TARGETS.
   :type signature: string
   :param ARGN: the same arguments as the CMake install command.
   :type ARGN: various
   

