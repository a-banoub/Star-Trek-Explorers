import CharacterSheet
from tkinter import *
from tkinter import ttk
import Archetypes
import PDFCreator

CharacterName = 'test'

PlayerCharacter = CharacterSheet.Character(CharacterName)	

PlayerCharacter.archetype = Archetypes.archetypes['The Outsider']
statblocks = Archetypes.archetypes['The Outsider']['StatBlocks']
PlayerCharacter.stats = statblocks[0]

#combo = PlayerCharacter.call_combobox_archetype_select(PlayerCharacter, "Choose Archetype", archetype_names)

print (PlayerCharacter.name)
print (PlayerCharacter.archetype)
print (PlayerCharacter.stats)


PlayerCharacter.save_character()
print ("PC Saved")

PDFCreator.mkpdf(PlayerCharacter)