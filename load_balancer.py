"""
O desafio é manter os servidores o mais ocupados quanto é possível até um certo limite de capacidade. Em nosso ambiente de simulação cada tick de relógio (unidade de tempo) um certo número de usuários se conectam a servidores disponíveis e requisitam uma mesma tarefa a ser executada.

Cada tarefa consome Ttask ticks de tempo para ser executada e depois disso o usuário se desconecta imediatamente. Os servidores são máquinas virtuais que podem ser iniciadas instantaneamente para atender novos usuários. Cada servidor custa $1.00 por tick de relógio e consegue lidar com um número Umax de usuários simultaneos.

Você pode desligar servidores vazios, isso é, sem tarefas sendo executadas. Seu desafio é construir um programa em Python que lide com usuários acessando o sistema assinalando suas tarefas de forma que o custo de servidores ligados seja o minimo possível.

Entrada: Um arquivo que apresenta em cada linha o número de novos usuários acessando o sistema. Saída: Um arquivo em que cada linha contenha uma lista de servidores disponíveis ao final do tick representado o número de usuários conectados em cada servidor. Exemplo com Ttask = 4 e Umax = 2:

# Clock Ticks
# Input
# Output
# Tip
# 1
# 1
# 1
# 1 server for 1 user. (1 server created)
# 2
# 3
# 2,2
# 2 servers for 4 users. (1 server created)
# 3
# 0
# 2,2
# idem
# 4
# 1
# 2,2,1
# 3 servers for 5 users. (1 server created)
# 5
# 0
# 1,2,1
# 3 servers for 4 users. (First user left after 4 ticks)
# 6
# 1
# 2
# 1 server for 2 users (3 users left, 1 joined. 2 servers terminated)
"""

import time

TTAKS = 4
UMAX = 2

class LoadBalance:
    r"""
    >>> lb = LoadBalance([], max_users=2)
    >>> lb.get_status()
    '\n0 servers for 0 users. (0 servers created)'

    >>> lb.add_user(Task(4))
    >>> lb.get_status()
    '1\n1 servers for 1 users. (1 servers created)'
    >>> lb.tick()

    >>> lb.add_user(Task(4))
    >>> lb.add_user(Task(4))
    >>> lb.add_user(Task(4))
    >>> lb.get_status()
    '2, 2\n2 servers for 4 users. (1 servers created)'
    >>> lb.tick()

    >>> lb.get_status()
    '2, 2\n2 servers for 4 users. (0 servers created)'
    >>> lb.tick()

    >>> lb.add_user(Task(4))
    >>> lb.get_status()
    '2, 2, 1\n3 servers for 5 users. (1 servers created)'
    >>> lb.tick()

    >>> lb.get_status()
    '1, 2, 1\n3 servers for 4 users. (0 servers created)'
    >>> lb.tick()

    >>> lb.add_user(Task(4))
    >>> lb.get_status()
    '2\n1 servers for 2 users. (0 servers created)'
    >>> lb.tick()
    """

    server_created_this_tick = 0

    def __init__(self, *servers, max_users):
        self.servers = list(*servers)
        self.max_users = max_users

    def add_server(self, server):
        self.servers.append(server)
        self.server_created_this_tick += 1

    def get_free_server(self):
        for server in self.servers:
            if len(server.users) < self.max_users:
                break
        else:
            server = Server([], max_users=UMAX)
            self.add_server(server)
        return server

    def get_status(self):
        total_servers = 0
        total_users = 0
        users_status = []

        for server in self.servers:
            total_servers += 1
            total_users += len(server.users)
            users_status.append(len(server.users))

        # users_status = ', '.join(map(str, users_status))  # Menos legivel
        users_status = str(users_status)[1:-1]
        return f"{users_status}\n{total_servers} servers for {total_users} users. ({self.server_created_this_tick} servers created)"

    def add_user(self, user):
        server = self.get_free_server()
        server.add_user(user)

    def tick(self):
        self.server_created_this_tick = 0
        for server in self.servers:
            server.tick()
        self.servers = list(filter(lambda server:server.users != [], self.servers))


class Server:
    def __init__(self, *users, max_users):
        self.max_users = max_users
        self.users = list(*users)[:max_users]

    def add_user(self, user):
        self.users.append(user)

    def tick(self):
        for user in self.users:
            user.tick()
        self.users = list(filter(lambda user:user.ttask != 0, self.users))


class Task:
    def __init__(self, ttask):
        self.ttask = ttask

    def tick(self):
        self.ttask -= 1


if __name__ == "__main__":
    lb = LoadBalance([], max_users=UMAX)
    schedule = [1, 3, 0, 1, 0, 1]

    for i in schedule:
        for j in range(i):
            lb.add_user(Task(TTAKS))

        print(lb.get_status())
        print('Tick!')
        lb.tick()
        time.sleep(1)
