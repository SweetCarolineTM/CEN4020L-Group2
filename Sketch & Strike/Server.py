import socket
import sys
import time
from _thread import *


#first, run this server script in order to run endless client scripts
#running on the local ip of the machine running it


server ="10.134.131.249" #use local ip of your machine, w/ ipconfig in terminal
port = 5555 #if port is already used for something this will fail

s =socket.socket(socket.AF_INET,socket.SOCK_STREAM) #inet represents the type of ipv4, and sock stream how string comes in 

try:
    s.bind((server,port))
except socket.error as e:
    str(e)
    sys.exit(1)

s.listen(2)
print("waiting for connection, server started")

"""
def hostGame(password):
    foo = False
"""

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,0),(100,100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1