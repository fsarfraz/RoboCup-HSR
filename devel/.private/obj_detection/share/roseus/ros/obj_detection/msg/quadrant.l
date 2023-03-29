;; Auto-generated. Do not edit!


(when (boundp 'obj_detection::quadrant)
  (if (not (find-package "OBJ_DETECTION"))
    (make-package "OBJ_DETECTION"))
  (shadow 'quadrant (find-package "OBJ_DETECTION")))
(unless (find-package "OBJ_DETECTION::QUADRANT")
  (make-package "OBJ_DETECTION::QUADRANT"))

(in-package "ROS")
;;//! \htmlinclude quadrant.msg.html


(defclass obj_detection::quadrant
  :super ros::object
  :slots (_quad ))

(defmethod obj_detection::quadrant
  (:init
   (&key
    ((:quad __quad) (let (r) (dotimes (i 0) (push nil r)) r))
    )
   (send-super :init)
   (setq _quad __quad)
   self)
  (:quad
   (&optional __quad)
   (if __quad (setq _quad __quad)) _quad)
  (:serialization-length
   ()
   (+
    ;; bool[] _quad
    (* 1    (length _quad)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool[] _quad
     (write-long (length _quad) s)
     (dotimes (i (length _quad))
       (if (elt _quad i) (write-byte -1 s) (write-byte 0 s))
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool[] _quad
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _quad (make-list n))
     (dotimes (i n)
     (setf (elt _quad i) (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
     ))
   ;;
   self)
  )

(setf (get obj_detection::quadrant :md5sum-) "92aebcddb7b3cd49dd137a53a53ec72d")
(setf (get obj_detection::quadrant :datatype-) "obj_detection/quadrant")
(setf (get obj_detection::quadrant :definition-)
      "bool[] quad
")



(provide :obj_detection/quadrant "92aebcddb7b3cd49dd137a53a53ec72d")


