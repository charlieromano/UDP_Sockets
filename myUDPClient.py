#!/usr/bin/python3
import socket
import sys

class myUDPClient:

    def __init__(self, ip, port):
        super().__init__()
        self.ip = ip
        self.port=port
        self.server_address=(self.ip, self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    
    def sendto(self,data):
    	self.sock.sendto(data.encode(), self.server_address)
    	#self.response = self.sock.recvfrom(128*1024)

#from myUDPClient import myUDPClient
#ip = "127.0.0.1"
#port = 10000
#x = myUDPClient(ip, port)
#x.sendto("hola")


