# !/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import sys
import math

class TurtleController(Node):

    def __init__(self):
        super().__init__("turtle_nav")
        self.subscriber_=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.pub_=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.timer=self.create_timer(1.0,self.go_to_goal)
        self.get_logger().info("Turtle Controller has started !")
        self.pose=None

    def pose_callback(self,data):
        self.pose=data
    
    def go_to_goal(self):
        goal=Pose()
        goal.x=float(sys.argv[1]) #to take input from terminal
        goal.y=float(sys.argv[2])
        #goal.theta=float(sys.argv[3])
        
        new_vel=Twist()

        delta_x=goal.x -self.pose.x
        delta_y=goal.y-self.pose.y

        #Ecludian Distance to go to target
        dis_to_goal=math.sqrt((delta_x * delta_x) + (delta_y * delta_y))
        #Angle to Goal
        angle_to_goal=math.atan2(delta_y,delta_x)       #atan2 is inverse tan function

        #Log distance and theta
        #self.get_logger().info(f"DTG : {dis_to_goal:.2f} , ATG : {angle_to_goal:.2f}")

        #now we need to adjust linear and angular velocity to new info
        dis_tolerance=0.3
        angle_tolerance=0.3 #to avoid overshooting

        angle_error=angle_to_goal-self.pose.theta

        if angle_error > angle_tolerance: #we didnt reach the desired angle yet
            new_vel.angular.z=angle_error
        else:
            if dis_to_goal > dis_tolerance: #we didnt reach the distance to goal
                new_vel.linear.x=dis_to_goal
            else: 
                new_vel.linear.x=0.0
                self.get_logger().info("Goal Reached!")
                quit()
    
                
        self.pub_.publish(new_vel)


def main(args=None):
    rclpy.init(args=args)
    node=TurtleController()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ =="__main__":
    main()