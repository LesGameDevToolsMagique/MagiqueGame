#!/usr/bin/env python3

from socketserver import TCPServer, ThreadingMixIn, BaseRequestHandler
from game_engine import TicTacToe

#
#   Handler class
#

class ClientHandler(BaseRequestHandler):
    """
    """

    #
    def recv_data(self, size=1024, decode="utf-8"):
        buff = []
        data = ""

        while not data:
            data = self.request.recv(size)
            if data:
                buff.append(data.decode(decode))

        return ''.join(buff)

    #
    def send_data(self, data="", encode="utf-8"):
        total_sent = 0

        while total_sent < len(data):
            s = self.request.send(data[total_sent:].encode(encode))
            if s == 0:
                raise RuntimeError("Connection lost")
            total_sent += s

        if total_sent > 0:
            self.send_data()

    #
    def handle(self):
        game = TicTacToe(self)

        game.init()

        game.run()

        game.destroy()


#
#   Server class
#

class Server(TCPServer, ThreadingMixIn):
    """
    """
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, host="127.0.0.1", port=12321):
        TCPServer.__init__(self, (host, port), ClientHandler)


#
#   Script start
#

def main():
    s = Server()

    try:
        s.serve_forever()
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main()
