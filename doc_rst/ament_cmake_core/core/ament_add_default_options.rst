
###############################################
ament_cmake_core.core/ament_add_default_options
###############################################

.. module:: ament_cmake_core.core/ament_add_default_options


.. function:: ament_add_default_options(**kwargs)


   .. note:: This is a macro, and so does not introduce a new scope.

   Explicit call to add default CMake options (e.g. BUILD_SHARED_LIBS)
   
   .. note:: It can be called multiple times, but should be called
     once for any package that requires the options.
   
   :param EXCLUDE_BUILD_SHARED_LIBS: Exclude the BUILD_SHARED_LIBS option
   
   @public
   


.. data:: BUILD_SHARED_LIBS


   .. note:: 

      
      This variable is a user-editable option,
      meaning it appears within the cache and can be
      edited on the command line by the :code:`-D` flag.
      

   

   :Help text: "Global flag to cause add_library() to create shared libraries if on. \
       If set to true, this will cause all libraries to be built shared \
       unless the library was explicitly added as a static library."

   :Default value: ON

   :type: bool

