from tkinter import *
from tkinter import ttk
import CharacterSheet
import Archetypes


def confirm_archetype(self, archetype_name):
    self.pc.set_archetype(self.archetype_name)
    self.root.destroy()

class combobox(): 
    def __init__(self, pc, title, values):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('400x400')  # Increased the window size for better display
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Added padding and sticky
        self.frm.columnconfigure(0, weight=1)  # Allow column 0 to expand horizontally
        self.frm.columnconfigure(1, weight=1)  # Allow column 1 to expand horizontally
        self.frm.rowconfigure(1, weight=1)  # Allow row 1 to expand vertically

        self.description = Label(self.frm, wraplength=360, anchor="nw", justify="left")
        self.description.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2)  # Added padding and sticky, updated columnspan
        self.values = values
        self.pc = pc
        self.archetype_name = "None"
        self.archetype_description = "Click an Archetype to read more"
        self.combo = ttk.Combobox(self.frm, values=values)
        self.combo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")  # Added padding and sticky
        self.combo.bind("<<ComboboxSelected>>", self.option_selected)
        self.button1 = ttk.Button(self.frm, text="Confirm Archetype", command=lambda: confirm_archetype(self, self.archetype_name))
        self.button1.grid(row=0, column=1, padx=10, pady=10, sticky="e")  # Added padding and sticky

    def option_selected(self, event): 
        self.archetype_name = self.combo.get()
        self.archetype_description = Archetypes.archetypes[self.archetype_name]['Description']
        self.archetype_examples = Archetypes.archetypes[self.archetype_name]['Examples']

        for widget in self.frm.grid_slaves(row=2):
            widget.grid_forget()
            
        for index, example in enumerate(self.archetype_examples):
            example_label = Label(self.frm, wraplength=360, anchor="w", justify="left", text=example)
            example_label.grid(row=2, column=index, padx=5, pady=5, sticky="w")  # Added padding and sticky

        self.description.config(text=self.archetype_description)

    def call(self):    
        self.root.mainloop()
