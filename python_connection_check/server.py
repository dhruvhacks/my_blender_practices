"""
Python SERVER side script to check active clients and detect connection break
implemented via socket module

What it Does??
Sends a test data of 5 bytes every 5 seconds via a socket to client and if acknowledged, it remains connected.
If a exception is raised (connection lost/broken), connection is closed and detected.
Multiple clients are assigned separate Threads and main thread is left to listen to new connections.

Language- Python 2.7
"""

import socket			#to implement socket 
import time				#for required delay of 5 seconds
import threading		#for connecting multiple clients.


"""
Class 'connection' to manage the connections.
"""
class connection(object):
	"""initiates socket port at server-end"""
	def __init__(self, sock = None, host = "", port = 0000, addr 	= ""):
		if(sock==None):
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.host = socket.gethostname()
			self.port = 8081	#can be changed
		else:
			self.sock = sock

	def port_bind(self):									#binds the port and host.
		self.sock.bind((self.host,self.port))

	def connect(self):										#main function that establishes connection to different clients
		self.sock.listen(5)
		while True:
			c,addr = self.sock.accept()						#accept connections from client
			threading.Thread(target = self.check,args=(c,addr)).start()	#seperate thread created for new clients.

	def check(self,client,address):
		while True:
			try:
				time.sleep(5)								#send "done!" string every 5 seconds
				client.send("done!")

				""" HERE PLEASE ADD THE VARIABLES AND DATA REQUIRED TO BE STORED IN A CONNECTED SESSION """

			except socket.error:
		#		print("Connection broken with ",address)	#test line to check lost clients
				client.close()
				return False
		#	print("Connected to- ",address)		#test line to check connected clients


"""main function"""
def main():
	client = connection()	#initiate a socket
	client.port_bind()		#bind the server's port
	client.connect()		#Establish and check the connection


if __name__ == '__main__':
	main()
