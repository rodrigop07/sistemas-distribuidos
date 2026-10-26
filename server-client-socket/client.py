import socket

HOST = '127.0.0.1' # endereço IP do servidor
PORT = 65432 # porta usada pelo servidor

def iniciar_cliente():
    # cria o socket: AF_INET (IPv4) e SOCK_STREAM (TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Tentando conectar a {HOST}:{PORT}...")
        
        try:
            s.connect((HOST, PORT)) # conecta ao servidor

        except Exception as e:
            print(f"Erro ao se conectar: {e}")
            exit()

        while True:
            print("0 - Sair")
            print("1 - Pedir horário ao servidor")
            opc = int(input("Escolha uma opcao: "))
            match opc:
                case 1:
                    mensagem = "Olá, Mundo Distribuído"
                    s.sendall(mensagem.encode('utf-8'))
                    print(f"Mensagem enviada: {mensagem}")

                    # aguarda resposta do servidor
                    data = s.recv(1024)
                    print(f"Recebido do servidor: {data.decode('utf-8')}")
                case 0:
                    exit()

if __name__ == "__main__":
    iniciar_cliente()

