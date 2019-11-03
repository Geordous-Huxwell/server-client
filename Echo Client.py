import socket

class EchoClient(socket.socket):
	'''
	'''
	def __init__(self, host = "127.0.0.1", port = 9999):
		super().__init__(socket.AF_INET, socket.SOCK_STREAM)
		self.host = host
		self.port = port

	def connectToServer(self):
		self.connect((self.host,self.port))

	def sendText(self, text):
		self.send(text.encode("ascii"))

	def receiveText(self):
		return self.recv(1024).decode("ascii")

	def Echo(self, text):
		self.sendText(text)
		return self.receiveText()

	def closeConnection(self):
		self.close()

if __name__ == "__main__":
	myClient = EchoClient()
	myClient.connectToServer()
	response = myClient.Echo("hello my name isn't jordan")
	myClient.closeConnection()
	print(response)