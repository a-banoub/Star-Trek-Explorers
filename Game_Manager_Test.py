import CharacterSheet
from tkinter import *
from tkinter import ttk
import Archetypes
import PDFCreator
import GameManager
import os
import MapMaker


game = GameManager.game('saa')

game.savegamedata()

game.newpc(game)

MapMaker.plotcourse(game.properties['Current System'], game)

game.savegamedata()

print (game.properties)

game.mainmenu(game)