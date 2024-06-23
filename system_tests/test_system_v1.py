import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import subprocess
import socket
import time
import threading

class TestClientServerInteraction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_process = subprocess.Popen(["python", "server/server.py"])
        time.sleep(1)  # Give the server some time to start

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()
        cls.server_process.wait()

    def test_client_server_interaction(self):
        client_process = subprocess.Popen(["python", "client/client.py"], 
                                          stdin=subprocess.PIPE, 
                                          stdout=subprocess.PIPE, 
                                          stderr=subprocess.PIPE,
                                          text=True
        )
        #client_process = subprocess.Popen(["python", "client/client.py"])

        # Connect to the server to simulate client sending commands
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("127.0.0.1", 9999))
            s.sendall(b"explore 172.18.0.3 .\n")
            response = s.recv(4096).decode()
            print('response: ',response)
            print('length of response: ',len(response))

        client_process.terminate()
        client_process.wait()

        #self.assertIn("SHA256", response)
        #self.assertIn("Modification Time", response)

        self.assertFalse("Modification Time" in response)

    

if __name__ == "__main__":
    unittest.main()
    