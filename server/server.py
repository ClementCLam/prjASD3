import socket
import threading
import json
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'server_config.json')
    with open(config_path) as config_json:
        config = json.load(config_json)
    return config

def handle_client(client_socket):
    # Handle incoming connections from clients
    try:
        while True:
            command = input("Enter command (e.g., 'explore <client_id> <path>'): ")
            client_socket.send(command.encode())
            response = client_socket.recv(4096).decode()
            print(response)
            
    except StopIteration:
        pass # only happen in unittest scenario 
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close() 
       

"""     except Exception as e:
        pass # print(f"Error: {e}")
    finally:
        client_socket.close()
 """

def main():
    config = load_config()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((config['host'], config['port']))
    server_socket.listen(5)
    print("\n[+] Listening for connections...")

    try:
        while True:
            client_socket, _ = server_socket.accept()
            print(f"[+] Accepted connection from {client_socket.getpeername()}")
            handle_client(client_socket)    
            #client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            #client_handler.start()
    except KeyboardInterrupt:
        print("[!] Server shutting down...")

if __name__ == "__main__":
    main()
