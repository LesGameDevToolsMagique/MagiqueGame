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
    def recv_data(self, decode="utf-8"):
        import struct
        size_buff = self.request.recv(4)
        size, = struct.unpack('!I', size_buff)

        data = self.request.recv(size).decode(decode)

        print("recv: %s" % (data))

        return data

    #
    def send_data(self, data="", encode="utf-8"):
        import struct
        self.request.send(struct.pack('!I', len(data)))
        print("send: %s" % (data))
        self.request.send(data.encode(encode))

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
