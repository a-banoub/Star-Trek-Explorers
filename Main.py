import CharacterSheet
from tkinter import *
from tkinter import ttk
import Archetypes

CharacterName = input("Character Name: ")

PlayerCharacter = CharacterSheet.Character(CharacterName)	
print (PlayerCharacter.name)

archetype_names = list(Archetypes.archetypes.keys())
combo = PlayerCharacter.call_combobox_archetype_select(PlayerCharacter, "Choose Archetype", archetype_names)


print (PlayerCharacter.name)
print (PlayerCharacter.archetype)
print (PlayerCharacter.stats)
