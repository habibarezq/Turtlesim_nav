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
        self.target_dis = 0.0
        self.start_dis=0.0
        self.speed = 0.0
        self.timer=None
        self.start_pose = Pose()
        self.pose=Pose()

    def pose_callback(self, data):
        self.pose = data

    def get_distance(self, start_pose, current_pose):
        return math.sqrt((current_pose.x - start_pose.x)**2 + (current_pose.y - start_pose.y)**2)
    
    def move(self, distance): #using spin_once
        new_vel=Twist()

        new_vel.linear.x = 1.0

        new_vel.angular.z = 0.0

        self.start_pose = Pose()
        self.start_pose.x = self.pose.x
        self.start_pose.y = self.pose.y
        self.start_pose.theta = self.pose.theta


        while self.get_distance(self.start_pose, self.pose) < distance:
            self.pub_.publish(new_vel)
            rclpy.spin_once(self, timeout_sec=0.1)

    # Stop the turtle once the distance is covered
        new_vel.linear.x = 0.0
        self.pub_.publish(new_vel)
        self.get_logger().info("Goal Reached!")
        quit()

    def move2(self, distance):

    # Ensure we have received a valid pose before proceeding
        while self.pose.x == 0.0 and self.pose.y == 0.0:
            rclpy.spin_once(self)  #waiting for position data to be avaliable

        self.target_dis = distance
        self.speed = 1.0

        self.start_pose.x = self.pose.x
        self.start_pose.y = self.pose.y
        
        self.get_logger().info(f"Starting position: {self.start_pose.x}, {self.start_pose.y}")
        self.timer = self.create_timer(0.1, self.move_callback)

    
    def move_callback(self):
        cur_dis=self.get_distance(self.start_pose,self.pose)
        
        new_vel=Twist()
        self.get_logger().info(f"current distance {cur_dis} , target {self.target_dis}")
        
        dis_tolerance=0.03

        if cur_dis+dis_tolerance >= self.target_dis:  #Target Distance reached
            new_vel.linear.x=0.0
            self.timer.cancel()
            self.get_logger().info("Goal Reached!")

        else: #not reached
            new_vel.linear.x=self.target_dis-cur_dis
            self.get_logger().warn("Not Reached!")
        
        self.pub_.publish(new_vel)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()

    distance_to_move=2.0
    node.move2(distance_to_move)

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
#if you want to use spin_once use while loop with it to keep monitoring position
#but if you want to use spin u should pair it with timer 
#you only want to start the timer when distance method is called so instead of starting it
#in init you should start it in move