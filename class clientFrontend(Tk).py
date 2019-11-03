from tkinter import *
from tkinter import messagebox
from tkinter import font


class serverFrontend(Tk):
	'''
	Server User Interface
	Updated by Joel Conley
	June 18, 2019
	'''
	class Button_class(Tk):

		def button_specs(btn, text, font, row, col, padx, pady, ipadx, ipady, sticky):
			btn.text = text
			btn.font = font
			btn.row = row
			btn.col = col
			btn.padx = padx
			btn.pady = pady
			btn.ipadx = ipadx
			btn.ipady = ipady
			btn.sticky = sticky

			class_button = Button(btn, text=btn.text, font=btn.font)
			class_button.grid(row=btn.row, column = btn.col, padx=btn.padx, pady=btn.pady, ipadx=btn.ipadx,ipady=btn.ipady,sticky=btn.sticky)

			# UI.btn_start = Button(UI, text = "Start", font = UI.font)
			# UI.btn_start.grid(row = 0, column = 3,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")


	def __init__(UI):
		super().__init__()
		UI.root = Tk()
		UI.title("Server")
		UI.font = font.Font(family='Times', size=38, weight='bold')
		px = 2
		py = 2
		ipx = 2
		ipy = 2

		UI.btn_start = UI.Button_class.button_specs(UI, "Start", UI.font, 0, 0, px, py, ipx, ipy, "NE")
		UI.btn_stop = UI.Button_class.button_specs(UI, "Stop", UI.font, 0, 3, px, py, ipx, ipy, "SW")

		Label(text="Message Received:").grid(row=1)

		UI.mainloop()

	

		

	# def serverGUI():
	# 	# messagebox.showinfo("Title","Hello, World!")

		
	# 	btn_1 = Button(root,text = "1")
	# 	btn_1.grid(row = 0, column = 0,padx = 0,pady = 0,ipadx = 0,ipady = 0)

	# 	btn_2 = Button(root,text = "2")
	# 	btn_2.grid(row = 0, column = 1)

	# 	btn_3 = Button(root,text = "3")
	# 	btn_3.grid(row = 0, column = 2)

	# 	btn_4 = Button(root,text = "4")
	# 	btn_4.grid(row = 1, column = 0)

	# 	btn_5 = Button(root,text = "5")
	# 	btn_5.grid(row = 1, column = 1)

	# 	btn_6 = Button(root,text = "6")
	# 	btn_6.grid(row = 1, column = 2)

	# 	btn_7 = Button(root,text = "7")
	# 	btn_7.grid(row = 2, column = 0)

	# 	btn_8 = Button(root,text = "8")
	# 	btn_8.grid(row = 2, column = 1)

	# 	btn_9 = Button(root,text = "9")
	# 	btn_9.grid(row = 2, column = 2)

	# 	btn_enter = Button(root, text = "This is the enter button",command = enterButtonAction)
	# 	btn_enter.grid(row = 0,column = 3,rowspan = 3,sticky = "NS")


if __name__ == '__main__':
	serverFrontend()

# class serverBackend(Threading):



# class clientFrontend(Tk):



# class clientBackend():

