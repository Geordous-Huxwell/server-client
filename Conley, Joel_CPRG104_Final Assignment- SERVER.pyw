from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import Frame
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


class serverFrontend(Tk):
	'''
	Server User Interface
	Updated by Joel Conley
	June 18, 2019
	'''
	class GUI_object(Tk):

		def specs(obj, _type_, text, font, state, row, rowspan, col, colspan, padx, pady, ipadx, ipady, sticky):
			obj.type = _type_
			obj.text = text
			obj.font = font
			obj.state = state
			obj.row = row
			obj.rowspan = rowspan
			obj.col = col
			obj.colspan = colspan
			obj.padx = padx
			obj.pady = pady
			obj.ipadx = ipadx
			obj.ipady = ipady
			obj.sticky = sticky


			if obj.type == "Button":
				class_button = Button(obj,  command=serverBackend().start, text=obj.text, font=obj.font, width=6, state=obj.state, background="ivory3").grid(row=obj.row, rowspan=obj.rowspan, column = obj.col, columnspan=obj.colspan, padx=obj.padx, pady=obj.pady, ipadx=obj.ipadx, ipady=obj.ipady, sticky=obj.sticky)
			
			if obj.type == "Label":
				class_label = Label(obj,  text=obj.text, font=("Arial",11,),width=14, state=obj.state, background="grey21", foreground="ivory3").grid(row=obj.row, rowspan=obj.rowspan, column=obj.col, columnspan=obj.colspan, padx=obj.padx, pady=obj.pady, ipadx=obj.ipadx, ipady=obj.ipady, sticky=obj.sticky)

			if obj.type == "Display":
				class_display = Entry(obj,  text=obj.text, font=("Arial",9), width=20, state=obj.state, background="grey23", foreground="DeepSkyBlue2").grid(row=obj.row, rowspan=obj.rowspan, column=obj.col, columnspan=obj.colspan, padx=obj.padx, pady=obj.pady, ipadx=obj.ipadx, ipady=obj.ipady, sticky=obj.sticky)

	def __init__(UI):
		super().__init__()
		# frame = Frame(master)
		
		UI.title("Server")
		UI.geometry("150x400+300+100")		# width x height + horizontal position + vertical position
		UI.resizable(width=False, height=False)		# disable user from resizing window
		UI.configure(background="grey21")
		UI.font = font.Font(family="Times", size=22, weight="bold")
		
		background = "grey21"
		rowspan = 1
		colspan = 1
		px = 2
		py = 2
		ipx = 2
		ipy = 2

		UI.btn_start = UI.GUI_object.specs(UI, "Button", "Start", UI.font, "normal", 0, rowspan, 0, colspan, px, py, ipx, ipy, "")
		

		UI.lbl_msg_rcv = UI.GUI_object.specs(UI, "Label", "Message Received:", UI.font, "normal", 1, rowspan, 0, colspan, px, py, ipx, ipy, "N")

		
		UI.input_display = UI.GUI_object.specs(UI, "Display", "", UI.font, "normal", 2, rowspan+4, 0, colspan, px, py, ipx, ipy, "NESW")
		

		UI.lbl_msg_rcv = UI.GUI_object.specs(UI, "Label", "Detail Log:", UI.font, "normal", 7, rowspan, 0, colspan, px, py, ipx, ipy, "NESW")

		
		UI.input_log = UI.GUI_object.specs(UI, "Display", "", UI.font, "disabled", 8, rowspan+4, 0, colspan, px, py, ipx, ipy, "NESW")

		
		# UI.btn_stop = UI.GUI_object.specs(UI, "Button", "Stop", UI.font, "normal", 13, rowspan, 0, colspan+1, px-2, py-2, ipx, ipy, "N")


		UI.grid_rowconfigure(0, weight = 1)
		# UI.grid_rowconfigure(1, weight = 1)
		UI.grid_rowconfigure(2, weight = 1)
		UI.grid_rowconfigure(3, weight = 1)
		UI.grid_rowconfigure(4, weight = 1)
		UI.grid_rowconfigure(5, weight = 1)
		UI.grid_rowconfigure(8, weight = 1)

		UI.grid_columnconfigure(0, weight=1)
		UI.grid_columnconfigure(1, weight=1)
		UI.grid_columnconfigure(2, weight=1)
		UI.grid_columnconfigure(3, weight=1)
		UI.grid_columnconfigure(4, weight=1)
		UI.grid_columnconfigure(5, weight=1)
		UI.grid_columnconfigure(6, weight=1)
		UI.grid_columnconfigure(7, weight=1)
		UI.grid_columnconfigure(8, weight=1)


		

		# UI.mainloop()



class serverBackend(socket):
	'''

	'''
	def __init__(server, host="localhost", port=9999):
		super().__init__(AF_INET, SOCK_STREAM)

		server.host = host
		server.port = port
		server.running = False
		server.bind((server.host, server.port))	#tells OS that a program wants to listen for network traffic on given port
		server.listen(5)		#queue up to 5 requests

	def sendText(server, text):
		return None


	def recvText(server):
		return server.clientsocket.recv(1024).decode("ascii")

	def start(server):
		server.running = True
		server.run()


	def run(server):
		while(server.running):
			print("waiting for connection...")
			server.clientsocket,addr = server.accept()
			print("Connection received from", str(addr))
			text = server.receiveText()
			text = text.title()
			server.send_msg(text)
			server.clientsocket.close()


		

	# def serverGUI():
	# 	# messagebox.showinfo("Title","Hello, World!")

		
	# 	obj_1 = Button(root,text = "1")
	# 	obj_1.grid(row = 0, column = 0,padx = 0,pady = 0,ipadx = 0,ipady = 0)

	# 	obj_2 = Button(root,text = "2")
	# 	obj_2.grid(row = 0, column = 1)

	# 	obj_3 = Button(root,text = "3")
	# 	obj_3.grid(row = 0, column = 2)

	# 	obj_4 = Button(root,text = "4")
	# 	obj_4.grid(row = 1, column = 0)

	# 	obj_5 = Button(root,text = "5")
	# 	obj_5.grid(row = 1, column = 1)

	# 	obj_6 = Button(root,text = "6")
	# 	obj_6.grid(row = 1, column = 2)

	# 	obj_7 = Button(root,text = "7")
	# 	obj_7.grid(row = 2, column = 0)

	# 	obj_8 = Button(root,text = "8")
	# 	obj_8.grid(row = 2, column = 1)

	# 	obj_9 = Button(root,text = "9")
	# 	obj_9.grid(row = 2, column = 2)

	# 	obj_enter = Button(root, text = "This is the enter button",command = enterButtonAction)
	# 	obj_enter.grid(row = 0,column = 3,rowspan = 3,sticky = "NS")


if __name__ == '__main__':
	# root = Tk()
	serverFrontend()
	mainloop()
	# server = serverBackend()
	# server.start()

# class serverBackend(Threading):



# class clientFrontend(Tk):



# class clientBackend():

