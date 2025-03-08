import socket
from threading import Thread

class PacketException(Exception):
    def __init__(self, packet_id):
        self.packet_id = packet_id;
        self.message = f"Pacote com ID {packet_id} não encontrado.";
        super().__init__(self.message);

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
    
    def handle(self):
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
        
    def handle(self):
        print(self.message);

class Connection:
    def __init__(self, host="127.0.0.1", port=8080):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.client_socket.connect((host, port));
        Thread(target=self.listen).start();
        
    def sendPacket(self, packet: Packet):
        try:
            packet_data = packet.serialize();
            self.client_socket.send(packet_data);
        except Exception as e:
            print(f"Error: {e}");
        
    def listen(self):
        while(True):
            data = self.client_socket.recv(1024);
            packet_id = int.from_bytes(data[0:1], 'big');
            packet = PacketProtocol.getPacket(packet_id)();
            packet.deserialize(data);
            packet.handle();
            
    def close(self):
        self.client_socket.close();