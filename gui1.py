
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer



class gui: 
    

    
    def button_1_clicked (self):
        self.window.destroy(),

    def __init__(self, switcher) :
        from pathlib import Path
        # from tkinter import *
        # Explicit imports to satisfy Flake8
        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
        import sys    
        self.window = Tk()
        self.window.geometry("1440x1024")
        self.window.configure(bg = "#000000")
        self.switcher = switcher

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alexa\OneDrive\Desktop\Star Trek Explorers\Star-Trek-Explorers\build\assets\frame1")

        def relative_to_assets(path: str) -> Path:
             return ASSETS_PATH / Path(path)
             print (sys.path)

        canvas = Canvas(
            self.window,
            bg = "#000000",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            719.0,
            492.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=111.0,
            y=339.0,
            width=252.0,
            height=96.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=363.0,
            y=512.0,
            width=252.0,
            height=96.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=719.0,
            y=714.0,
            width=252.0,
            height=96.0
        )
        self.window.resizable(False, False)
        self.window.mainloop()