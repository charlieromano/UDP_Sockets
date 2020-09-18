#!/usr/bin/python3
import csv
import json
import socket
import sys

ip = "127.0.0.1"
port = 10000

server_address = (ip, port)

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

filein = '../csv_test.csv'

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

# Send datagram
request = sock.sendto(message.encode('utf-8'), server_address)
response = sock.recvfrom(128*1024)

print(response)
