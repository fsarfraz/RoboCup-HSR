#!/usr/bin/env python3

from copy import deepcopy
import math
import sys
import numpy as np

import geometry_msgs.msg
from moveit_msgs.msg import CollisionObject, AttachedCollisionObject
import moveit_commander
import moveit_msgs.msg
import rospy
import shape_msgs.msg
from tf.transformations import quaternion_from_euler, quaternion_multiply
import trajectory_msgs.msg
from sensor_msgs.msg import Image, PointCloud, CameraInfo, PointCloud2, PointField
import ros_numpy
import open3d as o3d
import sys, os


class MoveItPickAndPlaceDemo(object):
    def __init__(self, wait=0.0):
        # initialize
        
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node("moveit_demo", anonymous=True)

        self.reference_frame = "odom"
        arm = moveit_commander.MoveGroupCommander("arm", wait_for_servers=0.0)
        base = moveit_commander.MoveGroupCommander("base", wait_for_servers=0.0)
        gripper = moveit_commander.MoveGroupCommander("gripper",wait_for_servers=0.0)
        head = moveit_commander.MoveGroupCommander("head",  wait_for_servers=0.0)
        self.whole_body = moveit_commander.MoveGroupCommander("whole_body",wait_for_servers=0.0)
        self.scene = moveit_commander.planning_scene_interface.PlanningSceneInterface()
        self._pub_co = rospy.Publisher('/collision_object', CollisionObject, queue_size=100)

        # self.point_cloud = rospy.Subscriber('/segmented_point_ros',PointCloud2,self.point_cloud_callback)
        # self.point_cloud = rospy.wait_for_message('/segmented_point_ros', PointCloud2)
        self.pnt_cld = np.load("pnt_cld.npy")
        # self.pnt_cld = ros_numpy.point_cloud2.pointcloud2_to_xyz_array(self.point_cloud, remove_nans=True)
        # np.save("pnt_cld.npy",self.pnt_cld)
        print("-----THIS IS WORKING ONCE--------\n")

        # self.pcd = o3d.geometry.PointCloud()
        # self.pcd.points = o3d.utility.Vector3dVector(self.pnt_cld)
        # self.pcd = self.pcd.uniform_down_sample(10)
        # self.pcd.estimate_normals()


        # mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(self.pcd, depth=4)
        # mesh.compute_vertex_normals()

        # mesh.paint_uniform_color(np.array([0.7, 0.7, 0.7]))
        # o3d.io.write_triangle_mesh(("mesh.ply"), mesh)
        # self.path = "mesh.ply"

        # mesh = o3d.io.read_triangle_mesh('mesh.ply')
        # o3d.visualization.draw_geometries([mesh])

        # rospy.sleep(5)


        #calculate center of bottle
        self.point_cloud_array = np.array(self.pnt_cld)
        self.centroid = (np.sum(self.point_cloud_array, axis = 0) / len(self.point_cloud_array))
        print(self.centroid)
        self.x_cent = self.centroid[0] + 0.6
        self.y_cent = self.centroid[1]
        self.z_cent = -self.centroid[2] + 0.2

        self.whole_body.allow_replanning(True)
        self.whole_body.set_planning_time(5)
        self.whole_body.set_pose_reference_frame(self.reference_frame)
        self.end_effector = self.whole_body.get_end_effector_link()
        rospy.sleep(1)

        # remove all objects
        self.scene.remove_attached_object(self.end_effector)
        self.scene.remove_world_object()
        rospy.sleep(1)


        # move_to_neutral
        rospy.loginfo("step1: move_to_neutral")
        base.go()
        arm.set_named_target("neutral")
        arm.go()
        head.set_named_target("neutral")
        head.go()
        gripper.set_joint_value_target("hand_motor_joint", 0.5)
        gripper.go()
        rospy.logdebug("done")
        rospy.sleep(wait)


    #add Mesh and try adding boxes for table and wall
        # self.add_box("table",
        #              [0.3, 0.8, 0.01],
        #              [0.5, 0.0, 0.5 - 0.01 / 2])
        # self.add_box("wall",
        #              [0.3, 0.01, 0.1],
        #              [0.5, 0.0, 0.5 + 0.1 / 2])
        # self.add_mesh("target1",
        #              [self.x_cent, self.y_cent, self.z_cent], self.path)
        self.add_cylinder("target1",
                          0.02, 0.12,
                          [self.x_cent, self.y_cent, self.z_cent])
        
        rospy.sleep(1)

        # pick target1
        self.whole_body.set_support_surface_name("table")
        rospy.loginfo("step2: pick target1")
        grasps = self.make_grasps("target1",
                                  (0.707, 0.0, 0.707, 0.0),
                                  quality=lambda x, y, z, roll, pitch, yaw: 1 - abs(pitch),  # noqa
                                  x=[-0.07],
                                  pitch=[-0.2, -0.1, 0, 0.1, 0.2])
        self.pick("target1", grasps)
        rospy.logdebug("done")
        rospy.sleep(wait)

        #pick target2
        # rospy.loginfo("step4: pick target1")
        # yaw = [i / 180.0 * math.pi for i in range(0, 360, 30)]
        # grasps = self.make_grasps("target1",
        #                           (1, 0, 0, 0),
        #                           z=[0.1],
        #                           yaw=yaw)
        # self.pick("target2", grasps)
        # rospy.logdebug("done")
        # rospy.sleep(wait)

        # place target1
        # rospy.loginfo("step3: place target1")
        # location = self.make_place_location(0.4, -0.2, 0.5 + 0.2 / 2)
        # self.place("target1", location)
        # rospy.logdebug("done")
        # rospy.sleep(wait)

        # gripper.set_joint_value_target("hand_motor_joint", 1.0)
        # gripper.go()

        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)


    def pick(self, target, grasps):
        n_attempts = 0
        max_pick_attempts = 10
        result = None

        while (result != moveit_msgs.msg.MoveItErrorCodes.SUCCESS) and \
              (n_attempts < max_pick_attempts):
            n_attempts += 1
            rospy.loginfo("Pick attempt: " + str(n_attempts))
            result = self.whole_body.pick(target, grasps)
            rospy.sleep(0.2)
        if result != moveit_msgs.msg.MoveItErrorCodes.SUCCESS:
            self.scene.remove_attached_object(self.end_effector)
        return result

    def place(self, target, location):
        n_attempts = 0
        max_pick_attempts = 10
        result = None

        while (result != moveit_msgs.msg.MoveItErrorCodes.SUCCESS) and \
              (n_attempts < max_pick_attempts):
            n_attempts += 1
            rospy.loginfo("Place attempt: " + str(n_attempts))
            result = self.whole_body.place(target, location)
            rospy.sleep(0.2)
        if result != moveit_msgs.msg.MoveItErrorCodes.SUCCESS:
            self.scene.remove_attached_object(self.end_effector)
        return result

    def make_gripper_posture(self, pos, effort=0.0):
        t = trajectory_msgs.msg.JointTrajectory()
        t.joint_names = ["hand_motor_joint"]
        tp = trajectory_msgs.msg.JointTrajectoryPoint()
        tp.positions = [pos]
        tp.effort = [effort]
        tp.time_from_start = rospy.Duration(2.0)
        t.points.append(tp)
        return t

    def make_gripper_translation(self, min_dist, desired, vector, frame=None):
        g = moveit_msgs.msg.GripperTranslation()
        g.direction.vector.x = vector[0]
        g.direction.vector.y = vector[1]
        g.direction.vector.z = vector[2]
        if frame is None:
            g.direction.header.frame_id = self.end_effector
        else:
            g.direction.header.frame_id = frame
        g.min_distance = min_dist
        g.desired_distance = desired
        return g

    def make_pose(self, init, x, y, z, roll, pitch, yaw):
        pose = geometry_msgs.msg.PoseStamped()
        pose.header.frame_id = self.reference_frame
        q = quaternion_from_euler(roll, pitch, yaw)
        q = quaternion_multiply(init, q)
        pose.pose.orientation.x = q[0]
        pose.pose.orientation.y = q[1]
        pose.pose.orientation.z = q[2]
        pose.pose.orientation.w = q[3]
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = z
        return pose

    def make_grasps(self, target, init,
                    quality=None,
                    x=[0], y=[0], z=[0],
                    roll=[0], pitch=[0], yaw=[0]):
        poses = self.scene.get_object_poses([target])
        pose = poses[target]
        g = moveit_msgs.msg.Grasp()
        g.pre_grasp_posture = self.make_gripper_posture(0.8)
        g.grasp_posture = self.make_gripper_posture(0.2, -0.01)
        g.pre_grasp_approach \
            = self.make_gripper_translation(0.01, 0.02, [0.0, 0.0, 1.0])
        g.post_grasp_retreat \
            = self.make_gripper_translation(0.01, 0.02, [0.0, 0.0, 1.0],
                                            "base_footprint")
        grasps = []
        for ix in x:
            for iy in y:
                for iz in z:
                    for iroll in roll:
                        for ipitch in pitch:
                            for iyaw in yaw:
                                x = pose.position.x + ix
                                y = pose.position.y + iy
                                z = pose.position.z + iz
                                g.grasp_pose = self.make_pose(init,
                                                              x, y, z,
                                                              iroll,
                                                              ipitch,
                                                              iyaw)
            g.id = str(len(grasps))
            g.allowed_touch_objects = ["target1"]
            g.max_contact_force = 0
            if quality is None:
                g.grasp_quality = 1.0
            else:
                g.grasp_quality = quality(ix, iy, iz, iroll, ipitch, iyaw)
            grasps.append(deepcopy(g))
        return grasps

    def make_place_location(self, x, y, z):
        location = moveit_msgs.msg.PlaceLocation()
        location.pre_place_approach \
            = self.make_gripper_translation(0.03, 0.05, [0, 0, -1.0],
                                            "base_footprint")
        location.post_place_posture \
            = self.make_gripper_posture(0.8)
        location.post_place_retreat \
            = self.make_gripper_translation(0.03, 0.05, [0, 0, -1.0])
        location.place_pose = self.make_pose((0, 0, 0, 1),
                                             x, y, z,
                                             0, 0, 0)
        return location




    def add_box(self, name, size, pos):
        p = geometry_msgs.msg.PoseStamped()
        p.header.frame_id = self.reference_frame
        p.pose.position.x = pos[0]
        p.pose.position.y = pos[1]
        p.pose.position.z = pos[2]
        p.pose.orientation.w = 1.0
        self.scene.add_box(name, p, size)

    # def add_mesh(self, name, pos, filepath):
    #     p = geometry_msgs.msg.PoseStamped()
    #     p.header.frame_id = self.reference_frame
    #     p.pose.position.x = pos[0]
    #     p.pose.position.y = pos[1]
    #     p.pose.position.z = pos[2]
    #     p.pose.orientation.w = 1.0
    #     self.scene.make_mesh(name,p,filepath)
    #     self.scene.add_mesh(name,p,filepath)
    #     # self._pub_co.publish(co)
    
    def add_cylinder(self, name, radius, height, pos):
        co = moveit_msgs.msg.CollisionObject()
        co.operation = moveit_msgs.msg.CollisionObject.ADD
        co.id = name
        co.header.frame_id = self.reference_frame
        box = shape_msgs.msg.SolidPrimitive()
        box.type = shape_msgs.msg.SolidPrimitive.CYLINDER
        box.dimensions = [height, radius]
        co.primitives = [box]
        p = geometry_msgs.msg.Pose()
        p.position.x = pos[0]
        p.position.y = pos[1]
        p.position.z = pos[2]
        co.primitive_poses = [p]
        # self.scene._pub_co.publish(co)
        self._pub_co.publish(co)

    



