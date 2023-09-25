import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []

nicknames=[]

print("Server has started...")

def clientthread(conn, nicknam):
    txt='Welcome to this chatroom, {}, you cannot leave'.format(nicknam)
    conn.send(txt.encode('utf-8'))
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                #print ("<" + addr[0] + "> " + message)
                print(message)

                #message_to_send = "<" + addr[0] + "> " + message
                broadcast(message, conn)
            else:
                remove(conn)
                remove_nickname(nicknam)
        except:
            continue

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message.encode('utf-8'))
            except:
                remove(clients)

def remove_nickname(nicknam):
    if nicknam in nicknames:
        nicknames.remove(nicknam)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    conn, addr = server.accept()
    conn.send("NICKNAME".encode('utf-8'))
    nicknam=conn.recv(2048).decode("utf-8")
    list_of_clients.append(conn)
    #print (addr[0] + " connected")
    nicknames.append(nicknam)
    message='{} has joined'.format(nicknam)
    print(message)
    broadcast(message,conn)
    new_thread = Thread(target= clientthread,args=(conn,nicknam))
    new_thread.start()