import socket

class EchoServer(socket.socket):
	'''

	'''
	def __init__(self, host="127.0.0.1", port=9999):
		super().__init__(socket.AF_INET, socket.SOCK_STREAM)

		self.host = host
		self.port = port
		self.running = False
		self.bind((self.host, self.port))	#tells OS that a program wants to listen for network traffic on given port
		self.listen(5)		#queue up to 5 requests

	def sendText(self, text):
		return None


	def receiveText(self):
		return self.clientsocket.recv(1024).decode("ascii")

	def start(self):
		self.running = True
		self.run()


	def run(self):
		while(self.running):
			print("waiting for connection...")
			self.clientsocket,addr = self.accept()
			print("Connection received from", str(addr))
			text = self.receiveText()
			text = text.title()
			self.sendText(text)
			clientsocket.close()


if __name__ == '__main__':
	myServer = EchoServer()
	myServer.start()

