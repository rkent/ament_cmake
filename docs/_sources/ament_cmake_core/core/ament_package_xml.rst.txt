
#######################################
ament_cmake_core.core/ament_package_xml
#######################################

.. module:: ament_cmake_core.core/ament_package_xml


.. function:: ament_package_xml()


   .. note:: This is a macro, and so does not introduce a new scope.

   Parse package.xml from ``DIRECTORY`` and
   make several information available to CMake.
   
   .. note:: It is called automatically by ``ament_package()`` if not
     called manually before.  It must be called once in each package,
     after calling ``project()`` where the project name must match the
     package name.
   
   :param DIRECTORY: the directory of the package.xml (default
     ``${CMAKE_CURRENT_SOURCE_DIR}``).
   :type DIRECTORY: string
   
   :outvar PACKAGE_NAME: the name of the package from the manifest
   :outvar <packagename>_VERSION: the version number
   :outvar <packagename>_MAINTAINER: the name and email of the
     maintainer(s)
   
   @public
   


.. function:: _ament_package_xml(dest_dir **kwargs)


   .. note:: This is a macro, and so does not introduce a new scope.

   

