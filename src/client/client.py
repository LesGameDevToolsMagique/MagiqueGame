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


import json
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

# Convert json string into python dictionary
def deserializeJson(jsonString):
    print("json string: %s" % (jsonString))
    json.loads(jsonString)

# Add content to graphicalEngine
def addContents(graphicalEngine, width, height, contents):
    for index, case in enumerate(contents):

        optsWidth = graphicalEngine.getWindowWidth() // width
        optsHeight = graphicalEngine.getWindowHeight() // height

        if case != "":
            opts = {
                "name": case,
                "width": optsWidth,
                "height": optsHeight,
                "x": ((index % width) * optsWidth),
                "y": ((int(math.floor(index // height))) * optsHeight)
            }
            optsId = "%s:x:%s:y:%s" % (opts['name'], opts['x'], opts['y'])
            graphicalEngine.setSpriteDimension(opts['name'], optsWidth, optsHeight)
            graphicalEngine.addContent(optsId, 'sprite', opts)

#
#   Script start here
#

# Game loop
def game(c, graphicalEngine):
    playing = True
    initGame = True
    while playing:
        dataFromServer = c.recv_data()
        dataFromServer = dataFromServer.replace("'", "\"")
        print("%s" % (dataFromServer))
        dataFromServer = json.loads(dataFromServer)
        if initGame:
            initGraphicalEngine(graphicalEngine)
            graphicalEngine.initWindow(500, 500)
            initGame = False
            start(graphicalEngine)
        else:
            addContents(graphicalEngine, 500, 500, contents.map)

# Start graphical engine
def start(graphicalEngine):
    graphicalEngine.run()

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
