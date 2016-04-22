import pyglet

class PygletLib:

    def __init__(self):

        # Game content
        self.content = {}

        # Grphical ressource management
        self.assets = {}
        self.resourcePath = []

    # Open a window
    def initWindow(self, width, height):
        self.window = pyglet.window.Window(width, height)

    # Draw content
    def draw(self):
        for key, value in self.content.iteritems():

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
    def setSpriteDimension(self, sprite, width, height):
        sprite['options']['width'] = width
        sprite['options']['height'] = height

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
        width = self.window.width // opts['width']
        height = self.window.height // opts['height']
        self.assets[name].width = width
        self.assets[name].height = height
        self.assets[name].blit(opts['x'] * width, opts['y'] * height)

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

    # Run pyglet app
    def run(self):
        @self.window.event
        def on_draw():
            self.window.clear()

            # Don't forget to uncomment when receiving object from server
            # self.update(new_object)

            self.draw()

        pyglet.app.run()
