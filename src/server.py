#!/usr/bin/env python

import socketserver, subprocess, sys
from threading import Thread
from pprint import pprint
from common.connection import Connection
import json
import re
import random

my_unix_command = ['bc']
HOST = 'localhost'
PORT = 12321

with open('expressions.json') as data_file:
    JSONexp = json.load(data_file)['expressions']
                
class JSONHandler:
    def ranexp(self):
        return (random.choice(JSONexp))

class gameLogic:
    """
    """

    def __init__(self):
        self.currentExp = None

    def newExpression(self):
        self.currentExp = JSONHandler.ranexp(self)
        self.request.send(str(self.currentExp).encode('utf-8'))

    def inputCheck(self, text, force):
        if ('aze' in text):
            self.newExpression()
            
    def responseCheck(self, response):
        print(self.currentExp['answer'])
        if (response is self.currentExp['answer']):
            return True
        return False

class SingleTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print ("%s connected", self.client_address[0])
        go = True
        while go:
            gameLogic.newExpression(self)
            data = self.request.recv(1024)
            if not data:
                go = False
            else:
                text = data.decode('utf-8')
                print("Client wrote: ", text)
                if (gameLogic.responseCheck(self, text[0]) is True):
                    print ('ok')
                else:
                    go = False
                    print('ko')
        print ("%s disconnected", self.client_address[0])
                            
class SimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True
            
def __init__(self, server_address, RequestHandlerClass):
    socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)
                
if __name__ == "__main__":
    server = SimpleServer((HOST, PORT), SingleTCPHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
