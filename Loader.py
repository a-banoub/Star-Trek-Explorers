import GameManager
import GameMenu as gm
import pickle
import os

gamelog = 'gamelog.json'

gamedir = {}

def newgame():
	gname = input("Campaign Name?")
	game = GameManager.game(gname)
	game.savegamedata()
	
	gamedir [gname] = game
	
	with open ('gamelog.pickle', 'wb') as file:
		pickle.dump(gamedir, file)

	print (f'{gname} campaign saved')
	print (gamedir)
	
	return game
	
def loadgame():
	pass
	
def loadgamemenu(game):
	gm.gmenu(game)
