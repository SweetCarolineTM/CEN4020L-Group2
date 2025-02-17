import socket

# class thats responsible for connection to the server

class Network:
    def __init__(self):
        self.client = socket.socket(socket.INET, socket.SOCK_STREAM)
        self.server = "" #keep consistent with server
        self.port =5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        #print(self.pos)

    def getPos(self):
        self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

"""n = Network()
print(n.send("hello"))
print(n.send("working"))

"""