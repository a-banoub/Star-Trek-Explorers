import Planet
import GameManager
import MapMaker

Name = 'Test Planet'
gname = "33"

game = GameManager.game(gname)

NewPlanet =  Planet.planet(Name, game)

game.properties['Explored Planets'].append(NewPlanet.properties['name'])

game.savegamedata()

NewPlanet.saveplanet()

print (NewPlanet.properties)

quit = False

while quit == False: 
	MapMaker.plotcourse(game.properties['Current System'], game)
