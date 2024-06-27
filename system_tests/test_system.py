import socket
import time
import unittest
import logging
import subprocess

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='system_test.log', filemode='w')

class SystemTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Start the server process
        logging.info("Start server process")        
        cls.server_process = subprocess.Popen(['python3', 'server/server.py'])
        time.sleep(5)  # Give the server time to start

        # Start the client process
        logging.info("Start client process") 
        cls.client_process = subprocess.Popen(['python3', 'client/client.py'])
        time.sleep(5)  # Give the client time to connect to the server

        # Setup client socket for sending commands
        # The host and port should match what is in the server_config.json
        logging.info("Setup client socket") 
        cls.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.client_socket.connect(('localhost', 9999))  # Change this if the config uses different host and port

    @classmethod
    def tearDownClass(cls):
        logging.info("enter tearDownClass") 
        cls.client_socket.close()
        cls.client_process.terminate()
        cls.client_process.wait()
        cls.server_process.terminate()
        cls.server_process.wait()

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