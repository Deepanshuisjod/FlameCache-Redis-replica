import socket
import asyncio

async def rclient1(server_ip,server_port):
    rclient1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rclient1.connect((server_ip, server_port))

    ping_msg_bycl = "PING"
    rclient1.send(ping_msg_bycl.encode('utf-8'))
    response1 = rclient1.recv(1024).decode('utf-8')
    return response1

async def rclient2(server_ip,server_port):
    rclient2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rclient2.connect((server_ip, server_port))

    pint_msg_byc2 = "PING"
    rclient2.send(pint_msg_byc2.encode('utf-8'))
    response2 = rclient2.recv(1024).decode('utf-8')
    return response2

async def main():
    server_ip = socket.gethostbyname(socket.gethostname())
    server_port = 6379

    batch = asyncio.gather(rclient1(server_ip,server_port),rclient2(server_ip,server_port))
    response_client1 , response_client2 = await batch

    print(f"Response from client 1 : {response_client1}")
    print(f"Response from client 2 : {response_client2}")
if __name__ == '__main__':
    asyncio.run(main())
