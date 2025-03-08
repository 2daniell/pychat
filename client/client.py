from screen import Screen
from connection import Connection

if __name__ == "__main__":
    try:
        screen = Screen("PyChat", 400, 600);
        connection = Connection("127.0.0.1", 8080);
        screen.run();
    except Exception as e:
        print(f'Ocorreu um erro interno: {e}');