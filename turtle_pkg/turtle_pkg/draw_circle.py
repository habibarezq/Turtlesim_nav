# !/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class drawCircle(Node):

    def __init__(self):
        super().__init__("draw_circle")
        self.pub_=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.timer=self.create_timer(0.5,self.send_vel) #to publish the velocity every 0.5sec
        self.get_logger().info("Draw Circle has started !")
        

    def send_vel(self):
        msg=Twist()
        msg.linear.x=2.0 #moves forward to the right
        msg.angular.z=1.0
        self.pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node=drawCircle()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ =="__main__":
    main()