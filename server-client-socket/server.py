import socket
import threading
from datetime import datetime

HOST = '127.0.0.1'  # endereço de loopback
PORT = 65432 # porta que o servidor vai escutar

def iniciar_servidor():
    # cria o socket: AF_INET (IPv4) e SOCK_STREAM (TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT)) # associa o socket ao endereço e porta
        s.listen() # fica aguardando conexões
        
        print(f"Servidor escutando em {HOST}:{PORT}...")
        
        while True: # fica esperando nova conexão
            conn, addr = s.accept() # aceita a conexão
            nova_thread = threading.Thread(target=gerenciar_conexao, args=(conn, addr)) # cria uma nova thread para gerenciar a nova conexão
            nova_thread.start()
        

def gerenciar_conexao(conn: socket.socket, addr):
    with conn:
        print(f"Conectado por {addr}")
        while True:
            data = conn.recv(1024) # lê até 1024 bytes
            if not data:
                break # se não houver mais dados, a conexão foi encerrada
            
            texto_recebido = data.decode('utf-8')
            print(f"Mensagem recebida do cliente: {texto_recebido}")
            
            # inverte a string recebida e obtém o horário atual formatado
            texto_invertido = texto_recebido[::-1]
            horario_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            # envia a string invertida e o horário
            resposta = f"Texto invertido: {texto_invertido} | Horário: {horario_atual}"
            conn.sendall(resposta.encode('utf-8'))


if __name__ == "__main__":
    iniciar_servidor()

