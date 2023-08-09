import uuid
import os
import shutil


GameStates = [
	'Downtime', 'On Duty', 'Away Mission'
]

class game ():
	def __init__(self, name):
		game = self
		self.properties = {
			'Campaign Name': name ,
			'ID' : str(uuid.uuid4()),
			'Characters': {
			},
			'Current System': 'Sol',
			'Ship' : None,
			'Captain' : None,
			'GameState' : GameStates [0],
			'Explored Planets' : []
		}
		
		def make_game_directory():
			dir = os.path.join('Games',self.properties['Campaign Name'])
			os.makedirs(dir)
			self.dir = dir
			return dir
		
		self.dir = make_game_directory()
		
		source_file = 'MapData.json'
		
		destination_file = os.path.join (self.dir, source_file)
		
		shutil.copy(source_file, destination_file)