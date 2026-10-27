# Sistemas Distribuídos

## Projetos e Módulos

### 1. [chat-socket](./chat-socket) (Novo)
**Aplicação de Chat em Tempo Real Multithread**
- **Arquitetura**: Cliente-Servidor com sockets TCP (`AF_INET`, `SOCK_STREAM`).
- **Concorrência**: Threads dedicadas por cliente no servidor e threads desacopladas de envio (`input`) e recebimento (`recv`) no cliente.
- **Sincronização**: Uso de `threading.Lock` para garantir thread-safety no estado compartilhado dos usuários conectados e `threading.Event` para encerramento gracioso.
- **Recursos**: Mensagens públicas (broadcast), mensagens privadas (`/msg`), listagem de usuários online (`/usuarios`), validação de apelidos únicos e suíte de testes automatizados (`test_chat.py`).

### 2. [RPyC](./RPyC)
**Chamada de Procedimento Remoto (RPC)**
- Utiliza a biblioteca `rpyc` com `ThreadedServer` para expor serviços e executar procedimentos remotos de forma transparente.

### 3. [server-client-socket](./server-client-socket)
**Exemplo Introdutório Cliente/Servidor com Sockets**
- Simulação básica de modelo cliente/servidor com inversão de texto e consulta de horário via sockets e multithread.

---