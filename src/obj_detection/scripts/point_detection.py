#!/usr/bin/env python
import rospy
import cv2
import mediapipe as mp
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import controller_manager_msgs.srv
import trajectory_msgs.msg
from std_msgs.msg import String

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

        #self.image_pub = rospy.Publisher("rand_topic",Image,queue_size=10)
        self.quad_pub = rospy.Publisher("quadrant", String, queue_size=1)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("usb_cam/image_raw",Image,self.detector)
    # def findHands(self,img, draw=False):
        

    #     if self.results.multi_hand_landmarks:
    #         for handLms in self.results.multi_hand_landmarks:
    #             if draw:
    #                 self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
    #             #for id, lm in enumerate(handLms.landmarks):
    #     return img
    
    def landmarks(self, img, handNo = 0, draw = False):
        landmark_list = []
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
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
        #Eventually remove
        # blue = (255,0,0)
        # green = (0,255,0)
        # red = (0,0,255)
        # rand = (130,90,40)
        q = None
        h,w,c = img.shape
        x_cord_list = []
        y_cord_list = []
        if landmark_list:
            o_x, o_y = landmark_list[0][1], landmark_list[0][2]
            for ids in landmark_list[6:9]:
                x_cord_list.append(ids[1])
                y_cord_list.append(ids[2])
            if all(0 < v1 < o_x for v1 in x_cord_list) & all(0 < v2 < o_y for v2 in y_cord_list):
                q = "q1"   
                print("quadrant1")
            
            if all(o_x < v1 < w for v1 in x_cord_list) & all(0 < v2 < o_y for v2 in y_cord_list):
                q = "q2"
                print("quadrant2")
            
            if all(0 < v1 < o_x for v1 in x_cord_list) & all(o_y < v2 < h for v2 in y_cord_list):
                q = "q3"
                print("quadrant3")
            
            if all(o_x < v1 < w for v1 in x_cord_list) & all(o_y < v2 < h for v2 in y_cord_list):
                q = "q4"
                print("quadrant4")
            else:
                pass
            #eventually
            # img = cv2.rectangle(img,(0,0),(o_x,o_y),blue,2)
            # img = cv2.rectangle(img,(o_x,0),(w,o_y),green,2)
            # img = cv2.rectangle(img,(0,o_y),(o_x,h),red,2)
            # img = cv2.rectangle(img,(o_x,o_y),(w,h),rand,2)
        return(q)
    

    def detector(self,data):
        try:
            img = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        lmList = self.landmarks(img)
        quadrant = self.quadrants(img, lmList)
        # cv2.imshow("Image", img)
        # cv2.waitKey(1)
        self.quad_pub.publish(quadrant)
        #rospy.sleep(3)


def main():
    rospy.init_node('point_detection')
    detect = pointDetector()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting Down")
    #cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
