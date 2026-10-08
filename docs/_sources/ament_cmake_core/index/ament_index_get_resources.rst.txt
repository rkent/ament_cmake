
################################################
ament_cmake_core.index/ament_index_get_resources
################################################

.. module:: ament_cmake_core.index/ament_index_get_resources


.. function:: ament_index_get_resources(var resource_type **kwargs)

   Get all registered package resources of a specific type from the index.
   
   :param var: the output variable name
   :type var: list of resource names
   :param resource_type: the type of the resource
   :type resource_type: string
   :param PREFIX_PATH: the prefix path to search for (default
     ``ament_index_get_prefix_path()``).
   :type PREFIX_PATH: list of strings
   
   @public
   

