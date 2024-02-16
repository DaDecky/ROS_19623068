#!/usr/bin/env python
import rospy
from tugas_rsc.msg import DronePos

def callback_fn(pos):
    #get_caller_id(): Get fully resolved name of local node
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", message.data)
    print("Heard position:")
    print(f"x: {pos.x}")
    print(f"y: {pos.y}")
    print(f"z: {pos.z}")
    print(f"status: {pos.status}")
    print("----------------")
    
    
def commander():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'commander' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('commander', anonymous=True)

    rospy.Subscriber("/drone_status", DronePos, callback_fn)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    commander()
