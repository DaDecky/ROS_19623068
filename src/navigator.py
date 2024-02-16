#!/usr/bin/env python
import rospy
from tugas_rsc.msg import DronePos

def navigator():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher('/drone_status', DronePos, queue_size=10)
    #we need to initialize the node
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'navigator' node 
    rospy.init_node('navigator', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(1) # 1hz


    #keep publishing until a Ctrl-C is pressed
    i = 0

    #initial value
    x = 0
    y = 0
    z = 0
    while (not rospy.is_shutdown()) and i <= 1000:
        drone_pos = DronePos()
        drone_pos.x = x
        drone_pos.y = y
        drone_pos.z = z

        if 1 <= z <= 9:
            drone_pos.status = "takeoff"
        elif z == 10:
            drone_pos.status = "fly"
        else:
            drone_pos.status = "land"
            


        # hello_str = "hello world %s" % i
        # rospy.loginfo(drone_pos)
        print("Sent postition:")
        print(f"x: {drone_pos.x}")
        print(f"y: {drone_pos.y}")
        print(f"z: {drone_pos.z}")
        print(f"status: {drone_pos.status}")
        print("----------------")

        pub.publish(drone_pos)
        rate.sleep()
        i+=1;x+=1;y-=1;z+=1
        
        if z > 10:
            z=0


if __name__ == '__main__':
    try:
        navigator()
    except rospy.ROSInterruptException:
        pass
