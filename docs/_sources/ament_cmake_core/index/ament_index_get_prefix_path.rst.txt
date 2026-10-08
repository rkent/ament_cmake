
##################################################
ament_cmake_core.index/ament_index_get_prefix_path
##################################################

.. module:: ament_cmake_core.index/ament_index_get_prefix_path


.. function:: ament_index_get_prefix_path(var **kwargs)

   Get the prefix path including the folder from the binary dir.
   
   :param var: the output variable name for the prefix path
   :type var: string
   :param SKIP_AMENT_PREFIX_PATH: if set skip adding the paths from the
     environment variable ``AMENT_PREFIX_PATH``
   :type SKIP_AMENT_PREFIX_PATH: option
   :param SKIP_BINARY_DIR: if set skip adding the folder within the binary dir
   :type SKIP_BINARY_DIR: option
   
   @public
   

