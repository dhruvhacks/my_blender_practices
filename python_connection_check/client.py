"""
simple python client

Language- Python 2.7
"""

import socket		#to implemet socket connection

s = socket.socket()			#socket created
host = socket.gethostname()	#host selected
port = 8081					#same port no. as server
s.connect((host,port))		#connected to server via accept() at server

while(1):
	#print("I am client 1")	#sample statement to test if client is connected	
	print(s.recv(5))		#receve string "done!" from server
	"""PLEASE ADD VARIABLES(data) NEEDED TO BE SENT TO SERVER OF THIS CLIENT"""