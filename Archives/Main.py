import CharacterSheet
from tkinter import *
from tkinter import ttk
import Archetypes
import PDFCreator
import GameManager 
CharacterName = input("Character Name: ")

PlayerCharacter = CharacterSheet.Character(CharacterName)	
print (PlayerCharacter.name)

species = input ("Species Name: ")
PlayerCharacter.add_species (species)

archetype_names = list(Archetypes.archetypes.keys())
combo = PlayerCharacter.call_combobox_archetype_select(PlayerCharacter, "Choose Archetype", archetype_names)

print (PlayerCharacter.name)
print (PlayerCharacter.archetype)
print (PlayerCharacter.stats)


PlayerCharacter.save_character()
print ("PC Saved")

PDFCreator.mkpdf(PlayerCharacter)
