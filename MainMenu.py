import Loader
quit = False

while quit == False:

	userinput = input ("Prompt? (type 'help' for more options): ")

	if userinput == 'quit':
		quit = True

	if userinput == 'help':
		print ('Commands: ')
		print ("'newgame': Creates a New Campaign")
		print ("'loadgame': Loads an Existing Campaign")
		print ('quit: Quits the program')
		
	if userinput == 'newgame':
		game = Loader.newgame()
		quit = True
		Loader.loadgamemenu(game)
		
	if userinput == 'loadgame':
		game = Loader.loadgame()
		quit = True
#		Loader.loadgamemenu(game)
		
	else: 
		pass