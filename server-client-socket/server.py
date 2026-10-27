# server.py

import socket
import threading
from datetime import datetime
import time

HOST = '127.0.0.1' # endereço de loopback
PORT = 8000 # porta específica

def gerenciar_conexao(conn: socket.socket, addr):
    with conn:
        print(f"[Servidor] Conectado por {addr}")
        data = conn.recv(1024)
        if not data:
            return

        texto_recebido = data.decode('utf-8')
        print(f"[Servidor] Mensagem recebida: '{texto_recebido}'")

        # inverte a string recebida e obtém o horário atual formatado
        texto_invertido = texto_recebido[::-1]
        horario_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # envia a string invertida e o horário do momento solicitado
        resposta = f"Texto invertido: {texto_invertido} | Horário: {horario_atual}"
        conn.sendall(resposta.encode('utf-8'))
        print(f"[Servidor] Resposta enviada para {addr}. Conexão encerrada.")

def rodar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"[Servidor] Escutando em {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            nova_thread = threading.Thread(target=gerenciar_conexao, args=(conn, addr), daemon=True)
            nova_thread.start()

thread_servidor = threading.Thread(target=rodar_servidor, daemon=True)
thread_servidor.start()

time.sleep(1)
