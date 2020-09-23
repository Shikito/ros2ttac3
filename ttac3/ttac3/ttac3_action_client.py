import sys
import rclpy

from rclpy.action import ActionClient
from rclpy.node import Node

from ttac3_actions.action import TTAC3

class TTAC3ActionClient(Node):

    def __init__(self):
        super().__init__('ttac3_action_client')
        self._action_client = ActionClient(
            self,
            TTAC3,
            'ttac3')

    def send_goal(self, xyz_goal):
        goal_msg = TTAC3.Goal()
        goal_msg.xyz_goal = xyz_goal

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        self.get_logger().info('Send Goal Async')

        self._send_goal_future.add_done_callback(self.goal_response_callback)
        

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.current_state))

    def goal_response_callback(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected: (')
            return
        
        self.get_logger().info('Goal accepted')

        self._get_result_future = goal_handle.get_result_async()

        self._get_result_future.add_done_callback(self.get_result_callback)
    
    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.is_success))
        rclpy.shutdown()
    

def main(args=sys.argv):
    # import ipdb; ipdb.set_trace()
    if not isinstance(args, list):
        print("isinstance(args, list) is must be True")
        return

    if len(args) != 4:
        print("len(args) != 4")
    
    rclpy.init()
    ttac3_action_client = TTAC3ActionClient()
    ttac3_action_client.send_goal([int(n) for n in args[1:]])
    rclpy.spin(ttac3_action_client)

if __name__ == '__main__':
    main()