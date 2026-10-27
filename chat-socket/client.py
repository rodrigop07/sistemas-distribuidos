import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def receber_mensagens(s):
    while True:
        try:
            mensagem = s.recv(1024).decode('utf-8')
            if not mensagem:
                break
            print(mensagem)
        except:
            break

def iniciar_cliente():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")
        return

    nome = input("Digite seu nome: ")
    s.sendall(nome.encode('utf-8'))

    thread = threading.Thread(target=receber_mensagens, args=(s,), daemon=True)
    thread.start()

    print("Conectado ao chat. Digite sua mensagem:\n")

    while True:
        try:
            mensagem = input()
            if mensagem.lower() == 'sair':
                break
            if mensagem.strip():
                s.sendall(mensagem.encode('utf-8'))
        except:
            break

    s.close()
    print("Você saiu do chat.")

if __name__ == "__main__":
    iniciar_cliente()
