
###########################
ament_cmake_core.core/stamp
###########################

.. module:: ament_cmake_core.core/stamp


.. function:: stamp(path)

     :param path:  file name
   
     Uses ``configure_file`` to generate a file ``filepath.stamp`` hidden
     somewhere in the build tree.  This will cause cmake to rebuild its
     cache when ``filepath`` is modified.
   

