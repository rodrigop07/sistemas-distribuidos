# client.py

import socket

HOST = '127.0.0.1'  # endereço IP do servidor
PORT = 8000 # porta usada pelo servidor

def iniciar_cliente():
    try:
        print(f"[Cliente] Conectando ao servidor em {HOST}:{PORT}...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
    except Exception as e:
        print(f"[Cliente] Erro ao se conectar: {e}")
        return

    try:
        mensagem = "Olá, Mundo Distribuído"
        s.sendall(mensagem.encode('utf-8'))
        print(f"[Cliente] Mensagem enviada: '{mensagem}'")

        data = s.recv(1024)
        if data:
            print(f"[Cliente] Resposta recebida do servidor: {data.decode('utf-8')}")
    except Exception as e:
        print(f"[Cliente] Erro na requisição: {e}")
    finally:
        s.close()
        print("[Cliente] Conexão encerrada. Cliente finalizado.")

if __name__ == "__main__":
    iniciar_cliente()
