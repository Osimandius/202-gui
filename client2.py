import socket
from threading import Thread
from tkinter import *

# nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")

        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)
        
        self.pls = Label(self.login,
					text = "Please login to continue",
					justify = CENTER,
					font = "Helvetica 14 bold")
        self.pls.place( relheight = 0.15,
                        relx = 0.2,
                        rely = 0.07)

        self.labelName = Label(self.login,
							text = "Name: ",
							font = "Helvetica 12")
        self.labelName.place(relheight = 0.2,
							relx = 0.1,
							rely = 0.2)

        self.entryName = Entry(self.login,
							font = "Helvetica 14")
        self.entryName.place(relwidth = 0.4,
							relheight = 0.12,
							relx = 0.35,
							rely = 0.2)
        self.entryName.focus()
        self.go=Button(self.login,text="BUTTON.",font="Helvetica 14 bold",command=lambda:self.goahead(self.entryName.get()))
        self.go.place(relx=0.4,rely=0.5)
        self.Window.mainloop()
    
    def goahead(self,name):
        self.login.destroy()
        self.name=name
        r=Thread(target=self.received)
        r.start()

    def received(self):
     while True:
         try:
             message = client.recv(2048).decode('utf-8')
             if message == 'NICKNAME':
                 client.send(self.name.encode('utf-8'))
             else:
                 print(message)
         except:
             print("An error occured!")
             client.close()
             break
g = GUI()
