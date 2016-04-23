#!/usr/bin/env python3

#
#   Client class
#

class Client(object):
    """
    """

    def __init__(self):
        from socket import socket
        self.s = socket()

    #
    def connect(self, host="127.0.0.1", port=12321):
        self.s.connect((host, port))

    #
    def disconnect(self):
        self.s.close()

    #
    def send_data(self, data="", encode="utf-8"):
        import struct
        self.s.send(struct.pack('!I', len(data)))
        send.s.send(data).encode(encode)

    #
    def recv_data(self, decode="utf-8"):
        import struct
        size_buff = self.s.recv(4)
        size, = struct.unpack('!I', size_buff)

        return self.s.recv(size).decode(decode)



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
        print("%s" % (c.recv_data()))
        c.disconnect()
    except KeyboardInterrupt:
        c.disconnect()
        exit(0)

if __name__ == '__main__':
    main()
