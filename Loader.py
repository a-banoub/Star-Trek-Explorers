import GameManager

gamelog = 'gamelog.json'

def newgame():
	gname = input("Campaign Name?")
	
	game = GameManager.game(gname)
	
	game.savegamedata()
	print (f'{gname} campaign saved')
	
def loadgame():
	pass