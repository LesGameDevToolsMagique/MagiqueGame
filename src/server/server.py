#!/usr/bin/env python3

from socketserver import TCPServer, ThreadingMixIn, BaseRequestHandler

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
    def send_data(self, data=""):
        total_sent = 0

        while total_sent < len(data):
            s = self.request.send(data[total_sent:].encode())
            if s == 0:
                raise RuntimeError("Connection lost")
            total_sent += s

        if total_sent > 0:
            self.send_data()

    #
    def handle(self):
        stop = False
        # g = Game(self)

        # g.run()
        while not stop:
            data = self.recv_data()
            stop = True

        # g.destroy()
        print("%s" % (data))


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
