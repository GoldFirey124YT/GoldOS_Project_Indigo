import socket

HOST = 'localhost'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Enter message: ")
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print('Received', repr(data.decode()))
