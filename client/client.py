from screen import Screen
from connection import Connection, PacketMessage
from events import EventDispatcher
import sys

try:
    screen = Screen("PyChat", 400, 600);
    connection = Connection("127.0.0.1", 8080);
except Exception as e:
    print(f'Ocorreu um erro interno: {e}');
    sys.exit();
    
def handle_send_message(message):
    packet = PacketMessage(message);
    connection.sendPacket(packet);
    
def handle_close():
    connection.close();

EventDispatcher.subscribe("close", handle_close);
EventDispatcher.subscribe("send_message", handle_send_message);
    
if __name__ == "__main__":        
    screen.run();