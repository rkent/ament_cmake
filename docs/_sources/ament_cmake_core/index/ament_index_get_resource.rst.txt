
###############################################
ament_cmake_core.index/ament_index_get_resource
###############################################

.. module:: ament_cmake_core.index/ament_index_get_resource


.. function:: ament_index_get_resource(var resource_type resource_name **kwargs)

   Get the content of a specific resource from the index.
   
   :param var: the output variable name for the content of the requested
     resource
   :type var: string
   :param resource_type: the type of the resource
   :type resource_type: string
   :param resource_name: the name of the resource
   :type resource_name: string
   :param PREFIX_PATH: the prefix path to search for (default
     ``ament_index_get_prefix_path()``).
   :type PREFIX_PATH: list of strings
   
   @public
   

