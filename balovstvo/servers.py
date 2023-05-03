from random import choice


class Server:
    ips = []

    def __new__(cls, *args, **kwargs):
        new_ip = choice([i for i in range(1, len(cls.ips) + 2) if i not in cls.ips])
        cls.ips.append(new_ip)
        return super().__new__(cls)

    def __del__(self):
        self.ips.remove(self.ip)

    def __init__(self):
        self.ip = self.ips[-1]
        self.buffer = []
        self.router = None

    def __repr__(self):
        return f"Сервер IP {self.ip} связан с роутером {self.router}"

    def send_data(self, data):
        self.router.buffer.append(data)

    def get_data(self):
        data = self.buffer.copy()
        self.buffer.clear()
        return data

    def get_ip(self):
        return self.ip


class Router:

    def __init__(self):
        self.servers = []
        self.buffer = []

    def link(self, server):
        self.servers.append(server)
        server.router = self

    def unlink(self, server):
        self.servers.remove(server)
        server.router = None

    def send_data(self):
        for server in self.servers:
            for data in self.buffer:
                if data.ip == server.ip:
                    server.buffer.append(data)

        self.buffer.clear()


class Data:

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

    def __repr__(self):
        return f"{self.data}, {self.ip}"


router = Router()
server_1 = Server()
server_2 = Server()
server_3 = Server()
server_4 = Server()

router.link(server_1)
router.link(server_2)
router.link(server_3)
router.link(server_4)

server_3.send_data(Data("Hello!", 1))
server_1.send_data(Data("Problem", 4))
server_1.send_data(Data("Problem!", 2))
server_3.send_data(Data("Not answer", 2))
server_3.send_data(Data("Hello!", 2))

router.send_data()

print(server_1.get_data())
print(server_2.get_data())
print(server_3.get_data())
print(server_4.get_data())
print(router.buffer)