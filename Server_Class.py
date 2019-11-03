import socket

class Server():
	"""docstring for Server"""
	def __init__(self, serversocket, localmachine):
		self.serversocket = serversocket
		self.localmachine = localmachine

	def server_run(self, serversocket, localmachine):
		# print(self.serversocket)
		# self.serversocket.bind(self.localmachine)
		# print(self.serversocket)

		while True:
			clientsocket,addr = self.serversocket.accept()
			print("Got a connection from %s" % str(addr))
		    
			clientsocket.send(msg.encode('ascii'))
			clientsocket.close()

class Client():
	"""docstring for Client"""
	def __init__(self, clientsocket, localmachine, msg):
		self.clientsocket = clientsocket
		self.localmachine = localmachine
		self.msg = msg


	def client_run(self, clientsocket, localmachine, msg):
		s = self.clientsocket
		
		s.connect(self.localmachine) 

		self.msg = s.recv(1024)                                     
	
		s.close()

		print (msg.decode('ascii'))

			