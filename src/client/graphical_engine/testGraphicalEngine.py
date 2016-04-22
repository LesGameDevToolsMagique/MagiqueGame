import json
import math
from pprint import pprint
from graphicalEngine import GraphicalEngine
from gameEngine import GameEngine

# Init and configure graphical engine
graphical_engine = GraphicalEngine()

game_engine = GameEngine()
game_engine.loadGraphicalEngine(graphical_engine)

game_engine.graphicalEngine.loadLibrary('lib.pygletLib', 'PygletLib')
game_engine.graphicalEngine.addResourcePath('./assets/sprites')
game_engine.graphicalEngine.loadResourcePath()
game_engine.graphicalEngine.addImage('wall', 'wall.png')
game_engine.graphicalEngine.initWindow(500, 500)

data = game_engine.readJsonFile('testMap.json')

# Get map
width = data['width']
height = data['height']
game_map = data['map']

for index, case in enumerate(game_map):
    if case == 1:
        print 'x: ' + str(index % width) + ' y: ' + str(int(math.floor(index / width)))
        opts = {
            "name": "wall",
            "width": width,
            "height": height,
            "x": index % width,
            "y": int(math.floor(index / width))
            }
        wall_id = 'wall:x:' + str(opts['x']) + ':y:' + str(opts['y'])
        game_engine.graphicalEngine.addContent(wall_id, 'sprite', opts)

game_engine.graphicalEngine.library.run()
