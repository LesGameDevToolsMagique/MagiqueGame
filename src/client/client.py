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
        self.s.send(data.encode(encode))

    #
    def recv_data(self, decode="utf-8"):
        import struct
        size_buff = self.s.recv(4)
        size, = struct.unpack('!I', size_buff)

        return self.s.recv(size).decode(decode)


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
    print(graphicalEngine.library.assets)

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
        if initGame == True:
            dataFromServer = c.recv_data()
            dataFromServer = dataFromServer.replace("'", "\"")
            print("Init %s" % (dataFromServer))
            dataFromServer = json.loads(dataFromServer)
            initGraphicalEngine(graphicalEngine)
            graphicalEngine.setMapSize(dataFromServer['map-width'], dataFromServer['map-height']);
            graphicalEngine.initWindow(500, 500)
            window = graphicalEngine.getWindow()
            initGame = False
        else:
            if running == False:
                graphicalEngine.runOnline(c)
                running = True

            dataFromServer = c.recv_data()
            dataFromServer = dataFromServer.replace("'", "\"")
            print("Not init %s" % (dataFromServer))
            contents = json.loads(dataFromServer)

            if 'map' in contents:
                graphicalEngine.addContents(graphicalEngine.getMapWidth(), graphicalEngine.getMapHeight(), contents['map'])
                graphicalEngine.getWindow().clear()
                graphicalEngine.draw()

    # start(graphicalEngine)

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
    except KeyboardInterrupt:
        c.disconnect()
        graphicalEngine.close()
        exit(0)

if __name__ == '__main__':
    main()
