#!usr/bin/python
import socket

# Creating a clien
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get client host and port
host = '127.0.0.1'
port = 12345
msg = "Hello this is your client!"

sock.connect((host, port))
sock.sendto(msg.encode('utf-8'), (host, port))
