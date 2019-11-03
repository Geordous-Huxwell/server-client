import socket
# import time


# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
#host = socket.gethostname()
host = "localhost" #127.0.0.1" #"localhost" #or 127.0.0.1                           

port = 9999

print(serversocket)                                           

# serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# bind to the port
serversocket.bind((host, port)) 
'''
-can be blocked by firewall, network, etc.                                 
-note that one argument, a tuple, is being passed, not two arguments
'''
print(type(serversocket))
# queue up to 5 requests
serversocket.listen(5)
'''
-max number of clients that can be waiting for response before requests get rejected                                           
'''

while True:
# i=0
# while i != 10:
# 	i+=1
# 	time.sleep(1)
   # establish a connection
	
	clientsocket,addr = serversocket.accept()      
	print(addr)
	'''
	- if no connection is established, you will have an orphaned task 
	that must be cancelled manually or ended in task manager
	'''
	print("Got a connection from %s" % str(addr))
    
	msg = 'Thank you for connecting'+ "\r\n"
	clientsocket.send(msg.encode('ascii'))
	clientsocket.close()
