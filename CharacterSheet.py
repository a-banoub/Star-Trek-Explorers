import GUI

archetypes = {'The Outsider':[
				{'Resourcefulness': 0, 'Tactics': 1, 'Logic': 2, 'Empathy': -1},
				{'Resourcefulness': 1, 'Tactics': 2, 'Logic': 1, 'Empathy': -2},
				{'Resourcefulness': 1, 'Tactics': 1, 'Logic': 0, 'Empathy': 0},
			], 
			'The Maverick':[
				{'Resourcefulness': 2, 'Tactics': 1, 'Logic': -2, 'Empathy': 1},
				{'Resourcefulness': 2, 'Tactics': 1, 'Logic': 1, 'Empathy': -2},
				{'Resourcefulness': 1, 'Tactics': 1, 'Logic': 0, 'Empathy': 0},
			],
			'The Idealist':[
				{'Resourcefulness': 1, 'Tactics': 2, 'Logic': 0, 'Empathy': 0},
				{'Resourcefulness': 1, 'Tactics': 0, 'Logic': 0, 'Empathy': 1},
				{'Resourcefulness': -1, 'Tactics': 2, 'Logic': 2, 'Empathy': -1},
]
	}

class Character: 
	def __init__(self,name):
		self.name = name
		self.stats = {
			'Resourcefulness': 0,
			'Tactics': 0,
			'Logic': 0, 
			'Empathy':0
		}
		
		self.expertise = []
		self.archetype = archetypes['The Maverick']
	
	def add_expertise (expertise_name):
		self.expertise = {expertise_name : 1}
		
	def call_combobox_archetype_select (self, title, values):
		self.combobox = GUI.combobox(title, values)
		self.combobox.call()