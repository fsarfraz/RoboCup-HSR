
(cl:in-package :asdf)

(defsystem "obj_detection-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "quadrant" :depends-on ("_package_quadrant"))
    (:file "_package_quadrant" :depends-on ("_package"))
  ))