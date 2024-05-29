import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(message)
            else:
                break
        except:
            print("[ERROR] An error occurred!")
            client_socket.close()
            break

def send_messages():
    while True:
        message = input()
        try:
            client_socket.send(message.encode("utf-8"))
        except:
            print("[ERROR] Unable to send message!")
            client_socket.close()
            break

# Define server address and port
HOST = '127.0.0.1'
PORT = 5556  # Ensure this matches the server's port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Start threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
