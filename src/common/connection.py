import socket

class Connection(object):
    """
    """

    def __init__(self):
        self.s = socket.socket()

    def connect(self, host, port):
        self.s.connect((host, port))

    def disconnect(self):
        self.s.close()

    def send(self, message=None):
        self.s.send(message.encode())

    def receive(self, recv_size=1024, decode="utf-8"):
        string = self.s.recv(recv_size).decode(decode)
        return str(string)
