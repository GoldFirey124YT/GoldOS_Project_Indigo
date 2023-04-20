import socket

HOST = #Enter Local IP of Server
PORT = #Enter Chosen Port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = input("Enter message: ")
client_socket.sendall(message.encode())
data = client_socket.recv(1024)
client_socket.close()
print('Received', repr(data))
