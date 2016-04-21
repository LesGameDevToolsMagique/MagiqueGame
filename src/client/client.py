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
    def send_data(self, data=""):
        total_sent = 0

        while total_sent < len(data):
            s = self.c.send(data[total_sent:].encode())
            if s == 0:
                raise RuntimeError("Connection lost")
            total_sent += s

        if total_sent > 0:
            self.send_data()

    #
    def recv_data(self, size=1024, decode="utf-8"):
        buff = []
        data = ""

        while data is not None:
            data = self.c.recv(size)
            if data is not None:
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
    stop = False
    c.connect()

    while stop is False:
        c.send_data(str(input()))
        stop = True

    c.disconnect()

if __name__ == '__main__':
    main()
