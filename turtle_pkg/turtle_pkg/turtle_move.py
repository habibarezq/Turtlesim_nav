# !/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

class TurtleController(Node):

    def __init__(self):
        super().__init__('turtle_move')
        self.pub_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.get_logger().info("Move Node has started!")
        self.start_pose = Pose()
        self.pose=Pose()

    def pose_callback(self, data):
        self.pose = data

    def get_distance(self, start_pose, current_pose):
        return math.sqrt((current_pose.x - start_pose.x)**2 + (current_pose.y - start_pose.y)**2)
    
    def move(self, distance):
        new_vel=Twist()

        new_vel.linear.x = 1.0
        new_vel.linear.y = 0.0
        new_vel.linear.z = 0.0

        # No angular velocity (no rotation)
        new_vel.angular.x = 0.0
        new_vel.angular.y = 0.0
        new_vel.angular.z = 0.0

        # Store a **copy** of the turtle's starting position
        self.start_pose = Pose()
        self.start_pose.x = self.pose.x
        self.start_pose.y = self.pose.y
        self.start_pose.theta = self.pose.theta

        self.start_pose = Pose()
        self.start_pose.x = self.pose.x
        self.start_pose.y = self.pose.y
        self.start_pose.theta = self.pose.theta

        self.get_logger().info("Here!!")

        while self.get_distance(self.start_pose, self.pose) < distance:
            self.pub_.publish(new_vel)
            rclpy.spin_once(self, timeout_sec=0.1)

    # Stop the turtle once the distance is covered
        new_vel.linear.x = 0.0
        self.pub_.publish(new_vel)
        self.get_logger().info("Goal Reached!")
        quit()


def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()

    # Let ROS spin to keep the node active and pose updates coming
    rclpy.spin_once(node)

    # Move the turtle by a certain distance
    distance_to_move=2.0
    node.move(distance_to_move)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
