import Server_Class
from Server_Class import Server
from Server_Class import Client
import socket

host = socket.gethostname()                           
port = 9999
msg = 'Thank you for connecting'+ "\r\n"

server = Server(socket.socket(socket.AF_INET, socket.SOCK_STREAM) , ("10.195.6.47", 9999))
client = Client(socket.socket(socket.AF_INET, socket.SOCK_STREAM) , (socket.gethostname(), 9999), 'Thank you for connecting'+ "\r\n")

serversocket = getattr(server, "serversocket")
localmachine = getattr(server, "localmachine")

serversocket.bind(localmachine)
serversocket.listen(5)

server.server_run(serversocket, localmachine)
client.client_run(socket.socket(socket.AF_INET, socket.SOCK_STREAM), (socket.gethostname(), 9999), 'Thank you for connecting'+ "\r\n")

# server = Server_Class.server_run("serversocket", "localmachine")
# client = Server_Class.client_run("serversocket", "localmachine", "msg")

