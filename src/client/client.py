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
        self.isRecv = False
        self.size = -1

    #
    def connect(self, host="127.0.0.1", port=12321):
        self.s.connect((host, port))
        self.s.setblocking(0)

    #
    def disconnect(self):
        self.s.shutdown()
        self.s.close()

    #
    def send_data(self, data="", encode="utf-8"):
        import struct
        print("client send %s" % (data))
        self.s.send(struct.pack('!I', len(data)))
        self.s.send(data.encode(encode))

    #
    def recv_data(self, decode="utf-8"):
        import struct
        from socket import socket
        from time import sleep
        print("before client recv")
        try:
            if self.isRecv is False:
                size_buff = self.s.recv(4)
                self.size, = struct.unpack('!I', size_buff)
                self.isRecv = True
                return "{}"
            else:
                try:
                    data = self.s.recv(self.size).decode(decode)
                    print("after client recv %s size %d" % (data, self.size))
                    self.isRecv = False
                    return data
                except Exception:
                    return "{}"
        except Exception:
            return "{}"

import json
import math
from graphical_engine.graphicalEngine import GraphicalEngine

#
#   Functions
#

# Load graphical library and resources
def initGraphicalEngine(graphicalEngine):
    graphicalEngine.loadLibrary('graphical_engine.lib.pygletLib', 'PygletLib')
    initResources(graphicalEngine)

# Load library resources
def initResources(graphicalEngine):
    graphicalEngine.addResourcePath('./graphical_engine/assets/sprites')
    graphicalEngine.loadResourcePath()
    graphicalEngine.addImage('wall', 'wall.png')
    graphicalEngine.addImage('X', 'x-300px.png')
    graphicalEngine.addImage('O', 'o-300px.png')

# Add content to graphicalEngine
# def addContents(graphicalEngine, width, height, contents):
#     for index, case in enumerate(contents):
#
#         print("index: %d and case: %s" % (index, case))
#         optsWidth = graphicalEngine.getWindowWidth() // width
#         optsHeight = graphicalEngine.getWindowHeight() // height
#
#         if case != "":
#             opts = {
#                 "name": case,
#                 "width": optsWidth,
#                 "height": optsHeight,
#                 "x": ((index % width) * optsWidth),
#                 "y": ((int(math.floor(index // height))) * optsHeight)
#             }
#             optsId = "%s:x:%s:y:%s" % (opts['name'], opts['x'], opts['y'])
#             graphicalEngine.setSpriteDimension(opts['name'], optsWidth, optsHeight)
#             graphicalEngine.addContent(optsId, 'sprite', opts)

#
#   Script start here
#

# Game loop
def game(c, graphicalEngine):
    initGame = True
    playing = True
    running = False

    while playing:
        if initGame is True:
            dataFromServer = c.recv_data()
            print("Init %s" % (dataFromServer))
            dataFromServer = dataFromServer.replace("'", "\"")
            dataFromServer = json.loads(dataFromServer)
            if 'map-width' in dataFromServer:
                print("Got info")
                initGraphicalEngine(graphicalEngine)
                graphicalEngine.setMapSize(dataFromServer['map-width'], dataFromServer['map-height']);
                graphicalEngine.initWindow(500, 500)
                window = graphicalEngine.getWindow()
                initGame = False
        else:
            print("Already init")

            graphicalEngine.runOnline(c)

# Start graphical engine
def start(graphicalEngine):
    graphicalEngine.runOnline()

def main():
    graphicalEngine = GraphicalEngine()
    c = Client()


    try:
        c.connect()

        game(c, graphicalEngine)

        c.disconnect()
    except Exception as e:
        c.disconnect()
        print("Exception %s" % (e))
        graphicalEngine.close()
        exit(0)

if __name__ == '__main__':
    main()
