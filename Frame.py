from fileinput import filename
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import filedialog as fd


#Create an instance of tkinter frame
win= Tk()
#Set the geometry of frame
win.geometry("400x600")
#Create a frame
win.tk.call('wm', 'iconphoto', win._w, tkinter.PhotoImage(file='Icon.png'))

frame = Frame(win)
frame.pack(side="top", expand=True, fill="both")

class HomePage:
    def Ala_l(self):
        clear_frame()   
        # Create a photoimage object of the image in the path
        image1 = Image.open("Ala-Too_International_University_Seal.png")
        test = ImageTk.PhotoImage(image1)

        label1 = tkinter.Label(frame, image=test)
        label1.image = test

        # Position image
        label1.place(x=70, y=70)        

        B = tkinter.Button(frame, text ="EXIT", command = quitwin )
        B.pack(side=BOTTOM)
        
        C = tkinter.Button(frame, text ="TEST", command = Spage().Labe )
        C.pack(side=BOTTOM,pady=5)
 

        Second = tkinter.Button(frame, text ="White & Black", command = SecondPage().all )
        Second.pack(side=BOTTOM)
class SecondPage:
    def __init__(self):
        pass 
    def normalize_size(self):
        pass 
    def all(self):
        clear_frame()
        filename1 = fd.askopenfilename()
        image1 = Image.open(filename1).convert("L")
        test = ImageTk.PhotoImage(image1)
        
        label1 = tkinter.Label(frame, image=test)
        label1.image = test

        # Position image
        label1.place(x=0, y=0)        

        tkinter.Button(frame, text="Return to HomePage",command = HomePage().Ala_l).pack(side=BOTTOM)
        tkinter.Button(frame, text="       Save       ",command = None).pack(side=BOTTOM)    
class Spage:
    def Labe(self):
        clear_frame()
        Label(frame,text="Enter the Password", font=('Helvetica',20)).pack(pady=20)
        Button(frame, text="Clear", font=('Helvetica bold', 10), command=
        HomePage().Ala_l).pack(pady=20)

def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()
def quitwin():
    win.quit()

HomePage().Ala_l()
#Create a button to close the window

win.mainloop()