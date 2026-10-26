import rpyc

HOST = '127.0.0.1'
PORT = 18812

def iniciar_cliente():
    try:
        print(f"Conectando ao servidor RPyC em {HOST}:{PORT}...")
        conn = rpyc.connect(HOST, PORT)
    except Exception as e:
        print(f"Erro ao se conectar: {e}")
        return

    try:
        horario = conn.root.obter_horario()
        print(f"Horário recebido do servidor: {horario}")
    except Exception as e:
        print(f"Erro na requisição: {e}")
    finally:
        conn.close()
        print("Conexão encerrada. Cliente finalizado.")

if __name__ == "__main__":
    iniciar_cliente()