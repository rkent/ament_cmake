
############
ament_vendor
############

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
   
   The AMENT_VENDOR_POLICY cache entry and the SATISFIED argument
   control whether or not this function builds the vendor package.
   If you want something other than the default, set AMENT_VENDOR_POLICY via the
   command line:
   
      * If you are using cmake directly: cmake -DAMENT_VENDOR_POLICY:STRING=DEFAULT ...
      * If you are using colcon: colcon --cmake-args -DAMENT_VENDOR_POLICY:STRING=DEFAULT ...
   
     AMENT_VENDOR_POLICY: String option that specifies how ament_vendor behaves,
                          the allowed values are listed in the following.
       DEFAULT: Vendor if ``SATISFIED`` argument is not supplied or false,
                do not vendor otherwise.
       FORCE_BUILD_VENDOR: Always vendor, independently of the value of the
                     ``SATISFIED`` argument.
       NEVER_VENDOR: Never vendor, and raise an error if ``SATISFIED`` argument
                     is not supplied or false.
       NEVER_VENDOR_IGNORE_SATISFIED_CHECK: Never vendor, and do not raise
                     an error even if ``SATISFIED`` argument is not supplied
                     or false. This option is unsupported by most packages,
                     so use at your own risk, as it could break the buid.
   
   To check if a package has been actually vendored, check if the target name
   passed as TARGET_NAME exists with if(TARGET <target_name>).
   
   


.. data:: FORCE_BUILD_VENDOR_PKG


   .. note:: 

      
      This variable is a user-editable option,
      meaning it appears within the cache and can be
      edited on the command line by the :code:`-D` flag.
      

   

   :Help text: "Build vendor packages from source, even if system-installed packages are available"

   :Default value: OFF

   :type: bool

