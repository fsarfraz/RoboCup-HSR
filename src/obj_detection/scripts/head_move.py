#!/usr/bin/env python
import rospy
import controller_manager_msgs.srv
import trajectory_msgs.msg
from std_msgs.msg import String


class move_head():
    def __init__(self):
        self.increment = 0
        self.quad_sub = rospy.Subscriber("quadrant", String, self.move)
        self.list_controllers = rospy.ServiceProxy('/hsrb/controller_manager/list_controllers',controller_manager_msgs.srv.ListControllers)
        #rospy.Timer(rospy.Duration(10), self.move_head)
        self.head_pub = rospy.Publisher('/hsrb/head_trajectory_controller/command',trajectory_msgs.msg.JointTrajectory, queue_size=1)

    # def init(self):


    def move(self,quad):
        quadrant = quad.data
        traj = trajectory_msgs.msg.JointTrajectory()
        traj.joint_names = ["head_pan_joint", "head_tilt_joint"]
        p = trajectory_msgs.msg.JointTrajectoryPoint()
        #if q1 q2 etc move robot head
        if quadrant == "q1":
            p.positions = [self.increment, 0.2]
            p.velocities = [0, 0]
            p.time_from_start = rospy.Duration(2)
            traj.points = [p]
            self.increment += 0.01
        
        if quadrant == "q2":
            p.positions = [self.increment, 0.2]
            p.velocities = [0, 0]
            p.time_from_start = rospy.Duration(2)
            traj.points = [p]
            self.increment -= 0.01
        
        if quadrant == "q3":  
            p.positions = [self.increment, -0.2]
            p.velocities = [0, 0]
            p.time_from_start = rospy.Duration(2)
            traj.points = [p]
            self.increment += 0.01  

        if quadrant == "q4":
            p.positions = [self.increment, -0.2]
            p.velocities = [0, 0]
            p.time_from_start = rospy.Duration(2)
            traj.points = [p]
            self.increment -= 0.01    
        # publish ROS message
        # print("traj", traj)
        self.head_pub.publish(traj)

def main():
    rospy.init_node('move_head')
    move = move_head()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting Down")



if __name__ == '__main__':
    main()