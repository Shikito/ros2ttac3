import time
import socket

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
import subprocess

from ttac3_actions.action import TTAC3
from utils.win_wsl_socket_client import send_msg

win_python_exe_path = '/mnt/c/Python37/python.exe'
win_wsl_socket_server_path = '/mnt/c/Users/Controller/Documents/Python Scripts/tta_c3/win_wsl_socket_server.py'

class TTAC3ActionServer(Node):

    def __init__(self):
        super().__init__('ttac3_action_server')
        self._action_server = ActionServer(  
            self,
            TTAC3,
            'ttac3',
            self.execute_callback)
    
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        feedback_msg = TTAC3.Feedback()
        
        self.get_logger().info(send_msg(f"xc.move_to_x_y_z({goal_handle.request.xyz_goal[0]},{goal_handle.request.xyz_goal[1]},{goal_handle.request.xyz_goal[2]})".encode()))
        
        goal_handle.publish_feedback(feedback_msg)

        goal_handle.succeed()
        
        result = TTAC3.Result()
        result.is_success = True
        return result

def main(args=None):
    rclpy.init(args=args)
    ttac3_action_server = TTAC3ActionServer()
    rclpy.spin(ttac3_action_server)

if __name__ == '__main__':
    main()