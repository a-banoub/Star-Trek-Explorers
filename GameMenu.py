import GameManager
import Loader

class gmenu: 
				
	def __init__(self, game):
		
		def loadmenu(self):
			while self.quit == False: 
				UserInput = input('Prompt?: ')
				
				if UserInput == 'quit':
					self.quit = True
					
				if UserInput == 'status':
					print (game.properties)
				
								
		self.quit = False
		self.game = game
		
		loadmenu(self)
		