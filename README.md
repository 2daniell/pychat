# PyChat - Aplicação de Chat

PyChat é um projeto de chat desenvolvido de forma modular e seguindo os princípios da programação orientada a objetos. Ele utiliza um protocolo de aplicação personalizado para facilitar a comunicação entre cliente e servidor.

## Objetivo

O objetivo do projeto é criar uma aplicação de chat que seja fácil de manter e expandir, garantindo modularidade e organização por meio de um sistema de pacotes bem estruturado.

## Arquitetura e Protocolo de Aplicação 

O projeto implementa um sistema de pacotes para comunicação entre cliente e servidor. Cada tipo de pacote deve estender a classe `Packet`.  

### Estrutura do Protocolo

1. **Registro de Pacotes**:  
   - Todos os pacotes estendidos a partir da classe `Packet` são registrados automaticamente classe `PacketProtocol`.  
   - Isso permite que o sistema reconheça e interprete os pacotes corretamente.

2. **Formato de Envio**:  
   - Os pacotes são  serializados em bytes com o seguinte formato:  
     ```
     <ID> <Conteudo>
     ```
   - No momento da recepção, o sistema busca o pacote correspondente ao ID registrado e interpreta os seus dados.

Esse modelo modular facilita a manutenção e a expansão do projeto, permitindo adicionar novos tipos de pacotes sem comprometer a estrutura principal.

---

## Como Executar

### Clonar o Repositório

```sh
git clone https://github.com/2daniell/pychat
cd pychat
```

### Executar o Servidor

```sh
cd server
python server.py
```

### Executar o Cliente

#### Criar ambiente virtual (opcional, mas recomendado)
```sh
python -m venv venv  # Criar ambiente virtual
```

Para Linux/Mac:
```sh
source venv/bin/activate
```

Para Windows:
```sh
venv\Scripts\activate
```

#### Instalar dependências e executar o cliente
```sh
pip install flet[all]
python client.py
```

---

## Autor

Projeto desenvolvido por **Daniel**  
Matrícula: **20241370017**

---

