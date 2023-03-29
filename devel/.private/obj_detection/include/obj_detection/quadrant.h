// Generated by gencpp from file obj_detection/quadrant.msg
// DO NOT EDIT!


#ifndef OBJ_DETECTION_MESSAGE_QUADRANT_H
#define OBJ_DETECTION_MESSAGE_QUADRANT_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace obj_detection
{
template <class ContainerAllocator>
struct quadrant_
{
  typedef quadrant_<ContainerAllocator> Type;

  quadrant_()
    : quad()  {
    }
  quadrant_(const ContainerAllocator& _alloc)
    : quad(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<uint8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint8_t>> _quad_type;
  _quad_type quad;





  typedef boost::shared_ptr< ::obj_detection::quadrant_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::obj_detection::quadrant_<ContainerAllocator> const> ConstPtr;

}; // struct quadrant_

typedef ::obj_detection::quadrant_<std::allocator<void> > quadrant;

typedef boost::shared_ptr< ::obj_detection::quadrant > quadrantPtr;
typedef boost::shared_ptr< ::obj_detection::quadrant const> quadrantConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::obj_detection::quadrant_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::obj_detection::quadrant_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::obj_detection::quadrant_<ContainerAllocator1> & lhs, const ::obj_detection::quadrant_<ContainerAllocator2> & rhs)
{
  return lhs.quad == rhs.quad;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::obj_detection::quadrant_<ContainerAllocator1> & lhs, const ::obj_detection::quadrant_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace obj_detection

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::obj_detection::quadrant_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::obj_detection::quadrant_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::obj_detection::quadrant_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::obj_detection::quadrant_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::obj_detection::quadrant_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::obj_detection::quadrant_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::obj_detection::quadrant_<ContainerAllocator> >
{
  static const char* value()
  {
    return "92aebcddb7b3cd49dd137a53a53ec72d";
  }

  static const char* value(const ::obj_detection::quadrant_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x92aebcddb7b3cd49ULL;
  static const uint64_t static_value2 = 0xdd137a53a53ec72dULL;
};

template<class ContainerAllocator>
struct DataType< ::obj_detection::quadrant_<ContainerAllocator> >
{
  static const char* value()
  {
    return "obj_detection/quadrant";
  }

  static const char* value(const ::obj_detection::quadrant_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::obj_detection::quadrant_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool[] quad\n"
;
  }

  static const char* value(const ::obj_detection::quadrant_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::obj_detection::quadrant_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.quad);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct quadrant_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::obj_detection::quadrant_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::obj_detection::quadrant_<ContainerAllocator>& v)
  {
    s << indent << "quad[]" << std::endl;
    for (size_t i = 0; i < v.quad.size(); ++i)
    {
      s << indent << "  quad[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.quad[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // OBJ_DETECTION_MESSAGE_QUADRANT_H