
############################################################################
ament_cmake_version.ament_export_development_version_if_higher_than_manifest
############################################################################

.. module:: ament_cmake_version.ament_export_development_version_if_higher_than_manifest


.. function:: ament_export_development_version_if_higher_than_manifest(development_version)


   .. note:: This is a macro, and so does not introduce a new scope.

   Set the exported package version to the passed value if the package
   version in the manifest is lower.
   
   It is recommended to append the suffix ``-dev`` to the passed upcoming
   version number.
   If the package version in the manifest is equal or newer than the passed
   development version this function call becomes a no-op.
   If the function is called multiple times only the higher version number will
   be used.
   
   .. note:: It is indirectly calling``ament_package_xml()`` if that hasn't
     happened already.
   
   :param target: development_version
   :type target: string
   
   @public
   

