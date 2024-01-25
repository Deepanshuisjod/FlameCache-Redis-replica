#!/usr/bin/env python3
import socket

SERVER, PORT = socket.gethostbyname(socket.gethostname()), 6379

rserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rserver.bind((SERVER, PORT))
rserver.listen()

def main():
    print(f"Server listening on {SERVER}:{PORT}")

    while True:
        client_socket, client_address = rserver.accept()
        print(f"Connection from {client_address}")

        req_msg = client_socket.recv(1024).decode('utf-8')
        resp_msg = "+PONG\r\n"

        if req_msg == 'PING\r\n':
            client_socket.send(resp_msg.encode('utf-8'))
        else:
            print(f"Received unknown message: {req_msg}")

        client_socket.close()

if __name__ == '__main__':
    main()
