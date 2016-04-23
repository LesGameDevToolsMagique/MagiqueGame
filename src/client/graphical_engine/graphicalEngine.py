import importlib

class GraphicalEngine:

    # Load library module, here the name is the file name
    # and the module the class name
    def loadLibrary(self, name, module):
        self.library = getattr(importlib.import_module(name), module)()

    # Init windows
    def initWindow(self, width, height):
        self.library.initWindow(width, height)

    # Add contents
    def addContents(self, width, height, contents):
        self.library.addContents(width, height, contents)

    # Add content, or object in game
    def addContent(self, id, type, options):
        self.library.addContent(id, type, options)

    # Set sprite dimension by name
    def setSpriteDimension(self, name, width, height):
        self.library.setSpriteDimension(name, width, height)

    # Set map dimension
    def setMapSize(self, width, height):
        self.library.setMapSize(width, height)

    def getMapWidth(self):
        return self.library.getMapWidth()

    def getMapHeight(self):
        return self.library.getMapHeight()

    # Add resource path
    def addResourcePath(self, path):
        self.library.addResourcePath(path)

    # Load all the resource path
    def loadResourcePath(self):
        self.library.loadResourcePath()

    # Add image in resources
    def addImage(self, name, path):
        self.library.addImage(name, path)

    # Get window width
    def getWindowWidth(self):
        return self.library.getWindowWidth()

    # Get window height
    def getWindowHeight(self):
        return self.library.getWindowHeight()

    # Get window
    def getWindow(self):
        return self.library.window

    # Draw from library
    def draw(self):
        self.library.draw()

    # Def runOnline
    def runOnline(self, client):
        self.library.runOnline(client)

    # Run the library
    def run(self):
        self.library.run()

    # Close library
    def close(self):
        self.library.close()
