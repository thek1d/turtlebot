#!/usr/bin/env python3
import rospy
import statistics
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from package_turtlebot_ogu.msg import Lidar


class Lidar_Sensor():

    def __init__(self):
        pass
    
    def process_lidar_values(self, msg, lidar_obj):
        temp1 = list(msg.ranges[0:11])
        temp2 = list(msg.ranges[350:360])
        ''' setting 0° to the middle of the list, median is by elem 10 '''
        temp1.reverse()
        temp2.reverse()
        twisted_list = temp1 + temp2
        lidar_obj.Values_0.Lidar_Range_Values_At_0 = twisted_list
        lidar_obj.Values_0.Lidar_Value_At_0 = statistics.median(lidar_obj.Values_0.Lidar_Range_Values_At_0)
        lidar_obj.Values_0.Mean = self.calc_mean_of_range(lidar_obj.Values_0.Lidar_Range_Values_At_0)

        temp1 = list(msg.ranges[90 : 101])
        temp1 = list(msg.ranges[80 : 90])
        temp1.reverse()
        temp2.reverse()
        twisted_list = temp1 + temp2
        lidar_obj.Values_90.Lidar_Range_Values_At_90 = twisted_list
        lidar_obj.Values_90.Lidar_Value_At_90 = statistics.median(lidar_obj.Values_90.Lidar_Range_Values_At_90)
        lidar_obj.Values_90.Mean = self.calc_mean_of_range(lidar_obj.Values_90.Lidar_Range_Values_At_90)

        temp1 = list(msg.ranges[180 : 191])
        temp1 = list(msg.ranges[170 : 180])
        temp1.reverse()
        temp2.reverse()
        twisted_list = temp1 + temp2
        lidar_obj.Values_180.Lidar_Range_Values_At_180 = twisted_list
        lidar_obj.Values_180.Lidar_Value_At_180 = statistics.median(lidar_obj.Values_180.Lidar_Range_Values_At_180)
        lidar_obj.Values_180.Mean = self.calc_mean_of_range(lidar_obj.Values_180.Lidar_Range_Values_At_180)

        temp1 = list(msg.ranges[270 : 281])
        temp1 = list(msg.ranges[260 : 270])
        temp1.reverse()
        temp2.reverse()
        twisted_list = temp1 + temp2
        lidar_obj.Values_270.Lidar_Range_Values_At_270 = twisted_list
        lidar_obj.Values_270.Lidar_Value_At_270 = statistics.median(lidar_obj.Values_270.Lidar_Range_Values_At_270)
        lidar_obj.Values_270.Mean = self.calc_mean_of_range(lidar_obj.Values_270.Lidar_Range_Values_At_270)


    def calc_mean_of_range(self, range_values):
        temp = -1.0
        for i in range_values:
            temp = temp + i
        return temp/len(range_values)

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