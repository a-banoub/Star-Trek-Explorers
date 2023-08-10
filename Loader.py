import GameManager
import GameMenu as gm
import pickle
import os


gamelog = 'gamelog.json'

if os.path.exists('gamelog.pickle'):
	print ("File Exists")
	
	with open ('gamelog.pickle', 'rb') as file:
		gamedir = pickle.load (file)
		print (gamedir.keys())

else:
	print ("File does not Exist. Create a New Game to create directory.")
	gamedir = {}

def loadmainmenu():
	import MainMenu
	MainMenu.MainMenu()
	
	
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
	for index, (campaign, game_instance) in enumerate(gamedir.items()):
		print(f"{campaign} : {index}")
	
	userinput = input ('Enter index number to load game: ')
	

	userinput = int(userinput)  # Convert the user input to an integer
		
	if userinput in range(len(gamedir)):
		game = list(gamedir.values())[userinput]
		print('Loaded:', game.properties['Campaign Name'])
		game_menu = loadgamemenu(game)
				
def savegame(game):
	with open ('gamelog.pickle', 'wb') as file:
		gamedir [game.properties['Campaign Name']] = game 
		pickle.dump(gamedir, file)
		print ('File Updated')
		
def loadgamemenu(game):
	gm.gmenu(game)


	