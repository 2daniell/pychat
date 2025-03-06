import socket
import time
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
        while (self.isRunning):
            try:
                
                data = self.client_socket.recv(1024);
                
                if not data:
                    self.isRunning = False;
                    self.disconnect();
                    break;
                
                print(data);
            except Exception as e:
                print(f"Error: {e}");

class Server:
    
    def __init__(self, host="0.0.0.0", port=8080):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.server_socket.bind((host, port));
        self.server_socket.listen();
        self.clients = [];
        
    def run(self):
        print("Servidor iniciado. Aguardando conexões...");
        while True:
            client_socket, addr = self.server_socket.accept();
            client = ClientConnection(client_socket, addr);
            
            self.clients.append(client);
            
            print(f'Cliente {addr} conectado.');
    
if (__name__ == "__main__"):
    server = Server()
    server.run()