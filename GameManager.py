import uuid
import os
import shutil
import json

GameStates = [
	'Downtime', 'On Duty', 'Away Mission'
]

gamelog = 'gamelog.json'

class game ():
	def __init__(self, name):
		self.game = self
		self.properties = {
			'Campaign Name': name ,
			'ID' : str(uuid.uuid4()),
			'Characters': [],
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
		
		
		
		def copymapdata(): 
			source_file = 'MapData.json'
			destination_file = os.path.join (self.dir, source_file)
			shutil.copy(source_file, destination_file)
		
		self.dir = make_game_directory()
		copymapdata()
	
	def savegamedata(self):
		
		data = {
			'Campaign Name' : self.properties['Campaign Name'],
			'ID' : self.properties['ID'],
			'Characters' : self.properties['Characters'],
			'Current System': self.properties['Current System'],
			'Ship' : self.properties['Ship'],
			'Captain' : self.properties['Captain'],
			'GameState' : self.properties['GameState'],
			'Explored Planets' : self.properties['Explored Planets']
		}
		print (data)
		
		
		if os.path.isfile(gamelog):
			print ("File Exists")
			with open(gamelog, "r") as file:
				file_content = file.read()
			
				game_data = json.loads(file_content)
				index_to_replace = None
				
				for i, existing_data in enumerate(game_data):
					if existing_data['ID'] == data['ID']:
						index_to_replace = i
						break
				
				if index_to_replace is not None:
					game_data[index_to_replace] = data
				
				else:
					game_data.append(data)
					
				with open(gamelog, "w") as file:
					json.dump(game_data, file)
							
#			except json.JSONDecodeError:
#				game_data = [data]
#				with open(gamelog, "w") as file:
#					json.dump(game_data, file)
		
		else:
			game_data = [data]
			with open(gamelog, "w") as file:
				json.dump(game_data, file)

					