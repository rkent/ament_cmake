
###############################################
ament_cmake_core.index/ament_index_has_resource
###############################################

.. module:: ament_cmake_core.index/ament_index_has_resource


.. function:: ament_index_has_resource(var resource_type resource_name **kwargs)

   Check if the index contains a specific resource.
   
   :param var: the prefix path if the resource exists, FALSE otherwise
   :type var: string or FALSE
   :param resource_type: the type of the resource
   :type resource_type: string
   :param resource_name: the name of the resource
   :type resource_name: string
   :param PREFIX_PATH: the prefix path to search for (default
     ``ament_index_get_prefix_path()``).
   :type PREFIX_PATH: list of strings
   
   @public
   

