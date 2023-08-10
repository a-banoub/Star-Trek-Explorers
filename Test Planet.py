import Planet
import GameManager

Name = 'Test Planet'
gname = "FunkyTown34333"

game = GameManager.game(gname)

NewPlanet =  Planet.planet(Name, game)

game.properties['Explored Planets'].append(NewPlanet.properties)

game.savegamedata()

NewPlanet.saveplanet()

print (NewPlanet.properties)

