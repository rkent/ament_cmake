
####################################
ament_cmake_core.core/normalize_path
####################################

.. module:: ament_cmake_core.core/normalize_path


.. function:: normalize_path(var path)

   Normalize a path by collapsing redundant parts and up-level references.
   
   This may change the meaning of a path that contains symbolic links.
   
   :param var: the output variable name
   :type var: string
   :param path: the path
   :type path: string
   

