import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

clientes = []

def broadcast(mensagem, remetente=None):
    for cliente in list(clientes):
        if cliente != remetente:
            try:
                cliente.sendall(mensagem)
            except:
                remover_cliente(cliente)

def remover_cliente(cliente):
    if cliente in clientes:
        clientes.remove(cliente)
        try:
            cliente.close()
        except:
            pass

def gerenciar_cliente(conn, addr):
    nome = ""
    try:
        nome = conn.recv(1024).decode('utf-8')
        clientes.append(conn)
        print(f"[CONEXÃO] {nome} conectou-se de {addr}.")
        broadcast(f"--> {nome} entrou no chat.".encode('utf-8'), remetente=conn)

        while True:
            mensagem = conn.recv(1024)
            if not mensagem:
                break
            texto = f"{nome}: {mensagem.decode('utf-8')}".encode('utf-8')
            broadcast(texto, remetente=conn)

    except:
        pass
    finally:
        remover_cliente(conn)
        if nome:
            print(f"[DESCONEXÃO] {nome} saiu do chat.")
            broadcast(f"<-- {nome} saiu do chat.".encode('utf-8'))

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"Servidor de chat rodando em {HOST}:{PORT}...")

    while True:
        conn, addr = servidor.accept()
        thread = threading.Thread(target=gerenciar_cliente, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()
