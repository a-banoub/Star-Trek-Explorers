from tkinter import *
from tkinter import ttk
import CharacterSheet
	
class combobox(): 
	def __init__(self, title, values):
		self.root = Tk()
		self.root.title(title)
		self.root.geometry('300x300')
		self.combo = ttk.Combobox(self.root)
		self.combo.pack()
		self.values = values
		
	def option_selected (event): 
		archetype_name = combo.get()
		print (archetype_name)
	
	def call():	
		self.combo = ttk.Combobox(self.root, self.values)
		
		self.root.mainloop()
		