from tkinter import *
from tkinter import ttk
from tkinter import _tkinter
import CharacterSheet
import Archetypes

def confirm_archetype (self, archetype_name):
	self.pc.set_archetype(self.archetype_name)
	self.root.destroy()
	self.pc.call_combobox_stat_select (self.pc, "Select StatBlock", self.archetype_name)
	
def confirm_statblock(self):
	print ('KEYS: ', self.statblock.keys())
	self.pc.set_stats (self.statblock)
	self.root.destroy()
	
	
class combobox () : 
	def __init__(self, pc, title, values):
		self.root = Tk()
		self.root.title (title)
		self.root.geometry ('400x400')
		self.frm = ttk.Frame (self.root, padding = 10)
		self.frm.grid()
		self.description = Label(self.frm, wraplength=280, anchor="nw", justify="left")
		self.description.grid(column = 0, row = 1)
		self.values = values
		self.pc = pc
		self.archetype_name = "None"
		self.archetype_description = "Click an Archetype to read more"
		self.combo = ttk.Combobox(self.frm, values=values)
		self.combo.grid (column = 0, row = 0)
		self.combo.bind ("<<ComboboxSelected>>", self.option_selected)
		
		self.button1 = ttk.Button(self.frm, text="Confirm Archetype", command= lambda: confirm_archetype(self,self.archetype_name))
		self.button1.grid (column = 1, row = 0)	
				
	def option_selected (self, event): 
		self.archetype_name = self.combo.get()
		self.archetype_description = Archetypes.archetypes[self.archetype_name]['Description']
		self.archetype_examples = Archetypes.archetypes[self.archetype_name]['Examples']
		
		for widget in self.frm.grid_slaves(row=2):
			widget.grid_forget()
			
		for index, example in enumerate(self.archetype_examples):
			example_label = Label(self.frm, justify="left", text=example)
			example_label.grid(column=index, row=2 )
			
		self.description.config(text= self.archetype_description)
		
	
	def call(self):	
		self.root.mainloop()

class combobox_1 () : 
	
	def __init__(self, pc, title, archetype):
		self.root = Tk()
		self.root.title (title)
		self.root.geometry ('400x400')
		self.frm = ttk.Frame (self.root, padding = 10)
		self.frm.grid()
		self.archetype_name = archetype
#		self.values = values
		self.pc = pc
		self.statblock = {}
		self.combo = ttk.Combobox(self.frm, values=Archetypes.archetypes[self.archetype_name]['StatBlocks'])
		self.combo.grid (column = 0, row = 0)
		self.combo.bind ("<<ComboboxSelected>>", self.option_selected)
		self.button1 = ttk.Button(self.frm, text="Confirm Statblock", command= lambda: confirm_statblock(self))
		self.button1.grid (column = 0, row = 1)	
		
	def option_selected (self, event): 
		
		index = self.combo.current()
		self.statblock = Archetypes.archetypes[self.archetype_name]['StatBlocks'][index]
		print (self.statblock)
		print (self.statblock)
		
	def call(self):	
		self.root.mainloop()