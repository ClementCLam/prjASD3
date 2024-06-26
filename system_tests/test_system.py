import socket
import json
import os
import time
import pytest

# Load server and client configurations
def load_server_config():
    config_path = os.path.join(os.path.dirname(__file__), 'server/server_config.json')
    with open(config_path) as config_json:
        config = json.load(config_json)
    return config

def load_client_config():
    config_path = os.path.join(os.path.dirname(__file__), 'client/client_config.json')
    with open(config_path) as config_json:
        config = json.load(config_json)
    return config

@pytest.fixture(scope='module')
def server():
    config = load_server_config()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((config['host'], config['port']))
    server_socket.listen(5)
    yield server_socket
    server_socket.close()

@pytest.fixture(scope='module')
def client():
    config = load_client_config()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((config['server_host'], config['server_port']))
    yield client_socket
    client_socket.close()

def test_explore_existing_directory(client):
    command = 'explore 1 /path/to/existing/directory'
    client.send(command.encode())
    response = client.recv(4096).decode()
    assert 'Directory is empty.' not in response
    assert 'Error:' not in response

def test_explore_non_existing_directory(client):
    command = 'explore 1 /path/to/non/existing/directory'
    client.send(command.encode())
    response = client.recv(4096).decode()
    assert 'Error: Directory' in response
    