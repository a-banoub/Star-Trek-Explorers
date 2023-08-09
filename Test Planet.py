import Planet
import GameManager

Name = 'Test Planet'
gname = "FunkyTown"

game = GameManager.game(gname)

NewPlanet =  Planet.planet(Name, game)

game.properties['Explored Planets'].append(NewPlanet)

game.savegamedata()

print (NewPlanet.properties)

