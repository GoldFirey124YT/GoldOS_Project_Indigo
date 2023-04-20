import socket

HOST =  #Edit with Local IP
PORT =  #Edit with Desired Port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

while True:
    conn, addr = server_socket.accept()
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
    conn.close()
