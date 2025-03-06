import socket
from threading import Thread

class Packet:
    ...

class Connection:
    def __init__(self, host="127.0.0.1", port=8080):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.client_socket.connect((host, port));
        Thread(target=self.listen).start();
        
    def sendPacket(self, packet: Packet):
        ...
        
    def listen(self):
        while(True):
            data = self.client_socket.recv(1024);
            
    def close(self):
        self.client_socket.close();

if (__name__ == "__main__"):
    ...