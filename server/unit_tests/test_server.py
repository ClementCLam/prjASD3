
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from server import handle_client

import unittest
#from server.server import handle_client
from unittest.mock import MagicMock, patch, call
import io

class TestServer(unittest.TestCase):
    def test_handle_client(self):
        # Mocking client_socket object
        client_socket = MagicMock()
        
        # Mocking user input
        inputs = ['explore client1 /path/to/explore', 'quit']
        sys.stdin = io.StringIO('\n'.join(inputs))

        # Mocking client_socket.recv() to return specific byte responses
        client_socket.recv.side_effect = [
            b'Response 1\n',
            b'Response 2\n'
        ]

        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                handle_client(client_socket)

        # Assert that the client_socket.send() methods were called as expected
        expected_send_calls = [
            call.send(b'explore client1 /path/to/explore'),
            call.send(b'quit')
        ]
        client_socket.send.assert_has_calls(expected_send_calls)

        # Assert that the expected outputs were printed to stdout
        expected_output = "Response 1\nResponse 2\n"
        actual_output = fake_stdout.getvalue()

        # Remove newline characters for comparison
        expected_output_stripped = expected_output.replace('\n', '')
        actual_output_stripped = actual_output.replace('\n', '')
        
        print(f"expected output: {expected_output_stripped}")
        print(f"actual output: {actual_output_stripped}")
        self.assertEqual(actual_output_stripped, expected_output_stripped)

        # Assert that the client_socket.close() was called
        client_socket.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()