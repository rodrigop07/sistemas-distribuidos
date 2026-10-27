import rpyc
from rpyc.utils.server import ThreadedServer
from datetime import datetime
import threading
import time

HOST = '127.0.0.1'
PORT = 18812

class ServicoProcessamento(rpyc.Service):
    def on_connect(self, conn):
        print("[Servidor] Cliente conectado")

    def on_disconnect(self, conn):
        print("[Servidor] Cliente desconectado")

    def exposed_obter_horario(self) -> str:
        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[Servidor] Horário solicitado. Enviando: {horario}")
        return horario

def rodar_servidor():
    servidor = ThreadedServer(
        ServicoProcessamento,
        hostname=HOST,
        port=PORT,
        protocol_config={"allow_public_attrs": True}
    )
    servidor.start()

thread_servidor = threading.Thread(target=rodar_servidor, daemon=True)
thread_servidor.start()

time.sleep(1)