import json
from tkinter import *
import GameManager
import MapMaker

gamelog = 'gamelog.json'

def newgame():
    game = GameManager.game (input('Campaign Name?'))
    game.savegamedata()
    game.newpc(game)
    MapMaker.plotcourse(game.properties['Current System'], game)
    game.savegamedata()
    print (game.properties)
    game.mainmenu

def loadgame():
    with open (gamelog) as log: 
        data = json.load(log)
        for index, entry in enumerate(data):
            print(f"Index: {index}, Campaign Name: {entry['Campaign Name']}")

    loadindex = input('Index to Load?')

    game = GameManager.game('Loaded Game')
    game.load_game_data(gamelog, loadindex)

    game.mainmenu (game)

    load = loadgame()

def gamemenu():
    print ('Main Menu. Type "new" for a new campaign or "load" to load')
    userinput = input('Prompt: ')
    if userinput == ('new'): 
        action = newgame()
        pass
    if userinput == ('load'):
        action = loadgame()
        pass
    else: 
        print ('Invalid Entry. Please try again.')
        action = gamemenu()
    action

startup = gamemenu ()
