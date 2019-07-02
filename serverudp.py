#!usr/bin/python
import socket

#Creating server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Define host and port
udp_host = '127.0.0.1'
udp_port = 12345

#Bind the server socket to the host
s.bind((udp_host, udp_port))

while True:
    print('Waiting for client')

    #Accept the connection from a client
    data, addr = s.recvfrom(1024)
    print('Received data from: ',addr)

    print('Data received:', data)


