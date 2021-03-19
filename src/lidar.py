#!/usr/bin/env python3
import rospy
import statistics
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from package_turtlebot_ogu.msg import Lidar


class Lidar_Sensor():

    range_max = 3.5

    temp1 = temp2 = list()
    def process_lidar_values(self, msg, lidar_obj):
        ''' for details see http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html '''
        temp1 = list(msg.ranges[0:18])
        temp2 = list(msg.ranges[344:359])

        lidar_obj.Front.Range_Values = temp2 + temp1
        ''' check if smallest value of sensor < max range of sensor '''
        lidar_obj.Front.Value       = min(min(lidar_obj.Front.Range_Values), Lidar_Sensor.range_max)
        lidar_obj.Front.Mean         = self.calc_mean(lidar_obj.Front.Range_Values)

        lidar_obj.Front_Left.Range_Values = list(msg.ranges[19:55])
        lidar_obj.Front_Left.Value        = min(min(lidar_obj.Front_Left.Range_Values), Lidar_Sensor.range_max)
        lidar_obj.Front_Left.Mean         = self.calc_mean(lidar_obj.Front_Left.Range_Values)

        lidar_obj.Left.Range_Values = list(msg.ranges[56:92])
        lidar_obj.Left.Value        = min(min(lidar_obj.Left.Range_Values), Lidar_Sensor.range_max)
        lidar_obj.Left.Mean         = self.calc_mean(lidar_obj.Left.Range_Values)

        lidar_obj.Right.Range_Values = list(msg.ranges[270:306])
        lidar_obj.Right.Value        = min(min(lidar_obj.Right.Range_Values), Lidar_Sensor.range_max)
        lidar_obj.Right.Mean         = self.calc_mean(lidar_obj.Right.Range_Values)

        lidar_obj.Front_Right.Range_Values = list(msg.ranges[307:343])
        lidar_obj.Front_Right.Value        = min(min(lidar_obj.Front_Right.Range_Values), Lidar_Sensor.range_max)
        lidar_obj.Front_Right.Mean         = self.calc_mean(lidar_obj.Front_Right.Range_Values)

    

    def calc_mean(self, range_values):
        temp = 0.0
        for i in range_values:
            temp = temp + i
        return i / len(range_values)
    
def main():
    rospy.init_node('lidar_node')
    lidar_sensor = Lidar_Sensor()
    lidar_msg_obj = Lidar()
    rospy.Subscriber('/scan', LaserScan, callback=lidar_sensor.process_lidar_values, callback_args=lidar_msg_obj, queue_size=1)
    lidar_pub = rospy.Publisher("/lidar_values", Lidar, queue_size=1)
    
    while not rospy.is_shutdown():
        lidar_pub.publish(lidar_msg_obj)

if __name__ == '__main__':
    main()