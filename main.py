import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd

class HomePage:
    def Ala_logo(self):
        root = Tk()
        root.geometry("400x600")
        # Create a photoimage object of the image in the path
        image1 = Image.open("Ala-Too_International_University_Seal.png")
        test = ImageTk.PhotoImage(image1)

        label1 = tkinter.Label(image=test)
        label1.image = test

        # Position image
        label1.place(x=70, y=70)

        root.mainloop()    
class FirstPage:
    root = Tk()
    root.geometry("400x600")
    # Create a photoimage object of the image in the path
    image1 = Image.open("Ala-Too_International_University_Seal.png")
    test = ImageTk.PhotoImage(image1)

    label1 = tkinter.Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=70, y=70)

    root.mainloop()

Tj = HomePage()
