#!/usr/bin/env python
import rospy
import controller_manager_msgs.srv
import trajectory_msgs.msg
from obj_detection.msg import quadrant


class move_head():
    def __init__(self):
        self.quad_sub = rospy.Subscriber("quadrant",quadrant,self.move_head)

    def move_head(self,data):
        quadrant_list = data
        print(quadrant_list)

def main():
    rospy.init_node('move_head')
    move = move_head()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting Down")
if __name__ == '__main__':
    main()