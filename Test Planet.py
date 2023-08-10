import Planet
import GameManager
import MapMaker

Name = 'Test Planet'
gname = "haa323"

game = GameManager.game(gname)

NewPlanet =  Planet.planet(Name, game)

game.properties['Explored Planets'].append(NewPlanet.properties)

game.savegamedata()

NewPlanet.saveplanet()

print (NewPlanet.properties)

MapMaker.plotcourse(game.properties['Current System'], game)