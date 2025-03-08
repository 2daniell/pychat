import flet as ft

class Screen:
    def __init__(self, title, width, height):
        self.title = title;
        self.width = width;
        self.height = height;
        
    def run(self):
        def main(page: ft.Page):
            page.title = self.title;
            page.window.width = self.width;
            page.window.height = self.height;
            
            messages = ft.ListView(expand=True, spacing=10)
            input_field = ft.TextField(label="Digite sua mensagem", expand=True)
            send_button = ft.ElevatedButton("Enviar")
            
            page.add(messages, ft.Row([input_field, send_button]))
        
        ft.app(target=main);