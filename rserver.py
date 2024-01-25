#!/usr/bin/env python3
import socket
import threading

SERVER, PORT = socket.gethostbyname(socket.gethostname()), 6379

rserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rserver.bind((SERVER, PORT))
rserver.listen()

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")

    req_msg = client_socket.recv(1024).decode('utf-8')
    if 'PING' in req_msg:
        resp_msg = "+PONG\r\n"
    elif req_msg[0] == "*":
        print("Requested Message is array")
        print(f"Requested message has :{req_msg[1]} string,")
        if 'ECHO' in req_msg:
            resp_msg = req_msg.replace('\r\n', '').replace('ECHO', '', 1)
            resp_msg = ''.join(char for char in req_msg if not (char.isdigit() or char in '{}$*'))
    #count_ping = req_msg.count('PING')
    #resp_msg = count_ping * resp_msg
    client_socket.send(resp_msg.encode('utf-8'))

    print(f"Connection from {client_address} closed")
    client_socket.close()

def main():
    print(f"Server listening on {SERVER}:{PORT}")

    while True:
        client_socket, client_address = rserver.accept()

        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == '__main__':
    main()

