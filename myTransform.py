#!/usr/bin/python3
import csv
import json
import socket
import sys

# constructor. objeto de formato.

# Create socket. metodo del client UDP.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# método del objeto de Transform
class myTransform :
	def __init__(self, input):
		super().__init__()  #myTransform.__init__(self)
		self.input = input 
		self.output = []

	def csv2json(self):
		with open(self.input) as f:
			records = csv.DictReader(f)
			for row in records:
				try:
					print(row)
					self.output.append(row)
				except Exception as e:
					print("error")

		self.output = json.dumps(self.output)
		return self.output

