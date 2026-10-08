
###################################
ament_cmake_core.core/ament_package
###################################

.. module:: ament_cmake_core.core/ament_package


.. function:: ament_package()


   .. note:: This is a macro, and so does not introduce a new scope.

   Install the package.xml file, and generate code for
   ``find_package`` so that other packages can get information about
   this package.
   
   .. note:: It must be called once for each package.
     It is indirectly calling``ament_package_xml()`` which will
     provide additional output variables.
   
   :param CONFIG_EXTRAS: a list of CMake files containing extra stuff
     that should be accessible to users of this package after
     ``find_package``\ -ing it.
     The file can either be a plain CMake file (ending in '.cmake') or
     a template which is expanded using configure_file() (ending in
     '.cmake.in') with @ONLY.
     If the global variable ${PROJECT_NAME}_CONFIG_EXTRAS is set it
     will be appended to the explicitly passed argument.
   :type CONFIG_EXTRAS: list of files
   :param CONFIG_EXTRAS_POST: a list of CMake files containing extra
     stuff that should be accessible to users of this package after
     ``find_package``\ -ing it.
     The file can either be a plain CMake file (ending in '.cmake') or
     a template which is expanded using configure_file() (ending in
     '.cmake.in') with @ONLY.
     If the global variable ${PROJECT_NAME}_CONFIG_EXTRAS_POST is set it
     will be prepended to the explicitly passed argument.
   :type CONFIG_EXTRAS_POST: list of files
   
   @public
   


.. function:: _ament_package(**kwargs)

   

