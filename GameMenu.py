import GameManager
import Loader
import MapMaker


class gmenu: 
				
	def __init__(self, game):
		
		def loadmenu(self):
			while self.quit == False: 
			
				print ('Campaign Status: ', game.properties)
				
				UserInput = input('Game Menu (type help for options) Prompt? : ')
				
				if UserInput == 'quit':
					self.quit = True
				
				if UserInput == 'help':
					print ("'quit' will quit the program.")
					print ("'plotcourse' will search a sector and plot a course.")
				
				if UserInput == 'plotcourse':
					MapMaker.plotcourse(game.properties['Current System'], game)
#					Loader.savegame(game)
					
					
		self.quit = False
		self.game = game
		
		loadmenu(self)
		