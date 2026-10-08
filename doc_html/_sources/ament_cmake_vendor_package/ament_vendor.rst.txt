
#######################################
ament_cmake_vendor_package.ament_vendor
#######################################

.. module:: ament_cmake_vendor_package.ament_vendor


.. function:: ament_vendor(TARGET_NAME **kwargs)


   .. note:: This is a macro, and so does not introduce a new scope.

   Build and install an external project as a vendor package.
   
   :param TARGET_NAME: the name to give this vendor package target.
   :type TARGET_NAME: string
   :param SATISFIED: a boolean flag indicating whether there is a system
     package which already satisfies the requirement that this vendor package
     aims to provide.
   :type SATISFIED: option
   :param VCS_TYPE: the mechanism used to fetch the project source code
     (i.e. git, tar, zip, svn, path). Defaults to 'git' if not specified.
   :type VCS_TYPE: string
   :param VCS_URL: the VCS-specific URL to fetch the project source code from.
   :type VCS_URL: string
   :param VCS_VERSION: the VCS-specific version to fetch the projcect source
     code at.
   :type VCS_VERSION: string
   :param PATCHES: paths to patch files to apply to downloaded source code,
     either absolute or relative to the current calling directory. If given a
     directory, all patch files in the directory (non-recursive) will be applied
     in alphabetical order.
   :type PATCHES: list of strings
   :param CMAKE_ARGS: extra arguments to pass to the CMake invocation of the
     external project.
   :type CMAKE_ARGS: list of strings
   :param SOURCE_SUBDIR: subdirectory within the external project to be built
     and installed. Defaults to the root directory.
   :type SOURCE_SUBDIR: string
   :param SKIP_INSTALL: when specified, do not install the external project or
     any associated ament support files.
   :type SKIP_INSTALL: option
   :param GLOBAL_HOOK: rather than requiring consumers of the external project
     to ``find_package`` the vendor package prior to looking for the external
     project, expose the external project globally to any downstream CMake
     projects.
   :type GLOBAL_HOOK: option
   
   @public
   


.. data:: FORCE_BUILD_VENDOR_PKG


   .. note:: 

      
      This variable is a user-editable option,
      meaning it appears within the cache and can be
      edited on the command line by the :code:`-D` flag.
      

   

   :Help text: "Build vendor packages from source, even if system-installed packages are available"

   :Default value: OFF

   :type: bool


.. function:: _ament_vendor(TARGET_NAME VCS_TYPE VCS_URL VCS_VERSION PATCHES CMAKE_ARGS SOURCE_SUBDIR SKIP_INSTALL)

   

