import rospy
from sensor_msgs.msg import LaserScan
def callback_laser(msg):
  # 120 degrees into 3 regions
  regions = [ 
    min(min(msg.ranges[0:2]), 10),
    min(min(msg.ranges[3:5]), 10),
    min( min(msg.ranges[6:9]), 10),
    ]
  rospy.loginfo(regions)
def main():
  rospy.init_node('sensors')
  sub= rospy.Subscriber("/mybot/laser/scan", LaserScan, callback_laser)
  rospy.spin()
if __name__ == '__main__':
  main()