#rospy.waitformessage method is possible
    # def point_cloud_callback(self,cloud):
    #     sys.path.append(os.path.abspath(os.path.join('..', 'include')))
    #     self.pnt_cld = ros_numpy.point_cloud2.pointcloud2_to_xyz_array(cloud, remove_nans=True)
    #     self.pcd = o3d.geometry.PointCloud()
    #     self.pcd.points = o3d.utility.Vector3dVector(self.pnt_cld)
    #     voxel_down_pcd = self.pcd.voxel_down_sample(voxel_size=0.002)
    #     voxel_down_pcd.estimate_normals()

    #     # to obtain a consistent normal orientation
    #     voxel_down_pcd.orient_normals_towards_camera_location(voxel_down_pcd.get_center())

    #     # or you might want to flip the normals to make them point outward, not mandatory
    #     voxel_down_pcd.normals = o3d.utility.Vector3dVector( - np.asarray(voxel_down_pcd.normals))

    #     # surface reconstruction using Poisson reconstruction
    #     mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(voxel_down_pcd, depth=5)

    #     # paint uniform color to better visualize, not mandatory
    #     mesh.paint_uniform_color(np.array([0.7, 0.7, 0.7]))
    #     o3d.io.write_triangle_mesh(("mesh.ply"), mesh)
    #     self.path = "mesh.ply"
    #     print("-------IS THIS WORKING-------")

if __name__ == "__main__":
    MoveItPickAndPlaceDemo(float(sys.argv[1]) if len(sys.argv) > 1 else 0.0)
        
