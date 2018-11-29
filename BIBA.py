import sys
import os
import Tkinter as tk
from Tkinter import *
from PIL import ImageTk
import subprocess



splashroot = tk.Tk()
splashroot.title("BIBA")
width = splashroot.winfo_screenwidth()
height = splashroot.winfo_screenheight()

def openfile():
    splashroot.destroy()
    subprocess.call(["sudo","python","Biba_Learning.py"])
    #os.system('BIBA_Raspi.py')

splashroot.geometry('%sx%s' % (width, height))
splashroot.config(width = width,height= height,padx = 10,pady=10,bg='#50b3b5')
width = splashroot.winfo_screenwidth()
height = splashroot.winfo_screenheight()
splashroot.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))
image = ImageTk.PhotoImage(file = "Images/BIBAspalsh.jpg")
canvas = tk.Canvas(splashroot, height=height*0.8, width=width*0.8, bg="brown")
canvas.create_image(width*0.8/2, height*0.8/2, image=image)
Proceed = ImageTk.PhotoImage(file = "Images/btn.jpg")
Proceedbutton=Button(splashroot,image = Proceed,command = openfile)
Proceedbutton.place(relx=0.5, rely=0.7, anchor=CENTER)
Proceedbutton.config(bd=0, highlightthickness=0,borderwidth=0, relief=tk.SOLID)

canvas.pack()
splashroot.mainloop()
