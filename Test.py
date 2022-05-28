from fileinput import filename
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import filedialog as fd
import test1

win= Tk()
win.geometry("400x600")
win.tk.call('wm', 'iconphoto', win._w, tkinter.PhotoImage(file='Icon.png'))

frame = Frame(win)
frame.pack(side="top", expand=True, fill="both")

class HomePage:
    def __init__(self):
        clear_frame()   
        # Create a photoimage object of the image in the path
        self.image1 = Image.open("Ala-Too_International_University_Seal.png")
        self.Ala_log()
        self.Exit = tkinter.Button(frame, text ="EXIT", command = self.quitwin )
        self.Spage = tkinter.Button(frame, text ="TEST", command = Spage().Labe )
        self.Second = tkinter.Button(frame, text ="White & Black", command = SecondPage )
        self.Buttons()
    
    def Buttons(self):
        self.Exit.pack(side=BOTTOM,pady=5)
        self.Spage.pack(side=BOTTOM,pady=5)
        self.Second.pack(side=BOTTOM,pady=5)

    def Ala_log(self):
        self.test = ImageTk.PhotoImage(self.image1)    
        self.label1 = tkinter.Label(frame, image=self.test)
        self.label1.image = self.test
        self.label1.place(x=70, y=70)        

    def quitwin(self):
        win.quit()
class SecondPage:
    def __init__(self):
        clear_frame()
        self.filename1 = fd.askopenfilename()
        self.image1 = Image.open(self.filename1)
        self.norm = 0
        self.x = self.image1.height
        self.y = self.image1.width
        self.Image_set()
        self.Return = tkinter.Button(frame, text="Return to HomePage",command = HomePage)
        self.Save = tkinter.Button(frame, text="       Save       ",command = None)
        self.Buttons() 
    def normalize_size(self):
        while self.x > 400 or self.y > 500:
            self.x /= 2
            self.y /= 2
    def Image_set(self):
        if self.x > 600 and self.y > 400:
            self.normalize_size()
        self.image1 = Image.open(self.filename1).convert("L").resize((int(self.y),int(self.x)))
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = tkinter.Label(frame, image=self.test)
        self.label1.image = self.test
        self.label1.place(x=0, y=0)        
    def Buttons(self):
        self.Return.pack(side=BOTTOM)
        self.Save.pack(side=BOTTOM)
class Spage:
    def Labe(self):
        clear_frame()
        Label(frame,text="Enter the Password", font=('Helvetica',20)).pack(pady=20)
        Button(frame, text="Clear", font=('Helvetica bold', 10), command=
        HomePage().Ala_l).pack(pady=20)

def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()

HomePage()
test1.Yrysbaev_Maksatbek()
#Create a button to close the window

win.mainloop()