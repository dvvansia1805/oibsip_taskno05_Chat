import socket
import threading

# List to keep track of connected clients
clients = []

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    connected = True
    while connected:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(f"[{client_address}] {message}")
                broadcast(message, client_socket)
            else:
                connected = False
        except:
            connected = False
            break
    
    print(f"[DISCONNECTED] {client_address} disconnected.")
    clients.remove(client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except:
                client.close()
                clients.remove(client)

def start_server():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

# Define server address and port
HOST = '127.0.0.1'
PORT = 5556  # Ensure this matches the client's port
SERVER = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER)

print("[STARTING] Server is starting...")
start_server()
