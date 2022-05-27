import tkinter
from tkinter import *
from turtle import right
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox

class FirstPage:
    def Ala_l(self):   
        # Create a photoimage object of the image in the path
        image1 = Image.open("Ala-Too_International_University_Seal.png")
        test = ImageTk.PhotoImage(image1)

        label1 = tkinter.Label(image=test)
        label1.image = test

        # Position image
        label1.place(x=70, y=70)
    
    def EXIT(self):

        root.destroy()
        

    def buttons(self):        

        B = tkinter.Button(root, text ="EXIT", command = FirstPage().EXIT )
        B.pack(side=BOTTOM)
        
        C = tkinter.Button(root, text ="TEST", command = SecondPage().Spage )
        C.pack(side=BOTTOM)
class SecondPage:
    def img():
        image1 = Image.open("Ala-Too_International_University_Seal.png")
        test = ImageTk.PhotoImage(image1)

        label1 = tkinter.Label(image=test)
        label1.image = test

        # Position image
        label1.place(x=70, y=70)

    def Spage(self):
        root = Tk()
        root.geometry("800x500")
        L = FirstPage().Ala_l()
        root.mainloop()
    def buttons(self):        

        B = tkinter.Button(root, text ="EXIT", command = FirstPage().EXIT )
        B.pack(side=BOTTOM)
        
        C = tkinter.Button(root, text ="TEST", command = SecondPage().Spage )
        C.pack(side=BOTTOM)

root = Tk()
root.geometry("400x600")
root.resizable(False, False)
T = FirstPage().Ala_l()
K = FirstPage().buttons()
root.mainloop()