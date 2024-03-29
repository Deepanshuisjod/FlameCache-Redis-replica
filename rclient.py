#!/usr/bin/env python3
import socket

SERVER_IP, SERVER_PORT = socket.gethostbyname(socket.gethostname()), 6379

rclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    rclient.connect((SERVER_IP, SERVER_PORT))

    ping_msg = "*2\r\n$4\r\nECHO\r\n$3\r\nhey\r\n"
    ping_msg = "GET\r\nage\r\n"  
    rclient.send(ping_msg.encode('utf-8'))

    resp_msg = rclient.recv(1024).decode('utf-8') 
    print(resp_msg)

    rclient.close()

if __name__ == "__main__":
    main()
