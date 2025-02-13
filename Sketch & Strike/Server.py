from socket import *
import sys
import time
from _thread import *


#first, run this server script in order to run endless client scripts
#running on the local ip of the machine running it


server ="" #use local ip of your machine, w/ ipconfig in terminal
port = 5555 #if port is already used for something this will fail

s =socket.socket(socket.INET,socket.SOCK_STREAM) #inet represents the type of ipv4, and sock stream how string comes in 

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
#print("waiting for connection, server started")

"""
def hostGame(password):
    foo = False
"""

def threaded_client(conn):
    
    conn.send(str.encode("Connected"))

    reply = ""
    while True:
        try:
            data = conn.recv(2048) # this is a bit amount, if errors increase this size, but larger, longer it will take to recv info
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("received ", reply)
                print("sending ", reply)
            conn.sendall(str.encode(reply))
        
        except:
            break

    print("Lost connection")
    conn.close()


while True:
    #continuously look for connections,
    conn,addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, )) #this will brancha  new process, while others still run, should handle more than 2 players
