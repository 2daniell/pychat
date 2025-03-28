import socket
from threading import Thread
from exception import PacketException
from events import EventDispatcher

class PacketListener:
    def __init__(self, server):
        self.server = server

class PacketMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct);
        if (hasattr(cls, 'id')):
            PacketProtocol.register(cls);

#Modelo de Pacote: [ID - 1 Byte] [CONTEUDO]
class Packet(metaclass=PacketMeta):
    
    def __init__(self, id=None):
        self.id = id
        
    def serialize(self):
        raise NotImplementedError
    
    def deserialize(self):
        raise NotImplementedError
    
class PacketProtocol:
    
    packets = {}

    @staticmethod    
    def register(packet: Packet):
        PacketProtocol.packets[packet.id] = packet
        
    @staticmethod
    def getPacket(id):
        if (id in PacketProtocol.packets):
            return PacketProtocol.packets[id];
        else:
            raise PacketException(id)
    
class PacketMessage(Packet):
    
    id = 1
    
    def __init__(self, message=""):
        super().__init__(self.id);
        self.message = message;
        
    def serialize(self):
        packet_id_bytes = self.id.to_bytes(1, 'big');
        message_bytes = self.message.encode('utf-8');
        return packet_id_bytes + message_bytes
    
    def deserialize(self, data):
        self.id = int.from_bytes(data[0:1], 'big');
        self.message = data[1:].decode('utf-8');

class ClientConnection:
    def __init__(self, client_socket: socket, addr):
        self.client_socket = client_socket;
        self.addr = addr;
        self.isRunning = True
        Thread(target=self.run).start();

    def sendPacket(self, packet: Packet):
        try:
            packet_data = packet.serialize();
            self.client_socket.send(packet_data);
        except Exception as e:
            print(f"Error: {e}");
        
    def disconnect(self):
        if (self.isRunning):
            print(f'Cliente {self.addr} desconectado.');
            self.client_socket.close();

    def run(self):
        while (self.isRunning):
            try:
                
                data = self.client_socket.recv(1024);
                
                if (not data):
                    print(f'Cliente {self.addr} desconectado.');
                    self.disconnect();
                    break;
                
                packet_id = int.from_bytes(data[0:1], 'big');
                packet_class = PacketProtocol.getPacket(packet_id);
                
                if (packet_class):
                    
                    packet = packet_class();
                    packet.deserialize(data);
                    
                    EventDispatcher.dispatch(f'packet_{packet.id}', packet, self.client_socket);
                
                
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