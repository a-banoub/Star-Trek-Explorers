import CharacterSheet
from tkinter import *
from tkinter import ttk


Alex = CharacterSheet.Character('Alex')
x = CharacterSheet.Character('Brian')

archetype_names = list(CharacterSheet.archetypes.keys())

Alex.call_combobox_archetype_select ("Choose an Archetype", archetype_names)

Alex.combobox.call

##x.stats = CharacterSheet.archetypes[archetype_names](0)
##Alex.stats = CharacterSheet.archetypes[archetype_names][1]

print (x.name)
print (x.stats)
print (Alex.name)
print (Alex.stats)

