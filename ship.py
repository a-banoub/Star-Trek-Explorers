from enum import Enum

class ship (): 
    def __init__ (self, name) : 
        self.stats = {
            'Name' : name,
            'Cruising Speed' : 5,
            'Hull Damage Taken' : 0, 
            'Hull Damage Max' : 6,
        }

        self.systems = {
                    'Sheilds' : {
                        'Current Power' : 1 ,
                        'Max Power' : 1,
                        'Damage Reduction' : 1, 
                        'Description' : "When attacker harm meets but does not exceed shield DR roll Evasive Maneuvers",
                        'Status' : {
                            'Sheilds Up' : 1,
                            'Sheilds Down' : 2,
                        }
                    },

                'Weapons' : {
                        'Current Power' : 2,
                        'Max Power' : 2,
                        'Phasers' : {
                            'Power Requirement' : 1,
                            'Damage' : 1,
                            'Description' : ' Base harm 1 to hull (reduced by sheilds)',
                        }, 
                        'Photon Torpedos' : {
                            'Power Requirement' : 2,
                            'Damage' : 2, 
                            'Description' : 'Base 2 harm to hull (reduced by sheilds)',
                        }
                },
                'Transporters' : {
                    'Current Power' : 1,
                    'Max Power' : 1, 
                    'Description' : 'Cannot work while sheilds are up',
                },

                'Comms' : {
                    'Current Power' : 2,
                    'Max Power' : 2,
                    'Description' : 'Power requirement for short range: 1; Power requirement for long range: 2' 
                },
                'Warp Engines' : {
                    "Current Power" : 1, 
                    'Max Power' : 1, 
                    'Description' : 'For every warp factor above your cruising speed, roll 1 DG. On a 1-3, mark 1 warp system offline.',
                },
                "Impulse Power" : {
                    'Current Power' : 1,
                    'Max Power' : 1,
                },
                'Tractor Beam' : {
                    'Current Power' : 1,
                    'Max Power' : 1, 
                },
                'Sensors' : {
                    'Current Power' : 2,  
                    "Max Power" : 2, 
                    'Description' : "Power requirement for short range: 1; Power requirement for long range: 2",
                }, 
                'Holodecks' : {
                    "Current Power" : 1,
                    'Max Power' : 1,                    
                },
                'Replicators' : {
                    "Current Power" : 1,
                    "Max Power" : 1, 
                },
                'Life Support' : {
                    'Current Power' : 2,
                    'Max Power' : 2, 
                }
            }

test = ship ('whoop')

print (test.stats)
print (test.systems)