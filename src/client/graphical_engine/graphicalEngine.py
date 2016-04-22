import importlib

class GraphicalEngine:

    # Load library module, here the name is the file name
    # and the module the class name
    def loadLibrary(self, name, module):
        self.library = getattr(importlib.import_module(name), module)()

    # Init windows
    def initWindow(self, width, height):
        self.library.initWindow(width, height)

    # Add content, or object in game
    def addContent(self, id, type, options):
        self.library.addContent(id, type, options)

    # Set sprite dimension by name
    def setSpriteDimension(self, name, width, height):
        self.library.setSpriteDimension(name, width, height)

    # Add resource path
    def addResourcePath(self, path):
        self.library.addResourcePath(path)

    # Load all the resource path
    def loadResourcePath(self):
        self.library.loadResourcePath()

    # Add image in resources
    def addImage(self, name, path):
        self.library.addImage(name, path)

    # Draw from library
    def draw(self):
        self.library.draw()

    # Run the library
    def run(self):
        self.library.run()

    # Close library
    def close(self):
        self.library.close()
