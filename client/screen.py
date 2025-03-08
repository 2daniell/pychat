import flet as ft
from events import EventDispatcher

class Screen:
    def __init__(self, title, width, height):
        self.title = title;
        self.width = width;
        self.height = height;
        self.messages: ft.ListView | None = None;
        self.page: ft.Page | None = None;
        
        EventDispatcher.subscribe("on_message", self.addMessage);
        
    def run(self):
        def main(page: ft.Page):
            self.page = page;
            page.title = self.title;
            page.window.width = self.width;
            page.window.height = self.height;
            
            self.messages = ft.ListView(expand=True, spacing=10)
            input_field = ft.TextField(label="Digite sua mensagem", expand=True)
            send_button = ft.ElevatedButton("Enviar", on_click=lambda _: self.sendMessage(input_field))
            
            page.add(self.messages, ft.Row([input_field, send_button]))
            
        ft.app(target=main);
        
    def sendMessage(self, input_field):
        message = input_field.value.strip();
        if (message):
            EventDispatcher.dispatch("send_message", message);
            input_field.value = "";
            self.addMessage(f'Você: {message}');
    
    def addMessage(self, message):
        if (self.messages):
            self.messages.controls.append(ft.Text(message));
            self.page.update();