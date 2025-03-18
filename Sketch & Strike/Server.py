import socket
from _thread import *
import sys
from tkinter import CURRENT

server = socket.gethostbyname(socket.gethostname()) 
port = int(sys.argv[1]) if int(sys.argv[1]) >= 5000 else 5555 #otherwise just use 5555 if the port entered is too small

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print(f"Server started at {server}:{port}") #You want the connecting client to join via this ip and port

def threaded_client(conn, player):
    conn.send(str.encode("Connected"))
    while True:
        try:
            data = conn.recv(2048).decode()
            if not data:
                print("Disconnected")
                break
            print(f"Player {player} sent: {data}")
            conn.sendall(str.encode(f"Player {player}: {data}"))
        except Exception as e:
            print(f"error with {player}")
            break
    print(f"Connection closed for {player}") #the message is sent then the client exits
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print(f"Connected to: {addr}")
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
