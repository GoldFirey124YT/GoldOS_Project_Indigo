import socket

HOST = '0.0.0.0'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []

def broadcast_message(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.sendall(message.encode())
            except:
                clients.remove(client)

while True:
    conn, addr = server_socket.accept()
    clients.append(conn)
    print(f"New client connected: {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = f"{addr}: {data.decode()}"
        print(message)
        broadcast_message(message, conn)

    conn.close()
    print(f"Client disconnected: {addr}")
