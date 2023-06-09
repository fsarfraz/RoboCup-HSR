# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "obj_detection: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iobj_detection:/home/farhan/robocup_ws/src/obj_detection/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(obj_detection_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/farhan/robocup_ws/src/obj_detection/msg/quadrant.msg" NAME_WE)
add_custom_target(_obj_detection_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "obj_detection" "/home/farhan/robocup_ws/src/obj_detection/msg/quadrant.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(obj_detection
  "/home/farhan/robocup_ws/src/obj_detection/msg/quadrant.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/obj_detection
)

### Generating Services

### Generating Module File
_generate_module_cpp(obj_detection
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/obj_detection
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(obj_detection_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(obj_detection_generate_messages obj_detection_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/farhan/robocup_ws/src/obj_detection/msg/quadrant.msg" NAME_WE)
add_dependencies(obj_detection_generate_messages_cpp _obj_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(obj_detection_gencpp)
add_dependencies(obj_detection_gencpp obj_detection_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS obj_detection_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(obj_detection
  "/home/farhan/robocup_ws/src/obj_detection/msg/quadrant.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/obj_detection
)

### Generating Services

### Generating Module File
_generate_module_eus(obj_detection
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/obj_detection
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(obj_detection_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(obj_detection_generate_messages obj_detection_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/farhan/robocup_ws/src/obj_detection/msg/quadrant.msg" NAME_WE)
add_dependencies(obj_detection_generate_messages_eus _obj_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(obj_detection_geneus)
add_dependencies(obj_detection_geneus obj_detection_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS obj_detection_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(obj_detection
  "/home/farhan/robocup_ws/src/obj_detection/msg/quadrant.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/obj_detection
)

### Generating Services

### Generating Module File
_generate_module_lisp(obj_detection
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/obj_detection
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(obj_detection_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(obj_detection_generate_messages obj_detection_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/farhan/robocup_ws/src/obj_detection/msg/quadrant.msg" NAME_WE)
add_dependencies(obj_detection_generate_messages_lisp _obj_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(obj_detection_genlisp)
add_dependencies(obj_detection_genlisp obj_detection_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS obj_detection_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(obj_detection
  "/home/farhan/robocup_ws/src/obj_detection/msg/quadrant.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/obj_detection
)

### Generating Services

### Generating Module File
_generate_module_nodejs(obj_detection
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/obj_detection
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(obj_detection_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(obj_detection_generate_messages obj_detection_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/farhan/robocup_ws/src/obj_detection/msg/quadrant.msg" NAME_WE)
add_dependencies(obj_detection_generate_messages_nodejs _obj_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(obj_detection_gennodejs)
add_dependencies(obj_detection_gennodejs obj_detection_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS obj_detection_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(obj_detection
  "/home/farhan/robocup_ws/src/obj_detection/msg/quadrant.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/obj_detection
)

### Generating Services

### Generating Module File
_generate_module_py(obj_detection
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/obj_detection
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(obj_detection_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(obj_detection_generate_messages obj_detection_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/farhan/robocup_ws/src/obj_detection/msg/quadrant.msg" NAME_WE)
add_dependencies(obj_detection_generate_messages_py _obj_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(obj_detection_genpy)
add_dependencies(obj_detection_genpy obj_detection_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS obj_detection_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/obj_detection)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/obj_detection
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(obj_detection_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/obj_detection)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/obj_detection
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(obj_detection_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/obj_detection)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/obj_detection
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(obj_detection_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/obj_detection)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/obj_detection
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(obj_detection_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/obj_detection)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/obj_detection\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/obj_detection
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(obj_detection_generate_messages_py std_msgs_generate_messages_py)
endif()
