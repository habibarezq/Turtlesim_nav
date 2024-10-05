# !/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class poseNode(Node):

    def __init__(self):
        super().__init__("pose_node")
        self.sub_=self.create_subscription(Pose,"/turtle1/pose",self.callback,10)
        self.get_logger().info("Position Node has started !")

    def callback(self,msg: Pose):
        self.get_logger().info(f"Msg Received !!  x = {msg.x} , theta = {msg.theta}")

def main(args=None):
    rclpy.init(args=args)
    node=poseNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ =="__main__":
    main()