#!/usr/bin/env python3
import socket

SERVER , PORT = socket.gethostbyname(socket.gethostname()) , 6379

if __name__ == '__main__':
    rserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    rserver.bind((SERVER,PORT))
    rserver.listen()