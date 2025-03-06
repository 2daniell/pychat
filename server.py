import socket
import time
from threading import Thread

#Modelo de Pacote: [ID - 1 Byte] [CONTEUDO]
class Packet:
    def __init__(self, id=None):
        self.id = id
        
    def serialize(self):
        raise NotImplementedError
    
    def deserialize(self):
        raise NotImplementedError
    
    def handle(self):
        raise NotImplementedError
    
class PacketMessage(Packet):
    def __init__(self, id=1, message=""):
        super().__init__(id);
        self.message = message;
        
    def serialize(self):
        packet_id_bytes = self.id.to_bytes(1, 'big');
        message_bytes = self.message.encode('utf-8');
        return packet_id_bytes + message_bytes
    
    def deserialize(self, data):
        self.id = data[0];
        self.message = data[1:];

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