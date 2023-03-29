// Auto-generated. Do not edit!

// (in-package obj_detection.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class quadrant {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.quad = null;
    }
    else {
      if (initObj.hasOwnProperty('quad')) {
        this.quad = initObj.quad
      }
      else {
        this.quad = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type quadrant
    // Serialize message field [quad]
    bufferOffset = _arraySerializer.bool(obj.quad, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type quadrant
    let len;
    let data = new quadrant(null);
    // Deserialize message field [quad]
    data.quad = _arrayDeserializer.bool(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.quad.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'obj_detection/quadrant';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '92aebcddb7b3cd49dd137a53a53ec72d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool[] quad
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new quadrant(null);
    if (msg.quad !== undefined) {
      resolved.quad = msg.quad;
    }
    else {
      resolved.quad = []
    }

    return resolved;
    }
};

module.exports = quadrant;
