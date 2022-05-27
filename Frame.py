from tkinter import *
import tkinter
from PIL import Image, ImageTk



#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("400x600")

#Create a frame
frame = Frame(win)
frame.pack(side="top", expand=True, fill="both")

class FirstPage:
    def Ala_l(self):
        clear_frame()   
        # Create a photoimage object of the image in the path
        image1 = Image.open("Ala-Too_International_University_Seal.png")
        test = ImageTk.PhotoImage(image1)

        label1 = tkinter.Label( image=test)
        label1.image = test

        # Position image
        label1.place(x=70, y=70)        

        B = tkinter.Button(frame, text ="EXIT", command = None )
        B.pack(side=BOTTOM)
        
        C = tkinter.Button(frame, text ="TEST", command = Spage().Labe )
        C.pack(side=BOTTOM)
#Create a text label
class Spage:
    def Labe(self):
        clear_frame()
        Label(frame,text="Enter the Password", font=('Helvetica',20)).pack(pady=20)
        Button(frame, text="Clear", font=('Helvetica bold', 10), command=
        FirstPage().Ala_l).pack(pady=20)
    
def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()
    
Spage().Labe()
#Create a button to close the window

win.mainloop()