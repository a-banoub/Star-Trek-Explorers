import json
from tkinter import *
import GameManager
import MapMaker
import sys

print (sys.path)
gamelog = 'gamelog.json'

def newgame (name):
    #name = input('Campaign Name?')
    campaign_name = name
    game = GameManager.game (campaign_name)
    game.make_game_directory()
    game.copymapdata()
    game.savegamedata()
    game.newpc(game)
    MapMaker.plotcourse(game.properties['Current System'], game)
    game.savegamedata()
    print (game.properties)
    game.mainmenu(game)

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
       newgame() 
       pass
    if userinput == ('load'):
        loadgame()
        pass
    else: 
        print ('Invalid Entry. Please try again.')
        gamemenu()

#startup = gamemenu()
