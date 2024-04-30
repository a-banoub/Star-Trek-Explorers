from tkinter import *
import GameManager
import MapMaker

game = GameManager.game ('ssadas')

game.savegamedata()

game.newpc(game)

MapMaker.plotcourse(game.properties['Current System'], game)

game.savegamedata()

print (game.properties)

game.mainmenu