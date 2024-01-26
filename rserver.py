#!/usr/bin/env python3
import socket
import threading
reddis_database = {}
SERVER, PORT = socket.gethostbyname(socket.gethostname()), 6379

rserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rserver.bind((SERVER, PORT))
rserver.listen()

# Responding to ping
def resp_to_ping(req_msg):
    count_ping = req_msg.count('PING')
    resp_msg = count_ping * req_msg
    return resp_msg

# Responding to array(*) type commands
def resp_to_array(req_msg):
    if 'ECHO' in req_msg:
        resp_msg = req_msg.split("\r\n")      
        return resp_msg[4]

# Responding to set command
def resp_to_set(req_msg):
    split_req_msg = req_msg.split("\r\n")
    reddis_database[split_req_msg[1]] = split_req_msg[2]
    
# Responding to get command    
def resp_to_get(req_msg):
    split_req_msg = req_msg.split("\r\n")
    if split_req_msg[1] in reddis_database:
        return reddis_database[split_req_msg[1]]
    else:
        return "DNE"
    
def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")

    req_msg = client_socket.recv(1024).decode('utf-8')
    req_msg_lower = req_msg.lower() 

    if 'ping' in req_msg_lower:
        resp_msg = resp_to_ping(req_msg)
    elif req_msg_lower.startswith("*"):
        resp_msg = resp_to_array(req_msg)
    elif 'set' in req_msg_lower:
        resp_to_set(req_msg)
        resp_msg = "OK"
    elif 'get' in req_msg_lower:
        resp_msg = resp_to_get(req_msg)
    else:
        resp_msg = "Unknown command"

    client_socket.send(resp_msg.encode('utf-8'))
    print(f"Connection from {client_address}")
    client_socket.close()

def main():
    print(f"Server listening on {SERVER}:{PORT}")

    while True:
        client_socket, client_address = rserver.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == '__main__':
    main()

