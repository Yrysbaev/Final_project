from fileinput import filename
from tkinter import *
import tkinter
from token import RIGHTSHIFT
from turtle import bgcolor
from PIL import Image, ImageTk
from tkinter import filedialog as fd
import test1

win= Tk()
win.geometry("400x600")
win.resizable(False,False)
win.tk.call('wm', 'iconphoto', win._w, tkinter.PhotoImage(file='Icon.png'))

frame = Frame(win)
frame.pack(side="top", expand=True, fill="both")

class HomePage:
    def __init__(self):
        clear_frame()   
        self.Wel = Label(frame, text = "Welcome to My")
        self.Pho = Label(frame, text = "Photo Editor")
        self.Text()
        self.image1 = Image.open("Ala-Too_International_University_Seal.png")
        self.Ala_log()
        self.Exit = tkinter.Button(frame, text ="EXIT", command = self.quitwin )
        self.Spage = tkinter.Button(frame, text ="Python GUI", command = Spage().Labe )
        self.Second = tkinter.Button(frame, text ="White & Black", command = SecondPage )
        self.Buttons()
    def Text(self):
        self.Wel.config(font =("Courier", 14))  
        self.Wel.pack()
        self.Pho.config(font =("Courier", 14))  
        self.Pho.pack()

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

        self.Return = tkinter.Button(frame, text="Return to HomePage",command = HomePage)
        self.Save = tkinter.Button(frame, text="       Save       ",command = self.savefile)
        self.Choose = tkinter.Button(frame, text=" Choose ", command = self.Choose_file)
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
        self.Choose.pack(side=BOTTOM)

    def savefile(self):
        a = self.image1.filename = fd.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (('JPEG', ('*.jpg','*.jpeg','*.jpe','*.jfif')),('PNG', '*.png'),('BMP', ('*.bmp','*.jdib')),('GIF', '*.gif')))
        self.image1.save(a)
    
    def Choose_file(self):
        self.filename1 = fd.askopenfilename()
        self.image1 = Image.open(self.filename1)
        self.x = self.image1.height
        self.y = self.image1.width
        self.Image_set()
class Spage:
    def Labe(self):
        clear_frame()
        def clear_textbox():
            text_box.delete(1.0, 'end')
        message ='''
        Dear Reader,

            Don't let this situation
            blind your future. We at
            PythonGuides write tutorials
            with real life examples to 
            make you understand the 
            concept in best 
            possible way.

        Thanks & Regards,
        Team PythonGuides '''

        text_box = Text(
            frame,
            height=13,
            width=40
        )
        text_box.pack(expand=True)
        text_box.insert('end', message)

        Button(
            frame,
            text='Clear',
            width=15,
            height=2,
            command=clear_textbox
        ).pack(expand=True)
        self.B = Button(frame, text="Home Page", font=('Helvetica bold', 10), command=HomePage)
        self.B.pack(side=BOTTOM)
def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()

HomePage()

win.mainloop()