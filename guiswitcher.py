
class switcher():

    def switch_to_frame_0(self):
        from gui import gui
        global currentgui
        currentgui = gui(self)
        start = currentgui

    def switch_to_frame_1(self):
        from gui1 import gui
        global currentgui
        currentgui = gui(self)
        start = currentgui
   
    def switch_to_frame_2(self):
        from gui2 import gui
        global currentgui
        currentgui = gui(self)
        start = currentgui

    def __init__ (self):

        global currentgui
        currentgui = None

