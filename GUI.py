from tkinter import *
from tkinter import ttk
import CharacterSheet

	

class combobox(): 

	
	def __init__(self, title, values):
		self.root = Tk()
		self.root.title(title)
		self.root.geometry('300x300')
		self.combo = ttk.Combobox(self.root, values=values)
		self.combo.pack()
		self.values = values
		
		self.combo.bind("<<ComboboxSelected>>", self.option_selected)
		
	def option_selected (self, event): 
		archetype_name = self.combo.get()
		print (archetype_name)
			
	def call(self):	
		self.root.mainloop()

		