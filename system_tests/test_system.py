import socket
import json
import os
import time
import unittest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Load server and client configurations
def load_server_config():
    config_path = os.path.join(os.path.dirname(__file__), '../server/server_config.json')
    with open(config_path) as config_json:
        config = json.load(config_json)
    return config

def load_client_config():
    config_path = os.path.join(os.path.dirname(__file__), '../client/client_config.json')
    with open(config_path) as config_json:
        config = json.load(config_json)
    return config

class SystemTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server_config = load_server_config()
        cls.client_config = load_client_config()

        # Setup server
        cls.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.server_socket.bind((cls.server_config['host'], cls.server_config['port']))
        cls.server_socket.listen(5)

        # Setup client
        cls.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.client_socket.connect((cls.client_config['server_host'], cls.client_config['server_port']))

    @classmethod
    def tearDownClass(cls):
        cls.server_socket.close()
        cls.client_socket.close()

    def test_explore_existing_directory(self):
        logging.info("Starting test: explore_existing_directory")
        command = 'explore 1 /path/to/existing/directory'
        self.client_socket.send(command.encode())
        response = self.client_socket.recv(4096).decode()
        logging.info("Received response: %s", response)
        self.assertNotIn('Directory is empty.', response)
        self.assertNotIn('Error:', response)
        logging.info("Completed test: explore_existing_directory")

    def test_explore_non_existing_directory(self):
        logging.info("Starting test: explore_non_existing_directory")
        command = 'explore 1 /path/to/non/existing/directory'
        self.client_socket.send(command.encode())
        response = self.client_socket.recv(4096).decode()
        logging.info("Received response: %s", response)
        self.assertIn('Error: Directory', response)
        logging.info("Completed test: explore_non_existing_directory")

if __name__ == '__main__':
    unittest.main()