import socket
from threading import Thread

class Packet:
    ...

class ClientConnection:
    def __init__(self, client_socket: socket, addr):
        self.client_socket = client_socket;
        self.addr = addr;
        self.isRunning = True
        Thread(target=self.run).start();

    def sendPacket(self, packet: Packet):
        ...
        
    def disconnect(self):
        if (self.isRunning):
            print(f'Cliente {self.addr} desconectado.');
            self.client_socket.close();

    def run(self):
        ...

class Server:
    ...
    
if (__name__ == "__main__"):
    server = Server()
    server.run()