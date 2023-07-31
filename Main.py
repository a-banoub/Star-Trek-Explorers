import CharacterSheet
from tkinter import *
from tkinter import ttk


Alex = CharacterSheet.Character('Alex')
x = CharacterSheet.Character('Brian')

archetype_names = list(CharacterSheet.archetypes.keys())

combo = Alex.call_combobox_archetype_select("Test", archetype_names)

combo.call()

##x.stats = CharacterSheet.archetypes[archetype_names](0)
##Alex.stats = CharacterSheet.archetypes[archetype_names][1]

print (x.name)
print (x.stats)
print (Alex.name)
print (Alex.stats)

