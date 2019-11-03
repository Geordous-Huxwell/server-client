import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import Frame
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

class clientBackend(socket, Thread):
		'''
		'''
		def __init__(client, host = "127.0.0.1", port = 9999):
			super().__init__(AF_INET, SOCK_STREAM)
			client.host = host
			client.port = port

			
		def receive():
			msg = client.recv(1024).decode("ascii")

			receive_thread = Thread(target=receive)
			receive_thread.start()


		def send_msg(client, event=None):
			# msg = clientFrontend.GUI_object.class_display.get()
			# msg.set("Thanks!")
			msg = "fuck"
			client_socket = socket(AF_INET, SOCK_STREAM)
			client_socket.connect((client.host,client.port))
			receive_thread = Thread(target=clientBackend.receive)
			receive_thread.start()
			client.msg = msg
			print(client.msg)
			client.msg = client.msg.encode("utf-8")
			client_socket.send(client.msg)

			# client.sendall(client.msg).encode('utf-8')


		def connectToServer(client):
			client.connect((client.host,client.port))
		

		def Echo(client, text):
			client.send_msg(text)
			return client.receiveText()

		def closeConnection(client):
			client.close()




class clientFrontend(Tk):
	'''
	Client User Interface
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
				class_button = Button(obj,  text=obj.text, font=obj.font, width=6, state=obj.state, background="ivory3", command=clientBackend().send_msg).grid(row=obj.row, rowspan=obj.rowspan, column = obj.col, columnspan=obj.colspan, padx=obj.padx, pady=obj.pady, ipadx=obj.ipadx, ipady=obj.ipady, sticky=obj.sticky)
				return obj

			if obj.type == "Label":
				class_label = Label(obj,  text=obj.text, font=("Arial",11,),width=14, state=obj.state, background="grey21", foreground="ivory3").grid(row=obj.row, rowspan=obj.rowspan, column=obj.col, columnspan=obj.colspan, padx=obj.padx, pady=obj.pady, ipadx=obj.ipadx, ipady=obj.ipady, sticky=obj.sticky)
				return obj

			if obj.type == "Display":
				class_display = Entry(obj,  textvariable=obj.text, font=("Arial",9), width=20, state=obj.state, background="grey23", foreground="DeepSkyBlue2").grid(row=obj.row, rowspan=obj.rowspan, column=obj.col, columnspan=obj.colspan, padx=obj.padx, pady=obj.pady, ipadx=obj.ipadx, ipady=obj.ipady, sticky=obj.sticky)
				msg = obj.text
				print(msg)
				clientBackend().send_msg(msg)
				return 
			# msg = class_display.get()
			# print(msg)
				# class_display.bind("<Return>", clientBackend.send())


	def __init__(UI):
		super().__init__()

		msg = tkinter.StringVar(UI)
		msg.set("1")

		# def btn_action():
		# 	msg = UI.input_display.get()
		# 	client.sendText(msg)
		
		UI.title("Client")
		UI.geometry("300x300+300+100")		# width x height + horizontal position + vertical position
		UI.resizable(width=False, height=False)		# disable user from resizing window
		UI.configure(background="grey21")
		UI.font = font.Font(family="Times", size=12, weight="bold")
		
		background = "grey21"
		rowspan = 1
		colspan = 1
		px = 2
		py = 2
		ipx = 2
		ipy = 2


		UI.lbl_IP = UI.GUI_object.specs(UI, "Label", "IP Address:", UI.font, "normal", 0, rowspan, 0, colspan, px, py, ipx, ipy, "NESW")


		UI.input_IP = UI.GUI_object.specs(UI, "Display", "127.0.0.1", UI.font, "normal", 0, rowspan, 1, colspan, px, py, ipx, ipy, "NESW")


		UI.lbl_port = UI.GUI_object.specs(UI, "Label", "Port Number:", UI.font, "normal", 1, rowspan, 0, colspan, px, py, ipx, ipy, "NESW")


		UI.input_port = UI.GUI_object.specs(UI, "Display", "9999", UI.font, "normal", 1, rowspan, 1, colspan, px, py, ipx, ipy, "NESW")


		UI.lbl_msg = UI.GUI_object.specs(UI, "Label", "Message:", UI.font, "normal", 2, rowspan, 0, colspan, px, py, ipx, ipy, "N")


		UI.input_display = UI.GUI_object.specs(UI, "Display", msg, UI.font, "normal", 2, rowspan, 1, colspan, px, py, ipx, ipy, "NESW")


		UI.btn_send = UI.GUI_object.specs(UI, "Button", "Send", UI.font, "normal", 3, rowspan, 1, colspan, px, py, ipx, ipy, "NE")
		

		UI.lbl_rsp = UI.GUI_object.specs(UI, "Label", "Response:", UI.font, "normal", 4, rowspan, 0, colspan, px, py, ipx, ipy, "N")


		UI.log_display = UI.GUI_object.specs(UI, "Display", "", UI.font, "normal", 4, rowspan, 1, colspan, px, py, ipx, ipy, "NESW")

		# msg = UI.input_display.get()
		
		# UI.grid_rowconfigure(0, weight = 1)
		# UI.grid_rowconfigure(1, weight = 1)
		# UI.grid_rowconfigure(2, weight = 1)
		UI.grid_rowconfigure(3, weight = 1)
		# UI.grid_rowconfigure(4, weight = 1)
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




		UI.mainloop()

	

	


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
	clientFrontend()
	client = clientBackend()
	client.connectToServer()
	response = client.Echo("hello my name isn't jordan")
	client.closeConnection()
	print(response)

# class serverBackend(Threading):



# class clientFrontend(Tk):



# class clientBackend():

