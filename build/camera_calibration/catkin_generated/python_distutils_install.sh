#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/farhan/robocup_ws/src/image_pipeline/camera_calibration"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/farhan/robocup_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/farhan/robocup_ws/install/lib/python3/dist-packages:/home/farhan/robocup_ws/build/camera_calibration/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/farhan/robocup_ws/build/camera_calibration" \
    "/usr/bin/python3" \
    "/home/farhan/robocup_ws/src/image_pipeline/camera_calibration/setup.py" \
    egg_info --egg-base /home/farhan/robocup_ws/build/camera_calibration \
    build --build-base "/home/farhan/robocup_ws/build/camera_calibration" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/farhan/robocup_ws/install" --install-scripts="/home/farhan/robocup_ws/install/bin"
