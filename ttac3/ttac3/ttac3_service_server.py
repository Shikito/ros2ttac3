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

        self.pub_ttac3_state = self.create_publisher(
            Int32MultiArray,
            'ttac3_state',
            10
        )
        timer_period = 0.01 # seconds
        self.timer = self.create_timer(timer_period, self.pub_ttac3_state_callback)

        self._invisible_state = [-1, -1, -1]
        self.ttac3_state = self._invisible_state
    
    def pub_ttac3_state_callback(self):
        msg = Int32MultiArray()
        msg.data = self.ttac3_state
        self.pub_ttac3_state.publish(msg)

    def move_ttac3_callback(self, request, response):
        self.get_logger().info('Receive a request!')
        self.ttac3_state = self._invisible_state
        self.pub_ttac3_state_callback()
        self.get_logger().info(send_msg(f"xc.move_to_x_y_z({request.xyz_goal[0]},{request.xyz_goal[1]},{request.xyz_goal[2]})".encode()))
        self.ttac3_state = [
            int(request.xyz_goal[0]),
            int(request.xyz_goal[1]),
            int(request.xyz_goal[2])
        ]
        self.get_logger().info('Done!')

        response.is_success = True
        return response

def main(args=None):
    rclpy.init(args=args)
    ttac3_service_server = TTAC3ServiceServer()
    rclpy.spin(ttac3_service_server)

if __name__=='__main__':
    main()