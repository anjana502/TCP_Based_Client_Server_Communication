import socket
import threading

def message_client(client_socket):
    while (True):
        data = client_socket.recv(1024)

        if (data == None):
            break
        
        message = data.decode("utf-8")

        print(f"Recieved message: {message}")

        response = f"Server received your message: {message}"
        client_socket.sendall(response.encode("utf-8"))
    
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listerning on {host}:{port}")

    while (True):
        client_socket, client_address = server_socket.accept()

        print(f"Accepted connection from{client_address}")

        client_handler = threading.Thread(target = message_client, args = (client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()