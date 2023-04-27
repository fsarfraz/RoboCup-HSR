# CMake generated Testfile for 
# Source directory: /home/farhan/robocup_ws/src/hsrb_moveit_config
# Build directory: /home/farhan/robocup_ws/build/hsrb_moveit_config
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_hsrb_moveit_config_roslaunch-check_launch "/home/farhan/robocup_ws/build/hsrb_moveit_config/catkin_generated/env_cached.sh" "/usr/bin/python3" "/opt/ros/noetic/share/catkin/cmake/test/run_tests.py" "/home/farhan/robocup_ws/build/hsrb_moveit_config/test_results/hsrb_moveit_config/roslaunch-check_launch.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/farhan/robocup_ws/build/hsrb_moveit_config/test_results/hsrb_moveit_config" "/opt/ros/noetic/share/roslaunch/cmake/../scripts/roslaunch-check -o \"/home/farhan/robocup_ws/build/hsrb_moveit_config/test_results/hsrb_moveit_config/roslaunch-check_launch.xml\" -t \"/home/farhan/robocup_ws/src/hsrb_moveit_config/launch\" ")
set_tests_properties(_ctest_hsrb_moveit_config_roslaunch-check_launch PROPERTIES  _BACKTRACE_TRIPLES "/opt/ros/noetic/share/catkin/cmake/test/tests.cmake;160;add_test;/opt/ros/noetic/share/roslaunch/cmake/roslaunch-extras.cmake;66;catkin_run_tests_target;/home/farhan/robocup_ws/src/hsrb_moveit_config/CMakeLists.txt;26;roslaunch_add_file_check;/home/farhan/robocup_ws/src/hsrb_moveit_config/CMakeLists.txt;0;")
subdirs("gtest")
