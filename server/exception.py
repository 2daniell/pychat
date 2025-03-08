class PacketException(Exception):
    def __init__(self, packet_id):
        self.packet_id = packet_id;
        self.message = f"Pacote com ID {packet_id} não encontrado.";
        super().__init__(self.message);