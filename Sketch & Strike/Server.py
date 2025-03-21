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

players = [(50, 50), (200, 200)]
clients = []

def threaded_client(conn, player):
    global players, clients
    conn.send(str.encode("Connected"))

    while True:
        try:
            data = conn.recv(4096).decode()
            if not data:
                print(f"Player {player} Disconnected")
                break

            x, y = map(int, data.split(","))
            players[player] = (x, y)

            other_player = 1 if player == 0 else 0
            reply = f"{players[other_player][0]},{players[other_player][1]}"
            conn.sendall(str.encode(reply))

        except:
            print(f"Connection lost with Player {player}")
            break

    conn.close()
    
    # Remove the client from the list
    if conn in clients:
        clients.remove(conn)

    # If all clients have disconnected, shut down the server
    if len(clients) == 0:
        print("No more clients connected. Shutting down server.")
        s.close()
        sys.exit()


while True: #accepts the clients to the server
    conn, addr = s.accept()
    if len(clients) < 2:
        clients.append(conn)
        player_id = len(clients) - 1
        print(f"Player {player_id} connected from {addr}")
        start_new_thread(threaded_client, (conn, player_id))
    else:
        conn.close()
