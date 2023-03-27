#!/usr/bin/env python3
import rospy
import cv2
import mediapipe as mp
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import controller_manager_msgs.srv
import trajectory_msgs.msg
from obj_detection.msg import quadrant


class pointDetector():
    def __init__(self, mode=False, maxHands=2, modelC=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelC = modelC
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelC, self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

        self.image_pub = rospy.Publisher("rand_topic",Image,queue_size=10)
        #self.quad_pub = rospy.Publisher("quadrant",quadrant,queue_size=10)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("usb_cam/image_raw",Image,self.detector)

        #self.head_pub = rospy.Publisher('/hsrb/head_trajectory_controller/command',trajectory_msgs.msg.JointTrajectory, queue_size=10)

    def findHands(self,img, draw=True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                #for id, lm in enumerate(handLms.landmarks):
        return img
    
    def landmarks(self, img, handNo = 0, draw = True):
        landmark_list = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)

        return landmark_list
    
    def quadrants(self,img,landmark_list):
        blue = (255,0,0)
        green = (0,255,0)
        red = (0,0,255)
        rand = (130,90,40)
        q1 = None
        q2 = None
        q3 = None
        q4 = None
        h,w,c = img.shape
        quadrant = []
        x_cord_list = []
        y_cord_list = []
        if landmark_list:
            o_x, o_y = landmark_list[0][1], landmark_list[0][2]
            for ids in landmark_list[6:9]:
                x_cord_list.append(ids[1])
                y_cord_list.append(ids[2])
            if all(0 < v1 < o_x for v1 in x_cord_list) & all(0 < v2 < o_y for v2 in y_cord_list):
                q1 = True   
                print("quadrant1")
            
            if all(o_x < v1 < w for v1 in x_cord_list) & all(0 < v2 < o_y for v2 in y_cord_list):
                q2 = True
                print("quadrant2")
            
            if all(0 < v1 < o_x for v1 in x_cord_list) & all(o_y < v2 < h for v2 in y_cord_list):
                q3 = True
                print("quadrant3")
            
            if all(o_x < v1 < w for v1 in x_cord_list) & all(o_y < v2 < h for v2 in y_cord_list):
                q4 = True
                print("quadrant4")
            else:
                pass
            quadrant.append([q1,q2,q3,q4])
            img = cv2.rectangle(img,(0,0),(o_x,o_y),blue,2)
            img = cv2.rectangle(img,(o_x,0),(w,o_y),green,2)
            img = cv2.rectangle(img,(0,o_y),(o_x,h),red,2)
            img = cv2.rectangle(img,(o_x,o_y),(w,h),rand,2)
        return(img,quadrant)
    
    def move_head(self,quad_list):
        while self.head_pub.get_num_connections() == 0:
            rospy.sleep(0.1)
        rospy.wait_for_service('/hsrb/controller_manager/list_controllers')
        list_controllers = rospy.ServiceProxy('/hsrb/controller_manager/list_controllers',controller_manager_msgs.srv.ListControllers)
        running = False
        while running is False:
            rospy.sleep(0.1)
            for c in list_controllers().controller:
                if c.name == 'head_trajectory_controller' and c.state == 'running':
                    running = True
        traj = trajectory_msgs.msg.JointTrajectory()
        traj.joint_names = ["head_pan_joint", "head_tilt_joint"]
        p = trajectory_msgs.msg.JointTrajectoryPoint()
        #if q1 q2 etc move robot head
        p.positions = [0, 0]
        p.velocities = [0, 0]
        p.time_from_start = rospy.Duration(3)
        traj.points = [p]

        # publish ROS message
        return traj

    def detector(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        #quad = quadrant()
        img = self.findHands(cv_image)
        lmList = self.landmarks(img)
        img, quadrant_list = self.quadrants(img, lmList)
        #quad.quad = quadrant_list
        cv2.imshow("Image", img)
        cv2.waitKey(1)

        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(img, "bgr8"))
            #self.quad_pub.publish(quad)
        except CvBridgeError as e:
            print(e)


def main():
    rospy.init_node('point_detection')
    detect = pointDetector()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting Down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    #subscribe to image
    #cv_bridge image to cv mat
    #publish and imshow