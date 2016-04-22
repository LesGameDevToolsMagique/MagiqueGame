#!/usr/bin/env python3

#
#   Client class
#

class Client(object):
    """
    """

    def __init__(self):
        from socket import socket
        self.c = socket()

    #
    def connect(self, host="127.0.0.1", port=12321):
        self.c.connect((host, port))

    #
    def disconnect(self):
        self.c.close()

    #
    def send_data(self, data="", encode="utf-8"):
        total_sent = 0

        while total_sent < len(data):
            s = self.c.send(data[total_sent:].encode(encode))
            if s == 0:
                raise RuntimeError("Connection lost")
            total_sent += s

        if total_sent > 0:
            self.send_data()

    #
    def recv_data(self, size=1024, decode="utf-8"):
        buff = []
        data = ""

        while not data:
            data = self.c.recv(size)
            if data:
                buff.append(data.decode(decode))

        return ''.join(buff)



#
#   Functions
#


#
#   Script start here
#

def main():
    c = Client()

    try:
        c.connect()
        print("%s" % (c.recv_data()))
        c.disconnect()
    except KeyboardInterrupt:
        c.disconnect()
        exit(0)

if __name__ == '__main__':
    main()
