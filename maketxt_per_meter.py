from haversine import haversine
import os
import rospy
from sensor_msgs.msg import NavSatFix
from math import sqrt, pow

class Point_distance:
    def __init__(self):
        rospy.init_node('distance_maker', anonymous=True)
        rospy.Subscriber("/gps/fix", NavSatFix, self.fix_callback)
        
        self.is_status =False
        self.pre_lat = 0
        self.pre_lon = 0

        self.file_path = "/home/donghyun/gps_point.txt" #파일을 저장할 위치를 지정한다.

        while not rospy.is_shutdown():
            if self.is_status:
                self.distance()
        


    def fix_callback(self,msg):
        self.is_status = True
        self.latitude = msg.latitude
        self.longiutude = msg.longitude
    
    def distance(self):
        now_lat = self.latitude
        now_lon = self.longiutude
        
        distance_meter = haversine((now_lat,now_lon),(self.pre_lat,self.pre_lon)) *1000

        if distance_meter > 3: #3m마다 gps 포인트를 txt파일에 기록한다.
            self.pre_lat = now_lat
            self.pre_lon = now_lon
            with open(self.file_path, 'a') as f:
                data = '{0}\t{1}\n'.format(now_lat, now_lon)
                f.write(data)
                print("lat, lon:", now_lat, now_lon)



if __name__ == '__main__':
    try:
        rate = rospy.Rate(1000)
        gps=Point_distance()
        rospy.spin()
        rate.sleep()
    except rospy.ROSInterruptException:
        pass

# loc1 = (35.230451439665345, 126.84117683055254)
# loc2 = (35.2304514245416, 126.84117681788118)
# loc3 = (35.22841801330818 , 126.84459283854733)
# loc4 = (35.2257298780273, 126.84131811318919)
# print(haversine(loc4, loc3)*1000)


