
####################################################
ament_cmake_core.index/ament_index_register_resource
####################################################

.. module:: ament_cmake_core.index/ament_index_register_resource


.. function:: ament_index_register_resource(resource_type **kwargs)

   Register a package resource of a specific type with the index.
   
   For both CONTENT as well as CONTENT_FILE CMake generator expressions are
   supported.
   
   :param resource_type: the type of the resource
   :type resource_type: string
   :param CONTENT: the content of the marker file being installed
     as a result of the registration (default: empty string)
   :type CONTENT: string
   :param CONTENT_FILE: the path to a file which will be used to fill
     the marker file being installed as a result of the registration.
     The file can either be a plain file or a template (ending with
     '.in') which is expanded using configure_file() with @ONLY.
     (optional, conflicts with CONTENT)
   :type CONTENT_FILE: string
   :param PACKAGE_NAME: the package name (default: ${PROJECT_NAME})
   :type PACKAGE_NAME: string
   :param AMENT_INDEX_BINARY_DIR: the base path of the generated ament
     index (default: ${CMAKE_BINARY_DIR}/ament_cmake_index)
   :type AMENT_INDEX_BINARY_DIR: string
   :param SKIP_INSTALL: if set skip installing the marker file
   :type SKIP_INSTALL: option
   
   @public
   

