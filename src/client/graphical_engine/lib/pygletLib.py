import pyglet
import json
import math

class PygletLib:

    def __init__(self):

        # Game content
        self.content = {}

        # Graphical ressource management
        self.assets = {}
        self.resourcePath = []

    # Open a window
    def initWindow(self, width, height):
        self.window = pyglet.window.Window(width, height)
        self.ratioWidth = self.window.width // width
        self.ratioHeight = self.window.height // height

    # Get window width
    def getWindowWidth(self):
        return self.window.width

    # Get window height
    def getWindowHeight(self):
        return self.window.height

    # Draw content
    def draw(self):
        for key, value in self.content.items():

            # Center horizontally and vertically
            if 'center' in value['opts'] and value['opts']['center']:
                value['opts']['x'] = self.window.width//2
                value['opts']['y'] = self.window.height//2

            # Center horizontally
            if 'center-width' in value['opts'] and value['opts']['center-width']:
                value['opts']['x'] = self.window.width//2

            # Draw label
            if value['type'] == 'label':
                self.drawLabel(value['text'], value['opts']);

            # Add input box
            if value['type'] == 'input_box':
                self.draw_quads(value['opts'])
                self.drawInputBox(value['text'], value['opts']);

            # Add sprite
            if value['type'] == 'sprite':
                #print("SPRITE")
                self.drawSprite(value['opts']['name'], value['opts'])

    # Update content
    def update(self, instructions):
        for key, value in instructions.iteritems():

            # Add or update content
            if value['action'] == 'update':
                self.content[key] = value['content']

            # Delete content
            if value['action'] == 'delete':
                del self.content[key]

    # Set sprite dimension
    def setSpriteDimension(self, name, width, height):
        self.assets[name].width = width
        self.assets[name].height = height

    # Set map dimension
    def setMapSize(self, width, height):
        self.mapWidth = width
        self.mapHeight = height

    def getMapWidth(self):
        return self.mapWidth

    def getMapHeight(self):
        return self.mapHeight

    # Add content
    def addContent(self, id, type, options):
        content = { 'type': type, 'opts': options }
        self.content[id] = content

    # Add resources path
    def addResourcePath(self, path):
        self.resourcePath.append(path)

    # Load all resource path contain in resourcePath array
    def loadResourcePath(self):
        pyglet.resource.path = self.resourcePath
        pyglet.resource.reindex()

    # Add image
    def addImage(self, name, path):
        self.assets[name] = pyglet.resource.image(path)

    # Add a text to containers
    def addText(self, id, type, text, options):
        document = { 'type': type, 'text': text, 'opts': options }
        self.content[id] = document

    # Draw label
    def drawLabel(self, text, opts):
        document = pyglet.text.decode_text(text)
        pyglet.text.Label(document.text, font_name='Times New Roman', font_size=36, x=opts['x'], y=opts['y'], anchor_x='center', anchor_y='center').draw()

    # Draw sprite
    def drawSprite(self, name, opts):
        #print("NAME %s, OPTIONS %s" % (name, opts))
        self.assets[name].blit(opts['x'], opts['y'])

    # Draw input box
    def drawInputBox(self, text, opts):
        document = pyglet.text.decode_text(text)
        pyglet.text.Label(document.text, font_name='Times New Roman', font_size=36, color=(0, 0, 0, 255), x=opts['x'], y=opts['y'], anchor_x='center', anchor_y='center').draw()

    # Draw quads
    def drawQuads(self, opts):
        upLeft = (opts['x'], opts['y'] + opts['height'])
        upRight = (opts['x'] + opts['width'], opts['y'] + opts['height'])
        downLeft = (opts['x'], opts['y'])
        downRight = (opts['x'] + opts['width'], opts['y'] - opts['height'])

        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2f', (upLeft[0], upLeft[1],
                                      upRight[0], upRight[1],
                                      downRight[0], downRight[1],
                                      downLeft[0], downLeft[1])))

    # Add content to graphicalEngine ( Like a private method )
    def addContents(self, width, height, contents):
        for index, case in enumerate(contents):

            #print("index: %d and case: %s" % (index, case))
            optsWidth = self.window.width // width
            optsHeight = self.window.height // height

            if case:
                # print("case is not empty => %s" % (case))
                opts = {
                    "name": case,
                    "width": optsWidth,
                    "height": optsHeight,
                    "x": ((index % width) * optsWidth),
                    "y": ((int(math.floor(index // height))) * optsHeight)
                }
                optsId = "%s:x:%s:y:%s" % (opts['name'], opts['x'], opts['y'])
                #print("add content %s" % (optsId))
                self.setSpriteDimension(opts['name'], optsWidth, optsHeight)
                self.addContent(optsId, 'sprite', opts)

    # Run pyglet online app
    def runOnline(self, client):

        @self.window.event
        def on_draw():
            self.window.clear()

            dataFromServer = client.recv_data()
            dataFromServer = dataFromServer.replace("'", "\"")
            #print("Not init %s" % (dataFromServer))
            contents = json.loads(dataFromServer)

            if 'map' in contents:
                self.addContents(self.mapWidth, self.mapHeight, contents['map'])

            self.draw()


        @self.window.event
        def on_mouse_press(x, y, button, modifiers):
            if pyglet.window.mouse.LEFT:
                posX = math.floor((x * self.mapWidth) // self.window.width)
                posY = math.floor((y * self.mapHeight) // self.window.height)
                toSend = "{\"x\": %d, \"y\": %d}" % (posX, posY)
                print(toSend)
                client.send_data(toSend)
            elif pyglet.window.mouse.RIGHT:
                posX = math.floor((x * self.mapWidth) // self.window.width)
                posY = math.floor((y * self.mapHeight) // self.window.height)
                client.send_data("{\"x\": %d, \"y\": %d}" % (posX, posY))

        @self.window.event
        def on_key_press(symbol, modifiers):
            if (symbol == pyglet.window.key.ESCAPE):
                self.close()
                exit(0)

        pyglet.app.run()

    # Run pyglet app
    def run(self):
        @self.window.event
        def on_draw():
            self.window.clear()

            # Don't forget to uncomment when receiving object from server
            # self.update(new_object)

            self.draw()

        @self.window.event
        def on_mouse_press(x, y, button, modifiers):
            if pyglet.window.mouse.LEFT:
                print("Left mouse at x: %d y: %d" % (x, y))
                pass
            elif pyglet.window.mouse.RIGHT:
                print("Right mouse at x: %d y: %d" % (x, y))
                pass

        pyglet.app.run()

    # Close pyglet app
    def close(self):
        pyglet.app.exit()
