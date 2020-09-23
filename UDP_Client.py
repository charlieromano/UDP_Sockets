#!/usr/bin/python3
import csv
import json
import socket
import sys

# constructor. objeto de formato.
filein = 'csv_test.csv'

# constructor. metodo del client UDP
ip = "127.0.0.1"
port = 10000
server_address = (ip, port)

# Create socket. metodo del client UDP.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# método del objeto de formato
y = []
with open(filein) as f:
    records = csv.DictReader(f)
    for row in records:
        try:
            print(row)
            y.append(row)
        except Exception as e:
            print("error")

message = json.dumps(y)

# Send datagram. metodo del client UDP.
request = sock.sendto(message.encode(), server_address)
response = sock.recvfrom(128*1024)

print(response)



