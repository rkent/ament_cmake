# Copyright 2025 R. Kent James
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This hook is run after all potential python packages have been defined, to do the
# actual install of the packages.

function(_ament_cmake_python_setup_package package_name)
  cmake_parse_arguments(
    ARG "SKIP_COMPILE" "PACKAGE_DIR;VERSION;SETUP_CFG;DESTINATION;SCRIPTS_DESTINATION" "" ${ARGN})
  if(ARG_UNPARSED_ARGUMENTS)
    message(FATAL_ERROR "ament_python_setup_package() called with unused "
      "arguments: ${ARG_UNPARSED_ARGUMENTS}")
  endif()

  set(build_dir "${CMAKE_CURRENT_BINARY_DIR}/ament_cmake_python/${package_name}")

  string(CONFIGURE "\
from setuptools import find_packages
from setuptools import setup

setup(
    name='${package_name}',
    version='${ARG_VERSION}',
    packages=find_packages(
        include=('${package_name}', '${package_name}.*')),
)
" setup_py_content)

  file(GENERATE
    OUTPUT "${build_dir}/setup.py"
    CONTENT "${setup_py_content}"
  )

  if(AMENT_CMAKE_SYMLINK_INSTALL)
    add_custom_target(
      ament_cmake_python_symlink_${package_name}
      COMMAND ${CMAKE_COMMAND} -E create_symlink
        "${ARG_PACKAGE_DIR}" "${build_dir}/${package_name}"
    )
    set(egg_dependencies ament_cmake_python_symlink_${package_name})

    if(ARG_SETUP_CFG)
      add_custom_target(
        ament_cmake_python_symlink_${package_name}_setup
        COMMAND ${CMAKE_COMMAND} -E create_symlink
          "${ARG_SETUP_CFG}" "${build_dir}/setup.cfg"
      )
      list(APPEND egg_dependencies ament_cmake_python_symlink_${package_name}_setup)
    endif()
  else()
    add_custom_target(
      ament_cmake_python_copy_${package_name}
      COMMAND ${CMAKE_COMMAND} -E copy_directory
        "${ARG_PACKAGE_DIR}" "${build_dir}/${package_name}"
    )
    set(egg_dependencies ament_cmake_python_copy_${package_name})

    if(ARG_SETUP_CFG)
      add_custom_target(
        ament_cmake_python_copy_${package_name}_setup
        COMMAND ${CMAKE_COMMAND} -E copy
          "${ARG_SETUP_CFG}" "${build_dir}/setup.cfg"
      )
      list(APPEND egg_dependencies ament_cmake_python_copy_${package_name}_setup)
    endif()
  endif()

  # Technically, we should call find_package(Python3) first to ensure that Python3::Interpreter
  # is available.  But we skip this here because this macro requires ament_cmake, and ament_cmake
  # calls find_package(Python3) for us.
  get_executable_path(python_interpreter Python3::Interpreter BUILD)

  add_custom_target(
    ament_cmake_python_build_${package_name}_egg ALL
    COMMAND ${python_interpreter} setup.py egg_info
    WORKING_DIRECTORY "${build_dir}"
    DEPENDS ${egg_dependencies}
  )

  set(python_version "py${Python3_VERSION_MAJOR}.${Python3_VERSION_MINOR}")

  set(egg_name "${package_name}")
  set(egg_install_name "${egg_name}-${ARG_VERSION}")
  set(egg_install_name "${egg_install_name}-${python_version}")

  install(
    DIRECTORY "${build_dir}/${egg_name}.egg-info/"
    DESTINATION "${ARG_DESTINATION}/${egg_install_name}.egg-info"
  )

  if(ARG_SCRIPTS_DESTINATION)
    file(MAKE_DIRECTORY "${build_dir}/scripts")  # setup.py may or may not create it

    add_custom_target(
      ament_cmake_python_build_${package_name}_scripts ALL
      COMMAND ${python_interpreter} setup.py install_scripts -d scripts
      WORKING_DIRECTORY "${build_dir}"
      DEPENDS ${egg_dependencies}
    )

    if(NOT AMENT_CMAKE_SYMLINK_INSTALL)
      # Not needed for nor supported by symlink installs
      set(_extra_install_args USE_SOURCE_PERMISSIONS)
    endif()

    install(
      DIRECTORY "${build_dir}/scripts/"
      DESTINATION "${ARG_SCRIPTS_DESTINATION}/"
      ${_extra_install_args}
    )
  endif()

  install(
    DIRECTORY "${ARG_PACKAGE_DIR}/"
    DESTINATION "${ARG_DESTINATION}/${package_name}"
    PATTERN "*.pyc" EXCLUDE
    PATTERN "__pycache__" EXCLUDE
  )

  if(NOT ARG_SKIP_COMPILE)
    get_executable_path(python_interpreter_config Python3::Interpreter CONFIGURE)
    # compile Python files
    install(CODE
      "execute_process(
        COMMAND
        \"${python_interpreter_config}\" \"-m\" \"compileall\"
        \"${CMAKE_INSTALL_PREFIX}/${ARG_DESTINATION}/${package_name}\"
      )"
    )
  endif()

  if(package_name IN_LIST AMENT_CMAKE_PYTHON_INSTALL_INSTALLED_NAMES)
    message(FATAL_ERROR
      "ament_python_install_package() a Python module file or package with "
      "the same name '${package_name}' has been installed before")
  endif()
  list(APPEND AMENT_CMAKE_PYTHON_INSTALL_INSTALLED_NAMES "${package_name}")
  set(AMENT_CMAKE_PYTHON_INSTALL_INSTALLED_NAMES
    "${AMENT_CMAKE_PYTHON_INSTALL_INSTALLED_NAMES}" PARENT_SCOPE)
endfunction()

# install packages defined in _ament_python_package_spec_*
foreach(index ${AMENT_PYTHON_PACKAGE_SPEC_INDICIES})
  _ament_cmake_python_setup_package(${AMENT_PYTHON_PACKAGE_SPEC_${index}})
endforeach()
