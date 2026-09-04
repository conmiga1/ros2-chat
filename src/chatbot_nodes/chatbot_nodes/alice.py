import rclpy
from rclpy.node import Node
from chatbot_interfaces.srv import Chatbot

class Alice(Node):
    def __init__(self):
        super().__init__('alice')
        self.cli = self.create_client(Chatbot, 'chatbot')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for Bob...')

    def send_request(self, sentence):
        req = Chatbot.Request()
        req.sentence = sentence
        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main():
    rclpy.init()
    alice = Alice()
    lines = [
        "Hi, Bob.",
        "Did you just arrive here?",
        "How do you like it?",
        "It really is very busy. I moved here from Tokyo 5 years ago and I still have trouble sometimes. Did you move here with your wife?",
        "Oh, I see.",
        "Yes, I am married and I have two children.",
        "6 and 8 years old",
    ]

    for line in lines:
        print(f'A: {line}')
        result = alice.send_request(line)
        print(f'B: {result.sentence}')

    alice.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
