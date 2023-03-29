; Auto-generated. Do not edit!


(cl:in-package obj_detection-msg)


;//! \htmlinclude quadrant.msg.html

(cl:defclass <quadrant> (roslisp-msg-protocol:ros-message)
  ((quad
    :reader quad
    :initarg :quad
    :type (cl:vector cl:boolean)
   :initform (cl:make-array 0 :element-type 'cl:boolean :initial-element cl:nil)))
)

(cl:defclass quadrant (<quadrant>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <quadrant>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'quadrant)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name obj_detection-msg:<quadrant> is deprecated: use obj_detection-msg:quadrant instead.")))

(cl:ensure-generic-function 'quad-val :lambda-list '(m))
(cl:defmethod quad-val ((m <quadrant>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader obj_detection-msg:quad-val is deprecated.  Use obj_detection-msg:quad instead.")
  (quad m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <quadrant>) ostream)
  "Serializes a message object of type '<quadrant>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'quad))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if ele 1 0)) ostream))
   (cl:slot-value msg 'quad))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <quadrant>) istream)
  "Deserializes a message object of type '<quadrant>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'quad) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'quad)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:not (cl:zerop (cl:read-byte istream)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<quadrant>)))
  "Returns string type for a message object of type '<quadrant>"
  "obj_detection/quadrant")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'quadrant)))
  "Returns string type for a message object of type 'quadrant"
  "obj_detection/quadrant")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<quadrant>)))
  "Returns md5sum for a message object of type '<quadrant>"
  "92aebcddb7b3cd49dd137a53a53ec72d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'quadrant)))
  "Returns md5sum for a message object of type 'quadrant"
  "92aebcddb7b3cd49dd137a53a53ec72d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<quadrant>)))
  "Returns full string definition for message of type '<quadrant>"
  (cl:format cl:nil "bool[] quad~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'quadrant)))
  "Returns full string definition for message of type 'quadrant"
  (cl:format cl:nil "bool[] quad~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <quadrant>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'quad) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <quadrant>))
  "Converts a ROS message object to a list"
  (cl:list 'quadrant
    (cl:cons ':quad (quad msg))
))
