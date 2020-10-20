import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray

from ttac3_interfaces.srv import TTAC3
from utils.win_wsl_socket_client import send_msg

class TTAC3ServiceServer(Node):

    def __init__(self):
        super().__init__('ttac3_service_server')
        self._service_server = self.create_service(
            TTAC3,
            'ttac3',
            self.move_ttac3_callback
        )

        self.pub_ttac3_state = 

    def move_ttac3_callback(self, request, response):
        self.get_logger().info('Receive a request!')
        self.get_logger().info(send_msg(f"xc.move_to_x_y_z({request.xyz_goal[0]},{request.xyz_goal[1]},{request.xyz_goal[2]})".encode()))
        self.get_logger().info('Done!')

        response.is_success = True
        return response

def main(args=None):
    rclpy.init(args=args)
    ttac3_service_server = TTAC3ServiceServer()
    rclpy.spin(ttac3_service_server)

if __name__=='__main__':
    main()