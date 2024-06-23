import socket
import os
import hashlib
import json
import datetime


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'client_config.json')
    with open(config_path) as config_json:
        config = json.load(config_json)
    return config

def get_directory_info(path):
    # error handling
    if not os.path.exists(path):
        return f"Error: Directory '{path}' does not exist."
    if not os.path.isdir(path):
        return f"Error: '{path}' is not a directory."

    info = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            dir_stat = os.stat(item_path)
            modification_time = datetime.datetime.fromtimestamp(dir_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            num_items = len(os.listdir(item_path))
            info.append(f"{item} (Dir) - {num_items} items, Modification Time: {modification_time}")
        else:
            file_stat = os.stat(item_path)
            modification_time = datetime.datetime.fromtimestamp(file_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            with open(item_path, 'rb') as f:
                content = f.read()
                hash_value = hashlib.sha256(content).hexdigest()
            info.append(f"{item} - SHA256: {hash_value}, Modification Time: {modification_time}")

    # error handling
    if not info:
        return "Directory is empty."            
    return '\n'.join(info)

def main():
    config = load_config()
    server_host = config['server_host']
    server_port = config['server_port']

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((server_host, server_port))

    try:
        while True:
            command = client_socket.recv(4096).decode()
            if command.startswith('explore'):
                _, _, path = command.split(' ', 2)
                response = get_directory_info(path)
                client_socket.send(response.encode())
    except KeyboardInterrupt:
        print("[!] Client shutting down...")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()

