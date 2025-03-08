from connection import Server
from events import EventDispatcher

server = Server()

def handle_message(packet, client_socket):
    print(f"Pacote com ID {packet.id} recebido.");
    for client in server.clients:
        if (client.client_socket is not client_socket):
            client.sendPacket(packet);
            
    print(f"Pacote com ID {packet.id} enviado para todos os clientes.");
    

EventDispatcher.subscribe('packet_1', handle_message)

if (__name__ == "__main__"):
    server.run()