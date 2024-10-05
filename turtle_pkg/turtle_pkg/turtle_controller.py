# !/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
#Whenever we receive from pose node we publish to send_vel
#we need to publish sth new only when we receive certain info thus no need for timer
class TurtleController(Node):

    def __init__(self):
        super().__init__("turtle_controller")
        self.subscriber_=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.pub_=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.get_logger().info("Turtle Controller has started !")
    def pose_callback(self,pose:Pose):

        cmd =Twist()

        if(pose.x >9.5 or pose.x <1.0):
            #make the turtle move in a circular way
            cmd.linear.x=1.0
            cmd.angular.z=0.9
        elif(pose.y >9.5 or pose.y <1.0):
            cmd.linear.x=1.0
            cmd.angular.z=1.0
        else:
            cmd.linear.x=3.0
            cmd.angular.z=1.0
        self.pub_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node=TurtleController()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ =="__main__":
    main()