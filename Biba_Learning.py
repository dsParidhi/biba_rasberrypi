import Tkinter
import Tkinter as tk
from Tkinter import *
from PIL import ImageTk
from tkColorChooser import askcolor
from tkColorChooser import askcolor
from ScrolledText import *
import tkMessageBox
import ttk
import time
import datetime

root = Tkinter.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.title("BIBA")
root.geometry('%sx%s' % (width, height))
root.config(width = width,height= height,padx = 10,pady=10,bg='#50b3b5')

Tops = Frame(root, bg="#50b3b5",pady = 2)
Tops.grid(row=0,column=1,columnspan = 6,sticky=W+E+N+S)

canvasleftheoight = (height*70)/100
canvasleftwidth = (width*70)/100
canvasrightwidth = (width*30)/100

canvaswidth = (canvasleftwidth*45)/100

canvas1height = (canvasleftheoight*65)/100
canvas2height = (canvasleftheoight*28)/100

canvasfucnwidth = (canvasleftwidth*60)/100
canvasfucnDetailwidth = (canvasleftwidth*40)/100

canvasright = Canvas(root,bg="#47a3a5")
canvasright.grid(row=1,column=1,rowspan=6,sticky=W+E+N+S,padx=10,pady=0)
canvasright.config(width=canvasrightwidth, height=canvasleftheoight,bd=0,highlightthickness=0)

class AutoScrollbar(Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):

        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        raise TclError, "cannot use pack with this widget"
    def place(self, **kw):
        raise TclError, "cannot use place with this widget"

canvasleft = Canvas(root)
canvasleft.grid(row=1,column=2,rowspan=6,sticky=tk.NW,padx=0,pady=0)
image = ImageTk.PhotoImage(file = "Images/homebg.jpg")
canvasleft.create_image(0,0, image = image,anchor = NW)
canvasleft.config(width=canvasleftwidth, height=canvasleftheoight,bd=0,highlightthickness=0,bg="white")
vscrollbar = AutoScrollbar(canvasleft,borderwidth=0)
vscrollbar.grid(row=1, column=3,rowspan= 100 ,padx=0,pady=5,sticky ='ns')
canvasf = Canvas(canvasleft,yscrollcommand=vscrollbar.set,bg="white")
canvasf.grid(row = 0, column = 0,rowspan= 20 ,padx=5,pady=10,sticky = 'n')
canvasf.config(width=canvasfucnwidth,height=canvasleftheoight+50)
vscrollbar.config(command=canvasf.yview)
canvasfunc = Canvas(canvasf,bd=0,highlightthickness = 0,bg="white")
image = ImageTk.PhotoImage(file = "Images/homebg.jpg")
canvasfunc.create_image(0,0,image = image)
canvasfunc.grid(row = 1, column = 2,rowspan=5000,padx=5,pady=10,sticky ='n')
canvasfunc.config(width=canvasfucnwidth, height=3000)
rowCount = canvasfunc.grid_size()[0]
colCount = canvasfunc.grid_size()[1]
canvasf.create_window(20, 0, anchor=N, window=canvasfunc)
canvasfunc.update_idletasks()

canvasf.config(scrollregion=canvasf.bbox("all"))
canvas = Canvas(canvasleft,bg="white",highlightbackground="grey",highlightthickness=1, highlightcolor="black")
canvas.grid(row=1,column=5,padx=10,pady=10,sticky=tk.NW)
canvas.config(width=canvasfucnDetailwidth, height=canvas1height)
#x-axis
canvas.create_line(0,1,canvasfucnwidth,1, width=0)
#y-axis
canvas.create_line(1,canvas1height,1,0,  width=1)

for i in range(100):
    x = 20 + (i * 5)
    y = 15 + (i * 25)
    h = canvas1height


    canvas.create_line(x,6,x,2, width=1)
    canvas.create_line(y,2,y,6, width=2)
    #canvas.create_text(x,330, text='%d'% (20*i), anchor=N)

    # markings on y axis
for i in range(100):
    y = 5 + (i * 5)
    x = 15 + (i * 25)
    canvas.create_line(3,y,7,y, width=1)
    canvas.create_line(3,x,9,x, width=2)

h = canvas1height
htext1 = h*4.5/100
canvas.create_text(h*4/100,12, text=0)
canvas.create_text(htext1+2,h-8, text=canvas1height)
canvas.create_text(canvasfucnDetailwidth-12,12, text=canvasfucnDetailwidth)
canvas1 = Canvas(canvasleft, bg="white",bd=2,highlightbackground="grey",highlightthickness=1, highlightcolor="black")
canvas1.grid(row = 3, column =5,padx=10, pady=2,sticky = tk.NW)
canvas1.config(width=canvasfucnDetailwidth, height=canvas2height)
lblinfo =   Label(Tops,font=('arial',20), text = 'BIBA Learning',bg = '#50b3b5',fg = 'White',anchor='w')
lblinfo.grid(row=0,column=0)

var = StringVar(canvasfunc)
var.set("Select Type")

message = tk.StringVar()
l1message = tk.StringVar()
messagesq = tk.StringVar()
messagerec = tk.StringVar()
messagecir = tk.StringVar()
messageline = tk.StringVar()
messageloop = tk.StringVar()
messageinitialvalue = tk.StringVar()
messagefinalvalue = tk.StringVar()
amessage = tk.StringVar()
bmessage = tk.StringVar()
ifmessage = tk.StringVar()
Elsemes = tk.StringVar()
Elsemessage = Label(canvasfunc)
Printlabel1 = Label(canvasfunc)
Printlabel2 = Label(canvasfunc)
printmess = tk.StringVar()
Print1mess = tk.StringVar()
Print2mess = tk.StringVar()
nestedifmessage = tk.StringVar()
nestedelsemessage = tk.StringVar()
elsemess = tk.StringVar()
switchmessage = tk.StringVar()
bgmessage = tk.StringVar()
textcolormessage = tk.StringVar()
textypemessage = tk.StringVar()
l4message = tk.StringVar()
l5message = tk.StringVar()
printswitchmess1 = tk.StringVar()
printswitchmess2 = tk.StringVar()
printswitchmess3 = tk.StringVar()
printswitchmess4 = tk.StringVar()
printswitchmess5 = tk.StringVar()
printswitchmess6 = tk.StringVar()
valAmess = tk.StringVar()
valBmess = tk.StringVar()
valCmess = tk.StringVar()
lbl_ValA = Label(canvasfunc)
lbl_ValB =Label(canvasfunc)
lbl_ValC =Label(canvasfunc)
Entr_ValA = Entry(canvasfunc)
Entr_ValA1 = Entry(canvasfunc)
Entr_ValB = Entry(canvasfunc)
Entr_ValC = Entry(canvasfunc)
elseifmess = tk.StringVar()
ifmess = tk.StringVar()
elifmess = tk.StringVar()
elsemess = tk.StringVar()
Printmess1 = tk.StringVar()
messageprintfor = tk.StringVar()
nestedifprint1 = tk.StringVar()
elmess = tk.StringVar()
nestediflbl1mess = tk.StringVar()
otherText = Entry(canvasfunc)
PrintText2 = Entry(canvasfunc)
PrintText1 = Entry(canvasfunc)
lbl_If = Label(canvasfunc)
Executenestif = Button(canvasfunc)
Executeif = Button(canvasfunc)
cancelfor = Button(canvasfunc)
Executenested = Button(canvasfunc)
cancelnestedif = Button(canvasfunc)
############################# Definations of widgets #################################################
Sqaure = Button( text ="Sqaure")
Circle = Button( text ="Circle")
Line = Button(text='Line')
Polygon = Button(text='Polygon')
E1 = Entry(canvasfunc)
E2 = Entry(canvasfunc)
E3 = Entry(canvasfunc)
E4 = Entry(canvasfunc)
label = Label(canvasfunc)
labelrec = Label(canvasfunc)
x = StringVar()
labelline = Label(canvasfunc)
Proceed = Button()
Proceedfor = Button(canvasfunc)
textlabel = Label(canvasfunc)
textentry = Entry(canvasfunc)
colorentry = Entry(canvasfunc)
labeltext = Label(canvasfunc)
entrytext = Entry(canvasfunc)
entrytype = Entry(canvasfunc)
itext = Entry(canvasfunc)
jtext = Entry(canvasfunc)
forlabel = Label(canvasfunc)
forinitiallabel = Label(canvasfunc)
forfinallabel = Label(canvasfunc)
outputtext = Text(canvasfunc)
output = Text(canvasfunc)
aText = Entry(canvasfunc)
bText = Entry(canvasfunc)
aLabel = Label(canvasfunc)
bLabel = Label(canvasfunc)
numlabel = Label(canvasfunc)
numlabelB = Label(canvasfunc)
numText = Entry(canvasfunc)
numText1 = Entry(canvasfunc)
numText2 = Entry(canvasfunc)
numText3 = Entry(canvasfunc)
numVal5 = Entry(canvasfunc)
numVal4 = Entry(canvasfunc)
l1 = Label(canvasfunc)
l2 = Label(canvasfunc)
l3 = Label(canvasfunc)
l4 = Label(canvasfunc)
l5 = Label(canvasfunc)
l6 = Label(canvasfunc)
o1 = Label(canvasfunc)
o2 = Label(canvasfunc)
o3 = Label(canvasfunc)
o4 = Label(canvasfunc)
o5 = Label(canvasfunc)
o6 = Label(canvasfunc)
l7 = Label(canvasfunc)
l8= Label(canvasfunc)
l9 = Label(canvasfunc)
l10 = Label(canvasfunc)
l11 = Label(canvasfunc)
l12 = Label(canvasfunc)
Proceedrec = Button(canvasfunc)
Proceedsq = Button(canvasfunc)
Proceedcir = Button(canvasfunc)
Proceedline = Button(canvasfunc)
Proceedtext = Button(canvasfunc)
Proceed = Button(canvasfunc)
Proceedtype = Button(canvasfunc)
switchlabel = Label(canvasfunc)
o1nestedif = Label(canvasfunc)
o6nestedif = Label(canvasfunc)
l1nestedif = Label(canvasfunc)
l2nestedif = Label(canvasfunc)
l3nestedif = Label(canvasfunc)
l4nestedif = Label(canvasfunc)
l5nestedif = Label(canvasfunc)
l6nestedif = Label(canvasfunc)
l1ifelse = Label(canvasfunc)
l3ifelse = Label(canvasfunc)
l4ifelse = Label(canvasfunc)
l5ifelse = Label(canvasfunc)
o1ifelse = Label(canvasfunc)
o4nestedif = Label(canvasfunc)
X1rec = Entry(canvasfunc)
X2rec = Entry(canvasfunc)
X3rec = Entry(canvasfunc)
X4rec =Entry(canvasfunc)
X1cir = Entry(canvasfunc)
X2cir = Entry(canvasfunc)
Rcir = Entry(canvasfunc)
X1line = Entry(canvasfunc)
X2line = Entry(canvasfunc)
X3line = Entry(canvasfunc)
X4line = Entry(canvasfunc)
X1sq = Entry(canvasfunc)
Ysq = Entry(canvasfunc)
Zsq = Entry(canvasfunc)
squarelabel = Label(canvasfunc)
T = Text(canvas1)
outputtext = ScrolledText(canvas1)
iflabel = Label(canvasfunc)
val1 = Label(canvasfunc)
val2 = Label(canvasfunc)
Print1 = Label(canvasfunc)
Print2 = Label(canvasfunc)
Print1mess = tk.StringVar()
cancelif = Button(canvasfunc)
proceedswitch = Button(canvasfunc)
switchVal1 = Entry(canvasfunc)
switchVal2 = Entry(canvasfunc)
Printswitch1 = Label(canvasfunc)
Printswitch2 = Label(canvasfunc)
Printswitch3 = Label(canvasfunc)
Printswitch4 = Label(canvasfunc)
Printswitch5 = Label(canvasfunc)
Printswitch6 = Label(canvasfunc)
Printlabel1 = Label(canvasfunc)
Printlabel2 = Label(canvasfunc)
Printlabel3 = Label(canvasfunc)
Printlabel4 = Label(canvasfunc)
Printlabel5 = Label(canvasfunc)
Printlabel6 = Label(canvasfunc)
PrintforloopPrintforloop = Label(canvasfunc)
cancelfor = Button(canvasfunc)
Proceedexe = Button(canvasfunc)
Proceedif = Button(canvasfunc)
varvalnew = StringVar(canvasfunc)
Printforloop = Label(canvasfunc)
varvalnew.set("Select Option")
casemess1 = StringVar(canvasfunc)
casemess2 = StringVar(canvasfunc)
casemess3 = StringVar(canvasfunc)
casemess4 = StringVar(canvasfunc)
printmess = StringVar(canvasfunc)
brkmess = StringVar(canvasfunc)
defaultmess = StringVar(canvasfunc)
caselabel = Label(canvasfunc,width = 10)
printlabel = Label(canvasfunc,width = 10)
printlabel1 = Label(canvasfunc,width = 10)
printlabel2 = Label(canvasfunc,width = 10)
printlabel3 = Label(canvasfunc,width = 10)
printlabel4 = Label(canvasfunc,width = 10)
case1text = Entry(canvasfunc)
breaklabel = Label(canvasfunc,width = 10)
breaklabel1 = Label(canvasfunc,width = 10)
breaklabel2 = Label(canvasfunc,width = 10)
breaklabel3 = Label(canvasfunc,width = 10)
breaklabel4 = Label(canvasfunc,width=10)
defaultlabel = Label(canvasfunc,width = 10)
defaultlabel2 = Label(canvasfunc,width = 10)
defaultlabel1 = Label(canvasfunc,width = 10)
defaultlabel3 = Label(canvasfunc,width = 10)
defaultlabel4 = Label(canvasfunc,width = 10)
dfeaultprintlabel5 = Label(canvasfunc,width = 10)
dfeaultprintlabel4 = Label(canvasfunc,width = 10)
dfeaultprintlabel3 = Label(canvasfunc,width = 10)
dfeaultprintlabel2 = Label(canvasfunc,width = 10)
dfeaultprintlabel1 = Label(canvasfunc,width = 10)
caselabel1 = Label(canvasfunc,width=10)
caselabel3 = Label(canvasfunc,width=10)
caselabel2 = Label(canvasfunc,width=10)
caselabel4 = Label(canvasfunc,width=10)
casemess5  = StringVar(canvasfunc)
casemess6  = StringVar(canvasfunc)
casemess7  = StringVar(canvasfunc)
casemess8  = StringVar(canvasfunc)
casemess9  = StringVar(canvasfunc)
casemess10  = StringVar(canvasfunc)
printlabel5 = Label(canvasfunc,width=10)
case7text = Entry(canvasfunc)
breaklabel5 = Label(canvasfunc,width=10)
defaultlabel5 = Label(canvasfunc,width=10)
dfeaultprintlabel5 = Label(canvasfunc,width=10)
dfeaultprintlabel4 = Label(canvasfunc,width=10)
dfeaultprintlabel3 = Label(canvasfunc,width=10)
dfeaultprintlabel2 = Label(canvasfunc,width=10)
breaklabel6 =  Label(canvasfunc,width=10)
defaultlabel6  =  Label(canvasfunc,width=10)
breaklabel7 =  Label(canvasfunc,width=10)
breaklabel8 =  Label(canvasfunc,width=10)
breaklabel9 =  Label(canvasfunc,width=10)
breaklabel10 =  Label(canvasfunc,width=10)
defaultlabel7  =  Label(canvasfunc,width=10)
dfeaultprintlabel6  =  Label(canvasfunc,width=10)
dfeaultprintlabel7  =  Label(canvasfunc,width=10)
defaultlabel8  =  Label(canvasfunc,width=10)
dfeaultprintlabel8  =  Label(canvasfunc,width=10)
defaultlabel9  =  Label(canvasfunc,width=10)
dfeaultprintlabel9  =  Label(canvasfunc,width=10)
defaultlabel10  =  Label(canvasfunc,width=10)
dfeaultprintlabel10  =  Label(canvasfunc,width=10)
defaultlabel11  =  Label(canvasfunc,width=10)
dfeaultprintlabel11  =  Label(canvasfunc,width=10)
defaulttext6 = Entry(canvasfunc)
defaulttext7 = Entry(canvasfunc)
defaulttext8 = Entry(canvasfunc)
defaulttext9 = Entry(canvasfunc)
defaulttext10 = Entry(canvasfunc)
defaulttext11 = Entry(canvasfunc)
printlabel4 = Label(canvasfunc,width=10)
case2text = Entry(canvasfunc)
case3text = Entry(canvasfunc)
case4text = Entry(canvasfunc)
case5text = Entry(canvasfunc)
case6text = Entry(canvasfunc)
defaulttext1 = Entry(canvasfunc)
defaulttext2 = Entry(canvasfunc)
defaulttext3 = Entry(canvasfunc)
defaulttext4 = Entry(canvasfunc)
defaulttext5 = Entry(canvasfunc)
cancelswitch = Button(canvasfunc)
lbl_If = Label(canvasfunc,width=5)
Entr_ValA = Entry(canvasfunc)
Entr_ValB = Entry(canvasfunc)
nestPrintlbl1 = Label(canvasfunc,width=10)
resultif = Entry(canvasfunc)
lbl_elIf = Label(canvasfunc,width=10)
Entr_ValA = Entry(canvasfunc)
Entr_ValC = Entry(canvasfunc)
nestPrintlbl2 = Label(canvasfunc,width=10)
nestPrintlbldefault = Label(canvasfunc,width=10)
resultelseif = Entry(canvasfunc)
lbl_el = Label(canvasfunc,width=5)
resultelse = Entry(canvasfunc)
Executeswitch = Button(canvasfunc)
cancelnestedif = Button(canvasfunc)
drop_menuoptncase2 = OptionMenu(canvasfunc,varvalnew,())
varval = StringVar(canvasfunc)
varval.set("Select Option")
drop_menuoptncase1 = OptionMenu(canvasfunc,varval,())
varnestif = StringVar(canvasfunc)
varnestif.set("Select Option")
drop_menuifcase1 = OptionMenu(canvasfunc,varnestif,())
nestediflblprint1 = Label(canvasfunc)
Proceedex2 = Button(canvasfunc)
nestediflbl1 = Label(canvasfunc)
Printlabel =  Label(canvasfunc,width = 5)
Printlabel1 =  Label(canvasfunc,width = 5)
Print1 = Label(canvasfunc,width = 20)
Print2 = Label(canvasfunc,width = 20)
lbl_elIf = Label(canvasfunc,width=5)
lbl_If = Label(canvasfunc,width=5)
scrollwidth = canvasfucnDetailwidth*12/100
outputtext = ScrolledText(canvas1,height=12, width=scrollwidth+2)
outputtext.grid(row =0, column=1,padx=0,pady=(0,2))
Printswitch1 = Label(canvasfunc,width = 20)
Printswitch2 = Label(canvasfunc,width = 20)
Printswitch3 = Label(canvasfunc,width = 20)
Printswitch4 = Label(canvasfunc,width = 20)
Printswitch5 = Label(canvasfunc,width = 20)
Printswitch6 = Label(canvasfunc,width = 20)
breaklabel5 =  Label(canvasfunc,width = 10)
caselabel5 = Label(canvasfunc,width=10)
printlabel6 = Label(canvasfunc,width=10)
breaklabel6 =  Label(canvasfunc,width = 10)
caselabel6 = Label(canvasfunc,width=10)
caselabel7 = Label(canvasfunc,width=10)
caselabel8 = Label(canvasfunc,width=10)
caselabel9 = Label(canvasfunc,width=10)
caselabel10 = Label(canvasfunc,width=10)
printlabel7 = Label(canvasfunc,width=10)
printlabel8 = Label(canvasfunc,width=10)
printlabel9 = Label(canvasfunc,width=10)
printlabel10 = Label(canvasfunc,width=10)
case8text = Entry(canvasfunc)
case9text = Entry(canvasfunc)
case10text = Entry(canvasfunc)
case11text = Entry(canvasfunc)
case12text = Entry(canvasfunc)
elifmess1 = StringVar(canvasfunc)
lbl_elIf1 =Label(canvasfunc)
Entr_ValA2 = Entry(canvasfunc)
nestPrintlbl3 = Label(canvasfunc,width=10)
resultelseif1 = Entry(canvasfunc)
lbl_el1 =  Label(canvasfunc)
nestPrintlbldefault1 = Label(canvasfunc,width=10)
resultelse1 = Entry(canvasfunc)
elifmess2 = StringVar(canvasfunc)
lbl_elIf2 =Label(canvasfunc)
Entr_ValA3= Entry(canvasfunc)
Entr_ValE= Entry(canvasfunc)
nestPrintlbl4 = Label(canvasfunc,width=10)
Printmess2 = StringVar(canvasfunc)
resultelseif2 = Entry(canvasfunc)
lbl_el2 = Label(canvasfunc)
nestPrintlbldefault2 = Label(canvasfunc,width=10)
resultelse2 = Entry(canvasfunc,width=10)
Printmess3 = StringVar(canvasfunc)
elifmess3 = StringVar(canvasfunc)
lbl_elIf3 = Label(canvasfunc)
Entr_ValA4  = Entry(canvasfunc)
Entr_ValF  = Entry(canvasfunc)
nestPrintlbl5 = Label(canvasfunc,width=10)
resultelseif3  = Entry(canvasfunc)
lbl_el3 = Label(canvasfunc)
nestPrintlbldefault3 = Label(canvasfunc,width=10)
resultelse3 = Entry(canvasfunc)
Printmess4  =StringVar(canvasfunc)
elifmess4 = StringVar(canvasfunc)
lbl_elIf4 = Label(canvasfunc)
Entr_ValA5  = Entry(canvasfunc)
Entr_ValG  = Entry(canvasfunc)
Printmess5  = StringVar(canvasfunc)
nestPrintlbl6 = Label(canvasfunc,width=10)
resultelseif4 = Entry(canvasfunc)
lbl_el4 = Label(canvasfunc)
nestPrintlbldefault4 = Label(canvasfunc,width=10)
resultelse4 = Entry(canvasfunc)
Entr_ValD = Entry(canvasfunc)
Entr_ValF = Entry(canvasfunc)
Entr_ValG = Entry(canvasfunc)
def populate_menu(optionmenu, **cmds):
    menu = optionmenu['menu']
    menu.delete(0, "end")
    for name, func in cmds.items():
        menu.add_command(label=name, command=
                         lambda name=name, func=func: func(name))
drop_menutext = OptionMenu(canvasfunc,var,())
drop_menuifelse = OptionMenu(canvasfunc,var,())
drop_menuswitch = OptionMenu(canvasfunc,var,())
drop_menutexttype = OptionMenu(canvasfunc,var,())
hidden=0
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

clearimage = tk.PhotoImage(file = "Images/resendicon.gif")
clearlogimage = tk.PhotoImage(file = "Images/clear_icon.gif")

#################################### Error message Popup function #####################################################
def hidden():
    drop_menutext.grid_remove()
def hello():
   tkMessageBox.showwarning("Error", "No. of Value is greater than input value")
def Rectangleerror():
   tkMessageBox.showinfo("Error", "Write accurate values")
def emptyfields():
    tkMessageBox.showwarning("Error", "TextField should not be empty")
    tkMessageBox.resizable(0,0)
def InvalidOperator():
     tkMessageBox.showwarning("Error", " One Number Should be smaller or greater than other or else choose appropriate operator ")
def InvalidInput():
     tkMessageBox.showwarning("Error", "Number You Entered is Not Whole Number")
def ForInvalidInput():
    tkMessageBox.showwarning("Error", "Please Enter Int value")
def InvalidSelection():
     tkMessageBox.showwarning("Error", "Please select Valid Option")
def differentvalerror():
     tkMessageBox.showwarning("Error", "Please select Different Option")
def validevalue():
    tkMessageBox.showwarning("Error", "values should not be greater than canvas scale height")
def shapesfeildsempty():
    tkMessageBox.showwarning("Error", "Text feild is empty or Option value is not selected")
cancel =  Button(text = " cancel")
close = ImageTk.PhotoImage(file = "Images/close.jpg")
class Placeholder_State(object):
     __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'

def add_placeholder_to(entry, placeholder, color="Black", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")

    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color=normal_color
    state.normal_font=normal_font
    state.placeholder_color=color
    state.placeholder_font=font
    state.placeholder_text = placeholder
    state.with_placeholder=True

    def on_focusin(event, entry=entry, state=state):
        if state.with_placeholder:
            entry.delete(0, "end")
            entry.config(fg = state.normal_color, font=state.normal_font)

            state.with_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg = state.placeholder_color, font=state.placeholder_font)

            state.with_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg = color, font=font)

    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")

    entry.placeholder_state = state

    return state


def clear_all():
    for item in canvasfunc.grid_slaves():
        item.grid_forget()

construct = 0

sv = StringVar(canvasfunc)
OPTIONS = ["*","+","-","/"]
sv.set(OPTIONS[0] )
omfor = OptionMenu( canvasfunc, sv,*OPTIONS)
sv = StringVar(canvasfunc)
OPTIONSIF = ["Operators","<",">","==","<=",">="]
sv.set(OPTIONSIF[0] )
omif = OptionMenu( canvasfunc, sv,*OPTIONSIF)
sv = StringVar(canvasfunc)
sv1 = StringVar()
OPTIONSNESTEDIF = ["Operators","<",">","==","<=",">="]
sv.set(OPTIONSNESTEDIF[0] )
sv1.set(OPTIONSNESTEDIF[0] )
omnestedif = OptionMenu( canvasfunc, sv,*OPTIONSNESTEDIF)
omnestedif1 = OptionMenu( canvasfunc, sv1,*OPTIONSNESTEDIF)


svnestif = StringVar(canvasfunc)
svnestif.set(OPTIONSNESTEDIF[0] )
svnestif1 = StringVar(canvasfunc)
svnestif1.set(OPTIONSNESTEDIF[0] )
svnestif2 = StringVar(canvasfunc)
svnestif2.set(OPTIONSNESTEDIF[0] )
svnestif3 = StringVar(canvasfunc)
svnestif3.set(OPTIONSNESTEDIF[0] )
svnestif4 = StringVar(canvasfunc)
svnestif4.set(OPTIONSNESTEDIF[0] )
svnestif5 = StringVar(canvasfunc)
svnestif5.set(OPTIONSNESTEDIF[0] )
omnestedif = OptionMenu( canvasfunc, svnestif,*OPTIONSNESTEDIF)
omnestedif1 = OptionMenu( canvasfunc, svnestif1, *OPTIONSNESTEDIF)
omnestedif2 = OptionMenu( canvasfunc, svnestif2,*OPTIONSNESTEDIF)
omnestedif3 = OptionMenu( canvasfunc, svnestif3,*OPTIONSNESTEDIF)
omnestedif4 = OptionMenu( canvasfunc, svnestif4,*OPTIONSNESTEDIF)
omnestedif5 = OptionMenu( canvasfunc, svnestif5,*OPTIONSNESTEDIF)

sv = StringVar(canvasfunc)
sv = StringVar()
Dic={'1':1,'1 to 2':2,'1 to 3':3,'1 to 4':4,'1 to 5':5}
sv.set("Cases")
omswitch = OptionMenu( canvasfunc, sv,*Dic.keys())
Buttonwidth = canvasfucnDetailwidth*50/100
Reset = Button(canvasleft,bg="#f2f2f2", text ="Clear Log",image = clearlogimage, compound= "left",state=DISABLED,width=Buttonwidth,height=0,pady = -800)
#Reset.place(relx=0.91,rely=0.975, x=-145, y=2, anchor=S)
Reset.grid(row = 4, column=5,pady = 2)
Delete = tk.Button(canvasleft, text ="Reset", image = clearimage, compound = "left",state=DISABLED, width=Buttonwidth,height=0,pady = -800)
    #Delete.place(relx=0.98,rely=0.6, x=-220, y=2, anchor=S)
Delete.grid(row=2,column=5)
################################## rectangle #################################################
class OptionMenurectColor:

    def __init__(self, aWindow,row,col):
       global rowCount
       #A list of string options for the optionMenu
       OPTIONS = ["Color","Red","Green","Yellow"]
       self.sv = StringVar()

       #Set CS4400 to be the default
       self.sv.set(OPTIONS[0] )

       om = OptionMenu( aWindow, self.sv, *OPTIONS)
       om.grid(row=row,column= col,pady=15)
       om.config(height=0,bd=0,highlightthickness=0)
       om.config(width=4)
       # self.b = Button(aWindow,text=setVal,command=lambda: optionChanged2(self.sv,1,2))

       Proceedrec = Button(canvasfunc,text ="Proceed",command =lambda row=rowCount, column=col+1: rectangle(self.sv,row, column,"deleterect"+str(row)) ,fg = "white",bg = "#ab4345",width=7)
      # Proceedrec.place(relx=1.0,rely=0.98, x=-194, y=2, anchor=S)
       Proceedrec.grid(row = rowCount,sticky = tk.NW,pady=15,padx=5, column=col+1)
def RectangleButton():
    global construct

    if(construct  == 1):

        clear_all()
    construct = 0
    global text
    global rowCount
    global Label
    global E1
    global E2
    global E3
    global E4
    global X1rec
    global X2rec
    global X3rec
    global X4rec
    global cancel
    global labelrec
    global deleterowcount

    global Proceedrec


    messagerec.set("Rectangle")
    deleterowcount = canvasfunc.grid_size()[1]

    for i in range(1):

        labelrec = Label(canvasfunc)
        labelrec.config(textvariable=messagerec,relief=RAISED,borderwidth=0)
        labelrec.grid(row = rowCount ,sticky = tk.NW, column=0,pady = 20,padx=(20,0))
        X1rec = Entry(canvasfunc)

        X1rec.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
        X1rec.grid(row =rowCount,sticky = tk.NW,column=1,pady = 20)
        add_placeholder_to(X1rec, 'X1')
        X2rec = Entry(canvasfunc)

        X2rec.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0 )
        X2rec.grid(row =rowCount,sticky = tk.NW, column=2,pady = 20)
        add_placeholder_to(X2rec, 'Y1')
        X3rec = Entry(canvasfunc)

        X3rec.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
        X3rec.grid(row= rowCount,sticky = tk.NW, column=3,pady = 20)
        add_placeholder_to(X3rec, 'X2')
        X4rec = Entry(canvasfunc)

        X4rec.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
        X4rec.grid(row =rowCount,sticky = tk.NW,column=4,pady = 20)
        add_placeholder_to(X4rec, 'Y2')

        app = OptionMenurectColor(canvasfunc,rowCount,5)
        cancel = Button(canvasfunc,image = close,command=lambda row=rowCount, column=7: delete_row(row, column,"deleterect"+str(row)))
        cancel.grid(row = rowCount, sticky = tk.NW,column=7,pady = 15,padx=2)
        cancel.config(bd=0,highlightthickness=0,bg = "White")
    colconfig = (canvasfucnwidth-80)/7
    canvasfunc.columnconfigure(0, minsize = 80)
    canvasfunc.columnconfigure(1, minsize = colconfig-5)
    canvasfunc.columnconfigure(2, minsize = colconfig-5)
    canvasfunc.columnconfigure(3, minsize = colconfig-5)
    canvasfunc.columnconfigure(4, minsize = colconfig-5)
    canvasfunc.columnconfigure(5, minsize = colconfig-5)
    canvasfunc.columnconfigure(6, minsize = colconfig-5)
    canvasfunc.columnconfigure(7, minsize = colconfig-5)
    rowCount = rowCount + 1
def find_in_grid(canvasfunc, row, column):
    for item in canvasfunc.grid_slaves():
        if (item.grid_info()["row"] == int(row) and item.grid_info()["column"] == int(column)):
            return item

    return None
def rectangle(rectoptn,number, test,tag):

    color = rectoptn.get()
    x = find_in_grid(canvasfunc, number, 1).get()
    # # x = X1rec.get()
    y = find_in_grid(canvasfunc, number, 2).get()
    # # y = X2rec.get()
    x2 = find_in_grid(canvasfunc, number, 3).get()
    # # x2 = X3rec.get()
    y2 = find_in_grid(canvasfunc, number, 4).get()
    canvas.delete(tag)

    if(x == "X" or y == "Y" or x2 == "length" or y2 == "width" or color == "Color"):
        shapesfeildsempty()
    elif(int(x) >= canvas1height or int(y) >= canvas1height or int(x2) >= canvas1height or int(y2) >= canvas1height):
        validevalue()
    else:
        drawRectangle(x,y,x2,y2,tag,color)
def drawRectangle(x,y,x2,y2,tag,color):
    global w

    w = canvas.create_rectangle(x,y,x2,y2, fill=color,tag =tag)
    # c.coords(x)
    def deletecanvas():
        canvas.delete('all')
        canvas.config(bg = "white")
        #x-axis
        canvas.create_line(0,1,canvasfucnwidth,1, width=0)
        #y-axis
        canvas.create_line(1,canvas1height,1,0,  width=1)



        for i in range(100):
            x = 20 + (i * 5)
            y = 15 + (i * 25)
            h = canvas1height


            canvas.create_line(x,6,x,2, width=1)
            canvas.create_line(y,2,y,6, width=2)
            #canvas.create_text(x,330, text='%d'% (20*i), anchor=N)

            # markings on y axis
        for i in range(100):
            y = 5 + (i * 5)
            x = 15 + (i * 25)
            canvas.create_line(3,y,7,y, width=1)
            canvas.create_line(3,x,9,x, width=2)
            #canvas.create_text(35,y, text='%d'% (20*i), anchor=E)

        h = canvas1height

        htext1 = h*4.5/100

        canvas.create_text(h*4/100,12, text=0)
        canvas.create_text(htext1+2,h-8, text=canvas1height)
        canvas.create_text(canvasfucnDetailwidth-12,12, text=canvasfucnDetailwidth)

    Delete = tk.Button(canvasleft, text ="Reset", image = clearimage, compound = "left",command = deletecanvas, width=Buttonwidth,height=0,pady = -800)
    #Delete.place(relx=0.98,rely=0.6, x=-220, y=2, anchor=S)
    Delete.grid(row=2,column=5)

################################ End rectangle ######################################################

######################################## Sqaure #######################################################

class OptionMenuSqColor:

    def __init__(self, aWindow,row,col):
       global rowCount
       #A list of string options for the optionMenu
       OPTIONS = ["Color","Red","Green","Yellow"]
       self.sv = StringVar()

       #Set CS4400 to be the default
       self.sv.set(OPTIONS[0] )

       om = OptionMenu( aWindow, self.sv, *OPTIONS)
       om.grid(columnspan=2, row=row,sticky = tk.NW,column= 4,pady=15)
       om.config(height=0,bd=0,highlightthickness=0,width=4)
       # self.b = Button(aWindow,text=setVal,command=lambda: optionChanged2(self.sv,1,2))

       Proceedsq = Button(canvasfunc, text ="Proceed",command = lambda row=rowCount, column=6: sqaure(self.sv,row, column,"sq"+str(row)) ,fg = "white",bg = "#ab4345",width=7)
       # Proceedsq.place(relx=1.0,rely=0.98, x=-194, y=2, anchor=S)
       Proceedsq.grid(row = rowCount,sticky = tk.NW, column=6,pady=15,padx=5)
def delete_row(number,test,tag):
    canvas.delete(tag)
    # global Proceedrec
    # Proceedrec.grid_remove()
    global deletecanvas

    for item in canvasfunc.grid_slaves():
        if int(item.grid_info()["row"]) == number:
            item.grid_forget()
def cancel():
    global X1rec
    global X2rec
    global X3rec
    global X4rec
    global labelrec
    global cancel

    cancel.grid_remove()
    labelrec.grid_remove()
    X1rec.grid_forget()
    X2rec.grid_forget()
    X3rec.grid_forget()
    X4rec.grid_forget()
def SqaureButton():
    global text
    global label

    global rowCount
    global X1sq
    global Ysq
    global Zsq
    global cancelsq
    global construct

    if(construct  == 1):
        clear_all()

    # deleteconstruct()
    construct = 0

    messagesq.set("Square")
    for i in range(1):
        label = Label(canvasfunc,textvariable=messagesq,relief=RAISED,borderwidth=0 )
        label.grid(row = rowCount ,sticky = tk.NW, column=0,pady = 20,padx=(20,0))

        X1sq= Entry(canvasfunc)
        X1sq.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
        X1sq.grid(row =rowCount,sticky = tk.NW, column=1,pady = 20)
        add_placeholder_to(X1sq, 'X')

        Ysq = Entry(canvasfunc)
        Ysq.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0 )
        Ysq.grid(row =rowCount,sticky = tk.NW, column=2,pady = 20)
        add_placeholder_to(Ysq, 'Y')

        Zsq = Entry(canvasfunc)
        Zsq.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
        Zsq.grid(row =rowCount,sticky = tk.NW, column=3,pady = 20)
        add_placeholder_to(Zsq, 'SIDE')

        app = OptionMenuSqColor(canvasfunc,rowCount,4)

        cancelsq = Button(canvasfunc,image = close, command=lambda row=rowCount, column=7: canselsq(row, column,"sq"+str(row)) )
        cancelsq.grid(row = rowCount, sticky = tk.NW,column=7,pady=15,padx=2)
        cancelsq.config(bd=0, highlightthickness=0,bg = "White")

    rowCount = rowCount+1
    # colconfig = canvasfucnwidth/10
    # canvasfunc.columnconfigure('all', minsize = colconfig)
    colconfig = (canvasfucnwidth-80)/7
    canvasfunc.columnconfigure(0, minsize = 80)
    canvasfunc.columnconfigure(1, minsize = colconfig-5)
    canvasfunc.columnconfigure(2, minsize = colconfig-5)
    canvasfunc.columnconfigure(3, minsize = colconfig-5)
    canvasfunc.columnconfigure(4, minsize = colconfig-5)
    canvasfunc.columnconfigure(5, minsize = colconfig-5)
    canvasfunc.columnconfigure(6, minsize = colconfig-5)
    canvasfunc.columnconfigure(7, minsize = colconfig-5)
def canselsq(number,test,sqtag):
    global ProceedsqProceedsq

    Proceedsq.grid_remove()
    Proceedsq.grid_forget()
    canvas.delete(sqtag)

    for item in canvasfunc.grid_slaves():
        if int(item.grid_info()["row"]) == number:
            item.grid_forget()
def sqaure(sqcolor,number,test,sqtag):
    global x
    global y
    global z
    color = sqcolor.get()

    x = (find_in_grid(canvasfunc, number, 1).get())
    # # x = X1rec.get()
    y = (find_in_grid(canvasfunc, number, 2).get())
    # # y = X2rec.get()
    side = (find_in_grid(canvasfunc, number, 3).get())
    # # # x2 = X3rec.get()
    #
    # x = X1sq.get()
    # y = Ysq.get()

    # side = Zsq.get()
    if(x == "X" or y == "Y" or side == "SIDE" or color == "Color" ):
        shapesfeildsempty()
    if(int(x) >= canvas1height or int(y) >= canvas1height or int(side) >= canvas1height):
        validevalue()
    else:
        create_square(int(x),int(y),int(side),sqtag,color)
    #drawSqaure(x,y,x2,y2)
def create_square(x1,y1,side, sqtag,color):
    x2 =  x1+side
    y2 =  y1+side
    size = x1
    canvas.delete(sqtag)


    sq = canvas.create_rectangle(x1,y1,x2,y2, fill=color,tag = sqtag)
    def deletecanvas():
        canvas.config(bg = "white")
        canvas.delete("all")
        #x-axis
        canvas.create_line(0,1,canvasfucnwidth,1, width=0)
        #y-axis
        canvas.create_line(1,canvas1height,1,0,  width=1)



        for i in range(100):
            x = 20 + (i * 5)
            y = 15 + (i * 25)
            h = canvas1height


            canvas.create_line(x,6,x,2, width=1)
            canvas.create_line(y,2,y,6, width=2)
            #canvas.create_text(x,330, text='%d'% (20*i), anchor=N)

            # markings on y axis
        for i in range(100):
            y = 5 + (i * 5)
            x = 15 + (i * 25)
            canvas.create_line(3,y,7,y, width=1)
            canvas.create_line(3,x,9,x, width=2)
            #canvas.create_text(35,y, text='%d'% (20*i), anchor=E)

        h = canvas1height


        htext1 = h*4.5/100

        canvas.create_text(h*4/100,12, text=0)
        canvas.create_text(htext1+2,h-8, text=canvas1height)
        canvas.create_text(canvasfucnDetailwidth-12,12, text=canvasfucnDetailwidth)



    Delete = Button(canvasleft,bg="#f2f2f2", text ="Reset",image = clearimage, compound = "left",command = deletecanvas, width=Buttonwidth,height=0,pady = -800)
    #Delete.place(relx=0.98,rely=0.6, x=-220, y=2, anchor=S)
    Delete.grid(row=2,column=5)
########################################### End sqaure ###################################################

#################################LINE#######################################################################
class OptionMenuLineColor:

    def __init__(self, aWindow,row,col):
       global rowCount
       #A list of string options for the optionMenu
       OPTIONS = ["Color","Red","Green","Yellow"]
       self.sv = StringVar()

       #Set CS4400 to be the default
       self.sv.set(OPTIONS[0] )

       om = OptionMenu( aWindow, self.sv, *OPTIONS)
       om.grid(row=row,column= col,sticky = tk.NW,pady=15)
       om.config(height=0,bd=0,highlightthickness=0,width=4)
       # self.b = Button(aWindow,text=setVal,command=lambda: optionChanged2(self.sv,1,2))

       Proceedline = Button(canvasfunc, text ="Proceed",command = lambda row=rowCount, column=col+1: Linefunction(self.sv,row, column,"line"+str(row)) ,fg = "white",bg = "#ab4345",width=7)
       # Proceedline.place(relx=1.0,rely=0.98, x=-194, y=2, anchor=S)
       Proceedline.grid(row = rowCount, column=col+1,sticky = tk.NW,pady=15,padx=5)
def LineButton():
    global text
    global labelline
    global E1
    global E2
    global E3
    global E4
    global rowCount
    global x
    global y
    global x2
    global y2
    global X1line
    global X2line
    global X3line
    global X4line
    global cancelline
    global construct

    if(construct  == 1):

        clear_all()
    # deleteconstruct()
    construct = 0

    messageline.set("Line")
    # deleteconstruct()
    for i in range(1):
        labelline = Label(canvasfunc )
        labelline.config( textvariable=messageline,relief=RAISED,borderwidth=0)
        labelline.grid(row = rowCount , column=0,pady = 20,padx=(20,0),sticky = tk.NW)

        X1line = Entry(canvasfunc)
        X1line.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
        X1line.grid(row =rowCount, column=1,pady = 20,sticky = tk.NW)
        add_placeholder_to(X1line, 'X1')

        X2line = Entry(canvasfunc )
        X2line.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
        X2line.grid(row =rowCount, column=2,pady = 20,sticky = tk.NW)
        add_placeholder_to(X2line, 'Y1')

        X3line = Entry(canvasfunc)
        X3line.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
        X3line.grid(row =rowCount, column=3,pady = 20,sticky = tk.NW)
        add_placeholder_to(X3line, 'X2')

        X4line = Entry(canvasfunc)
        X4line.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
        X4line.grid(row =rowCount, column=4,pady = 20,sticky = tk.NW)
        add_placeholder_to(X4line, 'Y2')

        app = OptionMenuLineColor(canvasfunc,rowCount,5)

        cancelline = Button(canvasfunc,image = close, command=lambda row=rowCount, column=7: delete_line(row, column,"line"+str(row)))
        cancelline.grid(row = rowCount, column=7,pady=15,padx=2,sticky = tk.NW)
        cancelline.config(bd=0, highlightthickness=0,bg = "White")

    rowCount = rowCount+1
    colconfig = (canvasfucnwidth-80)/7
    canvasfunc.columnconfigure(0, minsize = 80)
    canvasfunc.columnconfigure(1, minsize = colconfig-5)
    canvasfunc.columnconfigure(2, minsize = colconfig-5)
    canvasfunc.columnconfigure(3, minsize = colconfig-5)
    canvasfunc.columnconfigure(4, minsize = colconfig-5)
    canvasfunc.columnconfigure(5, minsize = colconfig-5)
    canvasfunc.columnconfigure(6, minsize = colconfig-5)
    canvasfunc.columnconfigure(7, minsize = colconfig-5)

    # colconfig = canvasfucnwidth/10
    # canvasfunc.columnconfigure('all', minsize = colconfig)
def delete_line(number,test,linetag):
    global Proceedline
    Proceedline.grid_remove()
    Proceedline.grid_forget()
    canvas.delete(linetag)

    for item in canvasfunc.grid_slaves():
        if int(item.grid_info()["row"]) == number:
            item.grid_forget()
def Linefunction(linecolor,number, test,linetag):
    # x = X1line.get()
    # y= X2line.get()
    # x2 = X3line.get()
    # y2 = X4line.get()
    x = find_in_grid(canvasfunc, number, 1).get()
    # # x = X1rec.get()
    y = find_in_grid(canvasfunc, number, 2).get()
    # # y = X2rec.get()
    x2 = find_in_grid(canvasfunc, number, 3).get()
    y2 = find_in_grid(canvasfunc, number, 4).get()

    color = linecolor.get()


    if(x == "X0" or y == "X1" or x2 =="Y0" or y2=="Y1" or color == "Color"):
        shapesfeildsempty()
    elif(int(x) >= canvas1height or int(y) >= canvas1height or int(x2) >= canvas1height or int(y2) >= canvas1height):
        validevalue()
    else:
        drwaLine(x,y,x2,y2,linetag,color)
def drwaLine(x,y,x2,y2,linetag,color):
    #greenbox = canvas.create_rectangle(x,y,x2,y2,fill = "green")
    canvas.delete(linetag)
    line = canvas.create_line(x,y,x2,y2,tag = linetag,fill = color)
    #canvas.create_rectangle(x,y,x2,y2)
    def deletecanvas():
        canvas.config(bg = "white")
        canvas.delete("all")
        #x-axis
        canvas.create_line(0,1,canvasfucnwidth,1, width=0)
        #y-axis
        canvas.create_line(1,canvas1height,1,0,  width=1)



        for i in range(100):
            x = 20 + (i * 5)
            y = 15 + (i * 25)
            h = canvas1height


            canvas.create_line(x,6,x,2, width=1)
            canvas.create_line(y,2,y,6, width=2)
            #canvas.create_text(x,330, text='%d'% (20*i), anchor=N)

            # markings on y axis
        for i in range(100):
            y = 5 + (i * 5)
            x = 15 + (i * 25)
            canvas.create_line(3,y,7,y, width=1)
            canvas.create_line(3,x,9,x, width=2)
            #canvas.create_text(35,y, text='%d'% (20*i), anchor=E)

        h = canvas1height

        htext1 = h*4.5/100

        canvas.create_text(h*4/100,12, text=0)
        canvas.create_text(htext1+2,h-8, text=canvas1height)
        canvas.create_text(canvasfucnDetailwidth-12,12, text=canvasfucnDetailwidth)

    Delete = Button(canvasleft,bg="#f2f2f2", text ="Reset",image = clearimage,compound="left",command = deletecanvas, width=Buttonwidth,height=0,pady = -800)
    #Delete.place(relx=1.0,rely=0.6, x=-220, y=2, anchor=S)
    Delete.grid(row=2,column=5)
    # Delete = Button(canvas,bg="#f2f2f2", text ="Reset",command = deletecanvas, width=60,height=0,pady = -800)
    # Delete.place(relx=1.0,rely=0.988, x=-220, y=2, anchor=S)

################################# end line ###########################################################

########################################Circle ############################################################
class OptionMenuCirColor:

    def __init__(self, aWindow,row,col):
       global rowCount
       #A list of string options for the optionMenu
       OPTIONS = ["Color","Red","Green","Yellow"]
       self.sv = StringVar()

       #Set CS4400 to be the default
       self.sv.set(OPTIONS[0] )

       om = OptionMenu( aWindow, self.sv, *OPTIONS)
       om.grid(columnspan=2, row=row,sticky = tk.NW,column= col,pady=15)
       om.config(height=0,bd=0,highlightthickness=0,width=4)
       # self.b = Button(aWindow,text=setVal,command=lambda: optionChanged2(self.sv,1,2))

       Proceedsq = Button(canvasfunc, text ="Proceed",command = lambda row=rowCount, column=6: circle(self.sv,row, column,"sq"+str(row)) ,fg = "white",bg = "#ab4345",width=7)
       # Proceedsq.place(relx=1.0,rely=0.98, x=-194, y=2, anchor=S)
       Proceedsq.grid(row = rowCount,sticky = tk.NW, column=6,pady=15,padx=5)
def CircleButton():
    global text
    global labelcircle
    global x
    global y
    global rowCount
    global review
    global X1cir
    global X2cir
    global Rcir
    global cancelcir
    global construct

    if(construct  == 1):

        clear_all()
    # deleteconstruct()
    construct = 0

    l1ifelse.grid_forget()
    l3ifelse.grid_forget()
    o1ifelse.grid_forget()
    l1nestedif.grid_forget()
    l2nestedif.grid_forget()
    l3nestedif.grid_forget()
    l4nestedif.grid_forget()
    l5nestedif.grid_forget()
    l6nestedif.grid_forget()
    o1nestedif.grid_forget()
    o6nestedif.grid_forget()
    o4nestedif.grid_forget()
    l1.grid_forget()
    l2.grid_forget()
    l3.grid_forget()
    l4.grid_forget()
    l5.grid_forget()
    l6.grid_forget()
    l7.grid_forget()
    l8.grid_forget()
    l9.grid_forget()
    l10.grid_forget()
    l11.grid_forget()
    l12.grid_forget()
    messagecir.set("Circle")
    # deleteconstruct()
    for i in range(1):
        labelcircle = Label(canvasfunc, textvariable=messagecir,borderwidth=0)
        labelcircle.grid(row = rowCount , column=0,pady = 20,padx=(20,0),sticky = tk.NW)

        X1cir = Entry(canvasfunc)
        X1cir.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
        X1cir.grid(row =rowCount, column=1,pady = 20,sticky = tk.NW)
        add_placeholder_to(X1cir, 'X')

        X2cir = Entry(canvasfunc)
        X2cir.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0 )
        X2cir.grid(row =rowCount, column=2,pady = 20,sticky = tk.NW)
        add_placeholder_to(X2cir, 'Y')

        Rcir = Entry(canvasfunc)
        Rcir.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
        Rcir.grid(row =rowCount, column=3,pady = 20,sticky = tk.NW)
        add_placeholder_to(Rcir, 'R')

        app = OptionMenuCirColor(canvasfunc,rowCount,4)

        cancelcir = Button(canvasfunc,image = close,command=lambda row=rowCount, column=7: delete_cir(row, column,"cir"+str(row)))
        cancelcir.grid(row = rowCount, column=7,pady=15,padx=2,sticky = tk.NW)
        cancelcir.config(bd=0, highlightthickness=0,bg = "White")


    rowCount=rowCount+1
    colconfig = (canvasfucnwidth-80)/7
    canvasfunc.columnconfigure(0, minsize = 80)
    canvasfunc.columnconfigure(1, minsize = colconfig-5)
    canvasfunc.columnconfigure(2, minsize = colconfig-5)
    canvasfunc.columnconfigure(3, minsize = colconfig-5)
    canvasfunc.columnconfigure(4, minsize = colconfig-5)
    canvasfunc.columnconfigure(5, minsize = colconfig-5)
    canvasfunc.columnconfigure(6, minsize = colconfig-5)
    canvasfunc.columnconfigure(7, minsize = colconfig-5)

    # colconfig = canvasfucnwidth/10
    # canvasfunc.columnconfigure('all', minsize = colconfig)
def delete_cir(number,test,cirtag):
    global Proceedcir

    Proceedcir.grid_remove()
    Proceedcir.grid_forget()
    canvas.delete(cirtag)

    for item in canvasfunc.grid_slaves():
        if int(item.grid_info()["row"]) == number:
            item.grid_forget()
def _create_circle(self, x, y, r, **kwargs):

    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle
def _create_circle_arc(self, x, y, r, **kwargs):

    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle_arc = _create_circle_arc
def circle(circolor,number,test,cirtag):

    x = find_in_grid(canvasfunc, number, 1).get()
    # # x = X1rec.get()
    y = find_in_grid(canvasfunc, number, 2).get()
    # # y = X2rec.get()
    r = find_in_grid(canvasfunc, number, 3).get()
    color = circolor.get()

    X = (x)
    Y = (y)
    R = (r)

    X1 = (x)
    Y1 = (y)
    R1 = (r)

    if(X == "X" or Y == "Y" or R =="R" or color == "Color" ):
        shapesfeildsempty()
    if(int(X1) >= canvas1height or int(Y1) >= canvas1height or int(R1) >= canvas1height):
        validevalue()
    else:
        canvas.delete(cirtag)
        cir = canvas.create_circle(int(X1),int(Y1),int(R1), tag = cirtag,fill=color, outline="Black")
    def deletecanvas():
        canvas.config(bg = "white")
        canvas.delete("all")
        #x-axis
        canvas.create_line(0,1,canvasfucnwidth,1, width=0)
        #y-axis
        canvas.create_line(1,canvas1height,1,0,  width=1)



        for i in range(100):
            x = 20 + (i * 5)
            y = 15 + (i * 25)
            h = canvas1height


            canvas.create_line(x,6,x,2, width=1)
            canvas.create_line(y,2,y,6, width=2)
            #canvas.create_text(x,330, text='%d'% (20*i), anchor=N)

            # markings on y axis
        for i in range(100):
            y = 5 + (i * 5)
            x = 15 + (i * 25)
            canvas.create_line(3,y,7,y, width=1)
            canvas.create_line(3,x,9,x, width=2)
            #canvas.create_text(35,y, text='%d'% (20*i), anchor=E)

        h = canvas1height


        htext1 = h*4.5/100

        canvas.create_text(h*4/100,12, text=0)
        canvas.create_text(htext1+2,h-8, text=canvas1height)
        canvas.create_text(canvasfucnDetailwidth-12,12, text=canvasfucnDetailwidth)


    Delete = Button(canvasleft,bg="#f2f2f2", text ="Reset",image = clearimage,compound="left",command = deletecanvas, width=Buttonwidth,height=0,pady = -800)
            #Delete.place(relx=1.0,rely=0.6, x=-220, y=2, anchor=S)
    Delete.grid(row=2,column=5)

################################ End Circle #################################################################

################################### Background #############################################################

def Background():
    global labelbg
    global E1
    global rowCount
    global cancelbg
    global construct

    if(construct  == 1):
        clear_all()
    # deleteconstruct()
    construct = 0


    bgmessage.set("Set Background :")
    (triple, hexstr) = askcolor()

    def my_callback():

        (triple, hexstr) = askcolor()


        if hexstr:

            canvas.config(bg=hexstr)
            E1.delete(0, 'end')
            E1.insert(INSERT,hexstr)
        else:

            add_placeholder_to(E1, 'COLOR')
    for i in range(1):
        labelbg = Label(canvasfunc)
        labelbg.config(textvariable=bgmessage)
        labelbg.grid(row = rowCount ,columnspan=2,sticky = tk.NW, column=0,pady = 20,padx=(20,0))
        E1 = Entry(canvasfunc)
        E1.config(justify= 'right',bg="#47a3a5",width = 7,borderwidth=0,highlightthickness=0)
        E1.bind("<Button-1>", lambda e:my_callback())
        E1.grid(row =rowCount,sticky = tk.NW,columnspan=4,column=2,pady = 20)



        if hexstr:
            canvas.config(bg=hexstr)
            E1.insert(INSERT,hexstr)
        else:
            add_placeholder_to(E1, 'COLOR')
        cancelbg = Button(canvasfunc,image = close,command=lambda row=rowCount, column=7: delete_bg(row, column) )
        cancelbg.grid(row = rowCount,sticky = tk.NW,column=7,pady=15,padx=2)
        cancelbg.config(bd=0, highlightthickness=0,bg = "White")
        Proceed = Button(canvasfunc, text ="Proceed",fg = "white",command =lambda row=rowCount, column=6: backgroundfill(row, column) ,bg = "#ab4345",width=7)
                # Proceed.place(relx=1.0,rely=0.98, x=-194, y=2, anchor=S)
        Proceed.grid(row = rowCount,sticky = tk.NW, column=6,pady=15,padx=5)

        # colconfig = canvasfucnwidth/10
        # canvasfunc.columnconfigure('all', minsize = colconfig)

        colconfig = (canvasfucnwidth-90)/7
        canvasfunc.columnconfigure(0, minsize = 90)
        canvasfunc.columnconfigure(1, minsize = colconfig-5)
        canvasfunc.columnconfigure(2, minsize = colconfig-5)
        canvasfunc.columnconfigure(3, minsize = colconfig-5)
        canvasfunc.columnconfigure(4, minsize = colconfig-5)
        canvasfunc.columnconfigure(5, minsize = colconfig-5)
        canvasfunc.columnconfigure(6, minsize = colconfig-5)
        canvasfunc.columnconfigure(7, minsize = colconfig-5)

        def deletecanvas():
            canvas.config(bg = "white")
            canvas.delete("all")
                #x-axis
            canvas.create_line(0,1,canvasfucnwidth,1, width=0)
                #y-axis
            canvas.create_line(1,canvas1height,1,0,  width=1)

            for i in range(100):
                x = 20 + (i * 5)
                y = 15 + (i * 25)
                h = canvas1height


                canvas.create_line(x,6,x,2, width=1)
                canvas.create_line(y,2,y,6, width=2)
                    #canvas.create_text(x,330, text='%d'% (20*i), anchor=N)

                    # markings on y axis
            for i in range(100):
                y = 5 + (i * 5)
                x = 15 + (i * 25)
                canvas.create_line(3,y,7,y, width=1)
                canvas.create_line(3,x,9,x, width=2)
                    #canvas.create_text(35,y, text='%d'% (20*i), anchor=E)

            h = canvas1height

            htext1 = h*4.5/100
            canvas.create_text(h*4/100,12, text=0)
            canvas.create_text(htext1+2,h-8, text=canvas1height)
            canvas.create_text(canvasfucnDetailwidth-12,12, text=canvasfucnDetailwidth)
        Delete = Button(canvasleft,bg="#f2f2f2", text ="Reset",image = clearimage,compound="left",command = deletecanvas, width=Buttonwidth,height=0,pady = -800)
                    #Delete.place(relx=1.0,rely=0.6, x=-220, y=2, anchor=S)
        Delete.grid(row=2,column=5)
        rowCount = rowCount+1
def backgroundfill(number,test):
    text = E1.get()
    # text = find_in_grid(canvasfunc, number, 1).get()

    if(text == "COLOR" ):
        emptyfields()
    else:
        canvas.config(bg=text)
    def deletecanvas():
        canvas.config(bg = "white")
        canvas.delete("all")
        #x-axis
        canvas.create_line(0,1,canvasfucnwidth,1, width=0)
        #y-axis
        canvas.create_line(1,canvas1height,1,0,  width=1)



        for i in range(100):
            x = 20 + (i * 5)
            y = 15 + (i * 25)
            h = canvas1height


            canvas.create_line(x,6,x,2, width=1)
            canvas.create_line(y,2,y,6, width=2)
            #canvas.create_text(x,330, text='%d'% (20*i), anchor=N)

            # markings on y axis
        for i in range(100):
            y = 5 + (i * 5)
            x = 15 + (i * 25)
            canvas.create_line(3,y,7,y, width=1)
            canvas.create_line(3,x,9,x, width=2)
            #canvas.create_text(35,y, text='%d'% (20*i), anchor=E)

        h = canvas1height


        htext1 = h*4.5/100

        canvas.create_text(h*4/100,12, text=0)
        canvas.create_text(htext1+2,h-8, text=canvas1height)
        canvas.create_text(canvasfucnDetailwidth-12,12, text=canvasfucnDetailwidth)


    Delete = Button(canvasleft,bg="#f2f2f2", text ="Reset",image = clearimage,compound="left",command = deletecanvas, width=Buttonwidth,height=0,pady = -800)
            #Delete.place(relx=1.0,rely=0.6, x=-220, y=2, anchor=S)
    Delete.grid(row=2,column=5)



    # # x = X1rec.get()

    # color  = E1.get()
def delete_bg(number,test):
    global Proceed
    Proceed.grid_remove()
    Proceed.grid_forget()
    for item in canvasfunc.grid_slaves():
        if int(item.grid_info()["row"]) == number:
            item.grid_forget()
######################################## End Backgournmd ##############################################

################################################# Text Color ######################################
class OptionMenuDemo:

    def __init__(self, aWindow,row,col):
       global rowCount
       #A list of string options for the optionMenu
       OPTIONS = ["Color","Red","Green","Yellow"]
       self.sv = StringVar()

       #Set CS4400 to be the default
       self.sv.set(OPTIONS[0] )

       om = OptionMenu( aWindow, self.sv, *OPTIONS)
       om.grid(columnspan=4,row=row,column= 2)
       om.config(height=0,bd=0,highlightthickness=0,width=4)
       # self.b = Button(aWindow,text=setVal,command=lambda: optionChanged2(self.sv,1,2))


       Proceedtext = Button(aWindow, text ="Proceed",fg = "white",command=lambda row=rowCount, column=6: colortext(self.sv,row, column) ,
       bg = "#ab4345",width=7)
       # Proceedtext.place(relx=1.0,rely=0.98, x=-194, y=0, anchor=S)
       Proceedtext.grid(row=row,sticky = tk.NW, column=6,pady = 20,padx=5)
def textcolor():

    # deleteconstruct()
    global textlabel
    global textentry
    global rowCount
    global colorentry
    global varcolor
    global canceltextcolor
    global drop_menutexttype
    global construct

    if(construct  == 1):
        clear_all()
    construct = 0
    textcolormessage.set("Draw Text")
    for i in range(1):
        textlabel = Label(canvasfunc)
        textlabel.config(textvariable=textcolormessage)
        textlabel.grid(row = rowCount ,sticky = tk.NW, column=0,pady = 20,padx=(20,0))
        textentry = Entry(canvasfunc)
        textentry.config(justify= 'right',relief=RAISED,width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
        textentry.grid(row =rowCount,sticky = tk.NW, column=1,pady = 20)
        add_placeholder_to(textentry, 'TEXT')
        #populate_menu(drop_menutexttype, Red=Red,Green=Green,Pink=Pink,Black = Black)
        varcolor = StringVar(canvasfunc)
        varcolor.set("Color")
        app = OptionMenuDemo(canvasfunc,rowCount,2)

        canceltextcolor = Button(canvasfunc,image = close,command=lambda row=rowCount, column=7: delete_textcolor(row, column))
        canceltextcolor.grid(row = rowCount,sticky = tk.NW, column=7,pady=20,padx=2)
        canceltextcolor.config(bd=0, highlightthickness=0,bg = "White")


    rowCount =rowCount+1
    # colconfig = canvasfucnwidth/10
    # canvasfunc.columnconfigure('all', minsize = colconfig)
    colconfig = (canvasfucnwidth-90)/7
    canvasfunc.columnconfigure(0, minsize = 90)
    canvasfunc.columnconfigure(1, minsize = colconfig-5)
    canvasfunc.columnconfigure(2, minsize = colconfig-5)
    canvasfunc.columnconfigure(3, minsize = colconfig-5)
    canvasfunc.columnconfigure(4, minsize = colconfig-5)
    canvasfunc.columnconfigure(5, minsize = colconfig-5)
    canvasfunc.columnconfigure(6, minsize = colconfig-5)
    canvasfunc.columnconfigure(7, minsize = colconfig-5)
def delete_textcolor(number,test):

    for item in canvasfunc.grid_slaves():
        if int(item.grid_info()["row"]) == number:
            item.grid_forget()
def colortext(sv,number ,test):
    #chosen_option = var.get()

    color = sv.get()
    text = find_in_grid(canvasfunc, number, 1).get()
    if(color == "Color" or  text == "TEXT" or text ==""):
        shapesfeildsempty()
    else:
        drawtext(color,text)


    # text = textentry.get()
    #color = find_in_grid(canvasfunc, number, 2,varcolor).get()

    #color = find_in_grid(canvasfunc, number, 2).get()
def drawtext(color,text):

    if(color == "Red"):

        outputtext.tag_configure('name1', foreground="Red")
        outputtext.insert(END, text+'\n', 'name1')

    if(color == "Green"):

        outputtext.tag_configure('name', foreground="Green")
        outputtext.insert(END, text+'\n', 'name')

    if(color == "Yellow"):
        outputtext.tag_configure('name2', foreground="Yellow")
        outputtext.insert(END, text+'\n', 'name2')


    def clearlog():
        outputtext.delete('1.0', END)

    Reset = Button(canvasleft,bg="#f2f2f2", text ="Clear Log",image = clearlogimage, compound= "left",command = clearlog,width=Buttonwidth,height=0,pady = -800)
    #Reset.place(relx=0.91,rely=0.975, x=-145, y=2, anchor=S)
    Reset.grid(row = 4, column=5,pady = 2)
def clearlog():

    output.delete('1.0', END)
##################################### End Text Color #############################################

##################################### Text type ###########################################################
class OptionMenuDemo2:

    def __init__(self, aWindow,row,col):
       global rowCount
       #A list of string options for the optionMenu
       OPTIONS = ["Type","Arial","Times","NewRoman"]
       OPTIONS2 = ["Color","Red","Yellow","Green"]
       self.sv = StringVar()
       self.sv1 = StringVar()

       #Set CS4400 to be the default
       self.sv.set(OPTIONS[0] )
       self.sv1.set(OPTIONS2[0] )

       om = OptionMenu( aWindow, self.sv, *OPTIONS)
       om.grid(row=row,column= col,sticky = tk.NW,pady=8,columnspan=2)
       om.config(height=0,bd=0,highlightthickness=0,width=8,padx=3)

       om2 = OptionMenu( aWindow, self.sv1, *OPTIONS2)
       om2.grid(row=row,column= 4,sticky = tk.NW,pady=8,padx=3,columnspan=2)
       om2.config(height=0,bd=0,highlightthickness=0,width=5)


       Proceedtype = Button(canvasfunc, text ="Proceed",fg = "white",command = lambda row=rowCount, column=6:typetext(self.sv,self.sv1,row, column) ,bg = "#ab4345",width=7)
       # Proceedtype.place(relx=1.0,rely=0.98, x=-194, y=2, anchor=S)
       Proceedtype.grid(row = rowCount,sticky = tk.NW, column=6,pady=10,padx=5)
def texttype():
    global labeltext
    global entrytext
    global hidden
    global rowCount
    global canceltexttype
    global drop_menutext
    global vartype
    global varcolortext
    global construct

    if(construct  == 1):
        clear_all()
    construct = 0
    hidden =1

    # deleteconstruct()

    textypemessage.set("Text Type")
    for i in range(1):

        labeltext = Label(canvasfunc)
        labeltext.config(textvariable=textypemessage)
        labeltext.grid(row = rowCount ,sticky = tk.NW, column=0,pady = 10,padx=(20,0))
        entrytext = Entry(canvasfunc)
        entrytext.config(justify= 'right',bg="#47a3a5",width=5,borderwidth=0,highlightthickness=0)
        entrytext.grid(row =rowCount, column=1,pady = 10,padx=5,sticky=tk.NW)
        add_placeholder_to(entrytext, 'TEXT')
        vartype = StringVar(canvasfunc)
        vartype.set("Type")

        app = OptionMenuDemo2(canvasfunc,rowCount,2)
        varcolortext = StringVar(canvasfunc)
        varcolortext.set("Color")

        canceltexttype = Button(canvasfunc,image = close,command=lambda row=rowCount, column=7: delete_texttype(row, column))
        canceltexttype.grid(row = rowCount,sticky = tk.NW, column=7,pady=10,padx=2)
        canceltexttype.config(bd=0, highlightthickness=0,bg = "White")

    # colconfig = canvasfucnwidth/10
    # canvasfunc.columnconfigure('all', minsize = colconfig)

    colconfig = (canvasfucnwidth-80)/7
    canvasfunc.columnconfigure(0, minsize = 80)
    canvasfunc.columnconfigure(1, minsize = colconfig-5)
    canvasfunc.columnconfigure(3, minsize = colconfig-5)
    canvasfunc.columnconfigure(5, minsize = colconfig-5)
    canvasfunc.columnconfigure(6, minsize = colconfig-5)
    canvasfunc.columnconfigure(7, minsize = colconfig-10)




    rowCount =rowCount+1
def delete_texttype(number,test):
    global Proceedtype
    Proceedtype.grid_remove()
    Proceedtype.grid_forget()
    for item in canvasfunc.grid_slaves():
        if int(item.grid_info()["row"]) == number:
            item.grid_forget()
def canceltexttype():
    global entrytext
    global drop_menutext
    global labeltext
    global canceltexttype
    canceltexttype.grid_remove()
    labeltext.grid_remove()
    drop_menutext.grid_forget()
    entrytext.grid_forget()
def typetext(optn,optn1,number,test):
    chosen_option = optn.get()
    colortext = optn1.get()


    text = find_in_grid(canvasfunc, number, 1).get()
    # text = entrytext.get()

    if(text == "TEXT" or chosen_option == "Type" or colortext =="Color"  or text ==""):
        shapesfeildsempty()

    drawtype(chosen_option,text,colortext)
def drawtype(chosen_option,text,colortext):

    if(chosen_option == "Arial" and colortext == "Red"):
        outputtext.insert(END, text+'\n',"name1")
        outputtext.tag_configure('name1', font="Arial", foreground = "Red")
    elif(chosen_option == "Arial" and colortext == "Yellow"):
        outputtext.insert(END, text+'\n',"name2")
        outputtext.tag_configure('name2', font="Arial", foreground = "Yellow")
    elif(chosen_option == "Arial" and colortext == "Green"):
        outputtext.insert(END, text+'\n',"name3")
        outputtext.tag_configure('name3', font="Arial", foreground = "Green")

    if(chosen_option == "Times" and colortext == "Green"):
        outputtext.insert(END, text+'\n',"name4")
        outputtext.tag_configure('name4', font="Times", foreground = "Green")
    elif(chosen_option == "Times" and colortext == "Red"):
        outputtext.insert(END, text+'\n',"name5")
        outputtext.tag_configure('name5', font="Times", foreground = "Red")
    elif(chosen_option == "Times" and colortext == "Yellow"):
        outputtext.insert(END, text+'\n',"name6")
        outputtext.tag_configure('name6', font="Times", foreground = "Yellow")

    if(chosen_option == "NewRoman" and colortext == "Green"):
        outputtext.insert(END, text+'\n',"name7")
        outputtext.tag_configure('name7', font="NewRoman", foreground = "Green")
    elif(chosen_option == "NewRoman" and colortext == "Red"):
        outputtext.insert(END, text+'\n',"name8")
        outputtext.tag_configure('name8', font="NewRoman", foreground = "Red")
    elif(chosen_option == "NewRoman" and colortext == "Yellow"):
        outputtext.insert(END, text+'\n',"name9")
        outputtext.tag_configure('name9', font="NewRoman", foreground = "Yellow")





    def clearlog():
        outputtext.delete('1.0', END)
    Reset = Button(canvasleft,bg="#f2f2f2", text ="Clear Log",image = clearlogimage, compound= "left",command = clearlog,width=Buttonwidth,height=0,pady = -800)
    #Reset.place(relx=0.91,rely=0.975, x=-145, y=2, anchor=S)
    Reset.grid(row= 4,column=5,pady = 2)
###################################### End Text type #######################################################

######################################## FOR- LOOP ############################################################

class OptionMenuDemoFor:

    def __init__(self, aWindow,row,col):
       global rowCount
       #A list of string options for the optionMenu
       OPTIONS = ["*","+","-","/"]
       self.sv = StringVar()
       self.sv.set(OPTIONS[0] )
       omfor = OptionMenu( aWindow, self.sv, *OPTIONS)
       omfor.grid(row=rowCount+1,column= col,columnspan=2,sticky=tk.NW)
       omfor.config(height=0,bd=0,highlightthickness=0,width=4)
       Proceedfor.config(text ="Proceed",fg = "white",command = lambda  row=rowCount, column=6: functionForLoop(self.sv,row, column) ,bg = "#ab4345",width=7)
       Proceedfor.grid(row = rowCount+1,columnspan=2,sticky=tk.NW, column=6)

       cancelfor.config(image = close,command=lambda row=rowCount,columnspan=2,sticky=tk.NW, column=6: btncancelfor(omfor,row, column))
       cancelfor.grid(row = rowCount, column=6)
       cancelfor.config(bd=0, highlightthickness=0,bg = "White")
otherText.insert(END,'1')
def Forloop():
    global forlabel
    global itext
    global jtext
    global rowCount
    global cancelfor
    global Proceedfor
    global forfinallabel
    global forinitiallabel
    global Printforloop
    global otherText
    global construct


    construct = 1
    clear_all()

    messageloop.set("For Y in Range :")
    messageinitialvalue.set("Initial Value")
    messagefinalvalue.set("Final Value")

    # for i in range(1):
    forlabel = Label(canvasfunc)
    forlabel.config(textvariable=messageloop,width=15)
    forlabel.grid(row =rowCount ,columnspan=2,sticky=tk.NW, column=0,pady = 20)

    itext = Entry(canvasfunc)
    itext.config(justify= 'right',width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
    add_placeholder_to(itext, 'Int A')
    itext.grid(row =rowCount,columnspan=2,sticky=tk.NW, column=2,pady =20)
    jtext = Entry(canvasfunc)
    jtext.config(justify= 'right',width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
    add_placeholder_to(jtext, 'Int B')
    jtext.grid(row =rowCount,columnspan=2,sticky=tk.NW, column=4,pady = 20)

    messageprintfor.set("Print Y : ")
    Printforloop.config(textvariable=messageprintfor,width=15)
    Printforloop.grid(row =rowCount+1 ,columnspan=2,sticky=tk.NW, column=0,pady = 1)

    app = OptionMenuDemoFor(canvasfunc,rowCount+1,2)

    otherText.config(justify= 'right',width = 5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
        #add_placeholder_to(otherText, 'Other int')
    otherText.grid(row =rowCount+1,columnspan=2,sticky=tk.NW, column=4,pady =1)
    # add_placeholder_to(otherText, '1')



    colconfig = (canvasfucnwidth-80)/7
    canvasfunc.columnconfigure(0, minsize = 80)
    canvasfunc.columnconfigure(1, minsize = colconfig-5)
    canvasfunc.columnconfigure(2, minsize = colconfig-5)
    canvasfunc.columnconfigure(3, minsize = colconfig-5)
    canvasfunc.columnconfigure(4, minsize = colconfig-5)
    canvasfunc.columnconfigure(5, minsize = colconfig-5)
    canvasfunc.columnconfigure(6, minsize = colconfig-5)
    canvasfunc.columnconfigure(7, minsize = colconfig-5)
    # colconfig = canvasfucnwidth/8
    # canvasfunc.columnconfigure('all', minsize = colconfig)


    #rowCount =rowCount+1
        # add_placeholder_to(otherText, '1')



    # rowCount = canvasfunc.grid_size()[0]
    # rowCount = rowCount+1
def functionForLoop(svfor,number,test):
    global rowCount
    global Printforloop

    ival = itext.get()
    jval = jtext.get()

    # ival = find_in_grid(canvasfunc, number, 1).get()
    # jval = find_in_grid(canvasfunc, number, 2).get()
    opr = svfor.get()

    time_string = time.strftime('%H:%M:%S')
    curdatetime = datetime.datetime.today()
    otherval = otherText.get()
    # otherval = find_in_grid(canvasfunc, number+1, 2).get()
    try:
        for x in range(int(ival),int(jval)):
            if(opr == "+"):

                Xresult = int(x)+int(otherval)
                outputtext.insert(END,  str(str(x)+"+"+str(otherval)+"="+str(Xresult))+'\n')
                if(x == (int(jval)-1)):
                    outputtext.insert(END,  str("End Loop"+".............."+str(curdatetime.year)+"-"+str(curdatetime.month)+"-"+str(curdatetime.day)+"/"+str(time_string))+'\n')
            if(opr == "-"):
                Xresult = int(x)-int(otherval)
                outputtext.insert(END, str(str(x)+"-"+str(otherval)+"="+str(Xresult))+'\n')
                if(x == (int(jval)-1)):
                    outputtext.insert(END,  str("End Loop"+".............."+str(curdatetime.year)+"-"+str(curdatetime.month)+"-"+str(curdatetime.day)+"/"+str(time_string))+'\n')
            if(opr == "*"):
                Xresult = int(x)*int(otherval)
                outputtext.insert(END, str(str(x)+"*"+str(otherval)+"="+str(Xresult))+'\n')
                if(x == (int(jval)-1)):
                    outputtext.insert(END,  str("End Loop"+".............."+str(curdatetime.year)+"-"+str(curdatetime.month)+"-"+str(curdatetime.day)+"/"+str(time_string))+'\n')
            if(opr == "/"):
                Xresult = float(x)/float(otherval)
                outputtext.insert(END, str(str(x)+"/"+str(otherval)+"="+str(Xresult))+'\n')
                if(x == (int(jval)-1)):
                    outputtext.insert(END,  str("End Loop"+".............."+str(curdatetime.year)+"-"+str(curdatetime.month)+"-"+str(curdatetime.day)+"/"+str(time_string))+'\n')

    except ValueError:
        if(not(ival.isdigit()) or not(jval.isdigit())):
            ForInvalidInput()
        if(int(ival) == "" or int(jval) == "" or int(ival) == "Int A" or int(jval) == "Int B" ):

            emptyfields()
    def clearlog():
        outputtext.delete('1.0', END)
    Reset = Button(canvasleft,bg="#f2f2f2", text ="Clear Log",image = clearlogimage, compound= "left",command = clearlog,width=Buttonwidth,height=0,pady = -800)

    Reset.grid(row=4,column=5,pady=2)
def btncancelfor(om,number,test):
    global Proceedrec
    global itext
    global jtext
    global cancelfor
    global forlabel
    global forinitiallabel
    global forfinallabel
    global Printforloop
    global construct
    if(construct == 1):
        clear_all()
        construct = 0




    if(omfor.winfo_exists()):
        omfor.grid_forget()

    if(Printforloop.winfo_exists):
        Printforloop.grid_forget()
        Printforloop.grid_remove()
    if(otherText.winfo_exists()):

        otherText.grid_forget()
        otherText.grid_remove()
    if(Proceedfor.winfo_exists()):
        Proceedfor.grid_forget()


    Proceedrec.grid_remove()
    Proceedrec.grid_forget()
    for item in canvasfunc.grid_slaves():
        if int(item.grid_info()["row"]) == number:
            item.grid_forget()
################################END FOR LOOP #############################################################

################################ IF- ELSE LOOP #############################################################
class OptionMenuDemoif:
    def __init__(self, aWindow,row,col):
       global rowCount
       global Executeif
       #A list of string options for the optionMenu
       OPTIONS = ["Signs","<",">","==","<=",">="]
       self.sv = StringVar()

       #Set CS4400 to be the default
       self.sv.set(OPTIONSIF[0] )

       omif = OptionMenu( aWindow, self.sv, *OPTIONSIF)
       omif.grid(row=row,column= col,columnspan=2,sticky=tk.NW,pady = 8)
       omif.config(height=0,bd=0,highlightthickness=0,width=7)
       # self.b = Button(aWindow,text=setVal,command=lambda: optionChanged2(self.sv,1,2))
       Executeif.config(text ="Proceed",command =lambda row=rowCount, column=6: exceuteifelse(self.sv,row, column),fg = "white"  ,bg = "#ab4345",width=10,height=0)
       Executeif.grid(row =rowCount+3, sticky=tk.NW,column=6,pady = 10)
def ifElse():
    global construct
    construct = 1
    global aLabel
    global bLabel

    global aText
    global bText
    global rowCount
    global cancelif
    global varif
    global Proceedif
    global drop_menuifelse
    global itext
    global jtext
    global cancelfor
    global forlabel
    global forinitiallabel
    global forfinallabel
    global varif
    global Printlabel
    global Elsemessage
    global PrintText2
    global PrintText1

    l1nestedif.grid_remove()
    l2nestedif.grid_remove()
    l3nestedif.grid_remove()
    l1nestedif.grid_remove()
    o1nestedif.grid_remove()
    ment = StringVar()
    valment = StringVar()

    clear_all()



    amessage.set("If")
    # for i in range(1):
    iflabel.config(textvariable=amessage)
    iflabel.grid(row = rowCount , column=0,pady = 10,sticky=tk.NW,padx=20)

    aText = Entry(canvasfunc)
    aText.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
    aText.grid(row =rowCount,columnspan=2,sticky=tk.NW, column=1,pady = 10)
    add_placeholder_to(aText, 'Int A')

    app = OptionMenuDemoif(canvasfunc,rowCount,3)

    bText = Entry(canvasfunc)
    bText.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
    bText.grid(row =rowCount,columnspan=2,sticky=tk.NW, column=5,pady = 10,padx=(5,0))
    add_placeholder_to(bText, 'Int B')

    printmess.set("Print:")
    Printlabel.config(textvariable = printmess)
    Printlabel.grid(row = rowCount+1 ,sticky=tk.NW, column=0,pady = 1,padx=20)

    PrintText1 = Entry(canvasfunc)
    PrintText1.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
    PrintText1.grid(row =rowCount+1,sticky=tk.NW, column=1,columnspan=6,pady = 1)
    add_placeholder_to(PrintText1, 'Hi')



    Elsemes.set("Else:")
    Elsemessage.config(textvariable=Elsemes)
    Elsemessage.grid(row = rowCount+2 ,sticky=tk.NW, columnspan=7,column=0,pady = 10,padx=20)

    Printlabel1.config(textvariable = printmess)
    Printlabel1.grid(row = rowCount+3 , sticky=tk.NW,column=0,pady = 5,padx=20)

    PrintText2 = Entry(canvasfunc)
    PrintText2.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
    PrintText2.grid(row =rowCount+3,sticky=tk.NW,columnspan=4, column=1,pady = 2)
    add_placeholder_to(PrintText2, 'Hello')



    cancelif.config(image = close,command=lambda row=rowCount, column=7: deleteif(row, column))
    cancelif.grid(row = rowCount, pady = 10,padx=(0,20),sticky=tk.NW,column=7)
    cancelif.config(bd=0, highlightthickness=0,bg = "White")

    # colconfig = canvasfucnwidth/10
    # canvasfunc.columnconfigure('all', minsize = colconfig)

    colconfig = (canvasfucnwidth-80)/8
    canvasfunc.columnconfigure(0, minsize = 80)
    canvasfunc.columnconfigure(1, minsize = colconfig-3)
    canvasfunc.columnconfigure(2, minsize = colconfig-3)
    canvasfunc.columnconfigure(3, minsize = colconfig-3)
    canvasfunc.columnconfigure(4, minsize = colconfig-3)
    canvasfunc.columnconfigure(5, minsize = colconfig-3)
    canvasfunc.columnconfigure(6, minsize = colconfig-3)
    canvasfunc.columnconfigure(7, minsize = colconfig-3)
    # rowCount = rowCount + 1
def exceuteifelse(svopr,number, test):
    global varif
    global Proceedif
    global drop_menuifelse
    global iflabel
    global varnestif1
    global val1
    global val2
    global Elsemessage
    global Printlabel1
    global rowCount
    global Printlabel2
    global cancelfor
    l1nestedif.grid_remove()
    l2nestedif.grid_remove()
    l3nestedif.grid_remove()
    l1nestedif.grid_remove()
    o1nestedif.grid_remove()
    ifmessage.set("If")
    Elsemes.set("Else:")
    if_oprval  = svopr.get()
    if_aval = aText.get()
    if_bval = bText.get()
    if_PrintText2 = PrintText2.get()
    if_PrintText1 = PrintText1.get()
    # if(if_oprval == "Operators"):
    #     shapesfeildsempty()
    if(not(if_aval.isdigit()) or not(if_bval.isdigit())):
        InvalidInput()
    if(int(if_aval) == "" or int(if_bval) == "" ):
        shapesfeildsempty()

    try:
        if(len(if_aval) != 0 and len(if_bval) != 0):

            if(if_aval.isdigit() and if_bval.isdigit()):
                if(if_oprval == "<"):

                    if(int(if_aval) < int(if_bval)):
                        outputtext.insert(END, str(if_PrintText1)+ '\n')
                    else:
                        outputtext.insert(END, str(if_PrintText2)+ '\n')
                elif(if_oprval == ">"):
                    if(int(if_aval) > int(if_bval)):
                        outputtext.insert(END, str(if_PrintText1)+ '\n')
                    else:
                        outputtext.insert(END, str(if_PrintText2)+ '\n')
                elif(if_oprval == "=="):
                    if(int(if_aval) == int(if_bval)):
                        outputtext.insert(END, str(if_PrintText1)+ '\n')
                    else:
                        outputtext.insert(END, str(if_PrintText2)+ '\n')
                elif(if_oprval == ">="):
                    if(int(if_aval) >= int(if_bval)):
                        outputtext.insert(END, str(if_PrintText1)+ '\n')
                    else:
                        outputtext.insert(END, str(if_PrintText2)+ '\n')
                elif(if_oprval == "<="):

                    if(int(if_aval) <= int(if_bval)):
                        outputtext.insert(END, str(if_PrintText1)+ '\n')
                    else:
                        outputtext.insert(END, str(if_PrintText2)+ '\n')
    except ValueError:
        if(not(if_aval.isdigit()) or not(if_bval.isdigit())):
            InvalidInput()
        if(int(if_avalif_aval) == "" or int(if_bval) == ""):
            emptyfields()
def deleteif(number,test):

    global drop_menuifelse
    global iflabel
    global Elsemessage
    global val1
    global val2
    global Print1
    global Print2
    global Printlabel
    global Proceedif
    global PrintText2
    global PrintText1
    global construct

    if(construct == 1):
        clear_all()

    construct = 0



    if(PrintText1.winfo_exists()):
        PrintText1.grid_forget()
        PrintText1.grid_remove()
    if(PrintText2.winfo_exists()):
        PrintText2.grid_forget()
        PrintText2.grid_remove()
    if(Printlabel.winfo_exists()):
        Printlabel.grid_remove()
    if(iflabel.winfo_exists()):
        iflabel.grid_remove()
    if(Elsemessage.winfo_exists()):
        Elsemessage.grid_remove()

    if(omif.winfo_exists()):
        omif.grid_forget()
        omif.grid_remove()

    if(Executeif.winfo_exists()):

        Executeif.grid_remove()
        Executeif.grid_forget()
    if(Printlabel1.winfo_exists()):
        Printlabel1.grid_remove()
        Printlabel1.grid_forget()
    for item in canvasfunc.grid_slaves():
        if int(item.grid_info()["row"]) == number:
            item.grid_forget()

######################################## END IF-ELSE #####################################################
######################################### Nested if else ###################################################
add_placeholder_to(resultif, 'Hello')
add_placeholder_to(resultelseif, 'Hi')
add_placeholder_to(resultelseif1, 'case2')
add_placeholder_to(resultelseif2, 'case3')
add_placeholder_to(resultelseif3, 'case4')
add_placeholder_to(resultelseif4, 'case5')
add_placeholder_to(resultelse, 'Default')
add_placeholder_to(resultelse1, 'Default')
add_placeholder_to(resultelse2, 'Default')
add_placeholder_to(resultelse3, 'Default')
add_placeholder_to(resultelse4, 'Default')
add_placeholder_to(Entr_ValF, 'Int F')
add_placeholder_to(Entr_ValG, 'Int G')
add_placeholder_to(Entr_ValB, 'Int B')
add_placeholder_to(Entr_ValC, 'Int C')
add_placeholder_to(Entr_ValD, 'Int D')
add_placeholder_to(Entr_ValE, 'Int E')


class CreateToolTip(object):
    '''
    create a tooltip for a given widget
    '''
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background='#47a3a5', relief='solid', borderwidth=0,
                       font=("times", "10", "normal"))
        label.pack(ipadx=1)
    def close(self, event=None):
        if self.tw:
            self.tw.destroy()
class OptionMenuDemonestedIf:
    def __init__(self, aWindow,row,col):
       global rowCount
       global Executeif
       global omnestedif
       global omnestedif1
       global omnestedif2
       global omnestedif3
       global omnestedif4
       global omnestedif5
       global svnestif
       global svnestif1
       global svnestif2
       global svnestif3
       global svnestif4
       global svnestif5



       nestedelsemessage.set("Elseif")
       elsemess.set("Else")

       ifmess.set("If")
       elseifmess.set("Elseif")
       elsemess.set("Else")
       Printmess1.set("Print")
       Printmess2.set("Print")
       Printmess3.set("Print")
       Printmess4.set("Print")
       Printmess5.set("Print")
       add_placeholder_to(Entr_ValA, 'Int A')
       add_placeholder_to(Entr_ValA1, 'Int A1')
       add_placeholder_to(Entr_ValA2, 'Int A2')
       add_placeholder_to(Entr_ValA3, 'Int A3')
       add_placeholder_to(Entr_ValA4, 'Int A4')
       add_placeholder_to(Entr_ValA5, 'Int A5')

       OPTIONS = ["Operators","<",">","==","<=",">="]
       OPTIONSnestedcases = ["1","2","3","4","5"]
       OPTIONSNESTEDIF = ["Operators","<",">","==","<=",">="]

       Dic={'1':1,'1 to 2':2,'1 to 3':3,'1 to 4':4,'1 to 5':5}
       # Dic = sorted(Dic.keys())
       self.svcase = StringVar()
       self.svcase.set("Loops")






       def OPTIONSNestedCases(*args):
           global entervalue
           entervalue = self.svcase.get()

           if(entervalue == "1"):

               omnestedif2.grid_remove()
               omnestedif3.grid_remove()
               omnestedif4.grid_remove()
               omnestedif5.grid_remove()
               lbl_elIf1.grid_forget()
               Entr_ValA2.grid_forget()
               Entr_ValD.grid_forget()
               nestPrintlbl3.grid_forget()
               resultelseif1.grid_forget()
               omnestedif2.grid_remove()
               omnestedif3.grid_remove()
               omnestedif4.grid_remove()
               omnestedif5.grid_remove()
               # omnestedif3.grid_forget()
               lbl_elIf2.grid_forget()
               Entr_ValA3.grid_forget()
               Entr_ValE.grid_forget()
               nestPrintlbl4.grid_forget()
               resultelseif2.grid_forget()
               # omnestedif4.grid_forget()
               lbl_elIf3.grid_forget()
               Entr_ValA4.grid_forget()
               Entr_ValF.grid_forget()
               nestPrintlbl5.grid_forget()
               resultelseif3.grid_forget()
               # omnestedif5.grid_forget()
               lbl_elIf4.grid_forget()
               Entr_ValA5.grid_forget()
               Entr_ValG.grid_forget()
               nestPrintlbl6.grid_forget()
               resultelseif4.grid_forget()
               lbl_el4.grid_forget()
               nestPrintlbldefault4.grid_forget()
               resultelse4.grid_forget()
               Executenested.grid_forget()
               lbl_elIf1.grid_forget()
               Entr_ValA2.grid_forget()
               lbl_el1.grid_forget()
               nestPrintlbldefault1.grid_forget()
               resultelse1.grid_forget()
               Executenested.grid_forget()
               lbl_elIf3.grid_forget()
               Entr_ValA4.grid_forget()
               Entr_ValF.grid_forget()
               nestPrintlbl5.grid_forget()
               resultelseif3.grid_forget()
               lbl_el3.grid_forget()
               nestPrintlbldefault3.grid_forget()
               resultelse3.grid_forget()
           if(entervalue == "1 to 2"):

               omnestedif3.grid_remove()
               omnestedif3.grid_forget()
               omnestedif4.grid_remove()
               omnestedif5.grid_remove()
               lbl_elIf2.grid_forget()
               Entr_ValA3.grid_forget()
               Entr_ValE.grid_forget()
               omnestedif3.grid_remove()
               omnestedif3.grid_forget()
               omnestedif4.grid_remove()
               omnestedif5.grid_remove()
               nestPrintlbl4.grid_forget()
               resultelseif2.grid_forget()
               omnestedif4.grid_forget()
               lbl_elIf3.grid_forget()
               Entr_ValA4.grid_forget()
               Entr_ValF.grid_forget()
               nestPrintlbl5.grid_forget()
               resultelseif3.grid_forget()
               lbl_el3.grid_forget()
               nestPrintlbldefault3.grid_forget()
               resultelse3.grid_forget()
               Executenested.grid_forget()
               omnestedif5.grid_forget()
               lbl_elIf4.grid_forget()
               Entr_ValA5.grid_forget()
               Entr_ValG.grid_forget()
               nestPrintlbl6.grid_forget()
               resultelseif4.grid_forget()
               lbl_el4.grid_forget()
               nestPrintlbldefault4.grid_forget()
               resultelse4.grid_forget()
               Executenested.grid_forget()
               lbl_el1.grid_forget()
               nestPrintlbldefault1.grid_forget()
               resultelse1.grid_forget()
               omnestedif3.grid_forget()
               lbl_elIf2.grid_forget()
               Entr_ValA3.grid_forget()
               Entr_ValE.grid_forget()
               nestPrintlbl4.grid_forget()
               lbl_el2.grid_forget()
               nestPrintlbldefault2.grid_forget()
               resultelse2.grid_forget()
               lbl_el.grid_forget()
               nestPrintlbldefault.grid_forget()
               resultelse.grid_forget()
               Executenested.grid_forget()
           if(entervalue=="1 to 3"):

               omnestedif4.grid_remove()
               omnestedif5.grid_remove()
               lbl_elIf2.grid_forget()
               Entr_ValA3.grid_forget()
               Entr_ValE.grid_forget()
               omnestedif4.grid_remove()
               omnestedif5.grid_remove()
               nestPrintlbl4.grid_forget()
               resultelseif2.grid_forget()
               omnestedif4.grid_forget()
               lbl_elIf3.grid_forget()
               Entr_ValA4.grid_forget()
               Entr_ValF.grid_forget()
               nestPrintlbl5.grid_forget()
               resultelseif3.grid_forget()
               lbl_el3.grid_forget()
               nestPrintlbldefault3.grid_forget()
               resultelse3.grid_forget()
               Executenested.grid_forget()
               omnestedif5.grid_forget()
               lbl_elIf4.grid_forget()
               Entr_ValA5.grid_forget()
               Entr_ValG.grid_forget()
               nestPrintlbl6.grid_forget()
               resultelseif4.grid_forget()
               lbl_el4.grid_forget()
               nestPrintlbldefault4.grid_forget()
               resultelse4.grid_forget()
               Executenested.grid_forget()
               lbl_el1.grid_forget()
               nestPrintlbldefault1.grid_forget()
               resultelse1.grid_forget()
           if(entervalue == "1 to 4"):

               omnestedif5.grid_remove()

               lbl_elIf4.grid_forget()
               Entr_ValA5.grid_forget()
               Entr_ValG.grid_forget()
               nestPrintlbl6.grid_forget()
               resultelseif4.grid_forget()
               lbl_el4.grid_forget()
               nestPrintlbldefault4.grid_forget()
               resultelse4.grid_forget()
               Executenested.grid_forget()
               lbl_el1.grid_forget()
               nestPrintlbldefault1.grid_forget()
               resultelse1.grid_forget()
               lbl_el1.grid_forget()
               nestPrintlbldefault1.grid_forget()
               resultelse1.grid_forget()
               lbl_el2.grid_forget()
               nestPrintlbldefault2.grid_forget()
               resultelse2.grid_forget()


           if(entervalue == "1"):

               lbl_If.config(textvariable=ifmess)
               lbl_If.grid(row = 0 , sticky=tk.NW,column=0,pady = 10,padx=20)



               v = StringVar()
               textvariable=v

               omnestedif.grid(row=0,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
               omnestedif.config(height=0,bd=0,highlightthickness=0,width=7)
               omnestedif1.grid(row=2,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
               omnestedif1.config(height=0,bd=0,highlightthickness=0,width=7)

               #Entr_ValA = Entry(canvasfunc)
               Entr_ValA.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               Entr_ValA.grid(row =0, columnspan=2,column=1,pady = 10)
               # add_placeholder_to(Entr_ValA, 'Int A')


               # app = OptionMenuDemonestedIf(canvasfunc,rowCount,3)

               #Entr_ValB = Entry(canvasfunc)
               Entr_ValB.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               Entr_ValB.grid(row =0, sticky=tk.NW, column=5,pady = 10)



               nestPrintlbl1.config(textvariable=Printmess1)
               nestPrintlbl1.grid(row = 1 , sticky=tk.NW,columnspan=2, column=0,pady = 10,padx=20)


               resultif.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               resultif.grid(row =1, sticky=tk.NW, column=2,columnspan=5,pady = 10)
                       ########## elif row####################################################

               elifmess.set("Elseif")


               lbl_elIf.config(textvariable=elifmess)
               lbl_elIf.grid(row = 2 , sticky=tk.NW, column=0,pady = 10,padx=20)

               Entr_ValA1.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               Entr_ValA1.grid(row =2, sticky=tk.NW,columnspan=2, column=1,pady = 10)
               add_placeholder_to(Entr_ValA1, 'Int A')

                   # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
              # Entr_ValC = Entry(canvasfunc)
               Entr_ValC.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               Entr_ValC.grid(row =2, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))

               nestPrintlbl2.config(textvariable=Printmess1)
               nestPrintlbl2.grid(row = 3 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)


               resultelseif.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               resultelseif.grid(row =3,  sticky=tk.NW,column=2,columnspan=5,pady = 10)


               elmess.set("Else")
               lbl_el.config(textvariable=elmess)
               lbl_el.grid(row = 4 , sticky=tk.NW, column=0,pady = 10,padx=20)

               nestPrintlbldefault.config(textvariable=Printmess1)
               nestPrintlbldefault.grid(row = 5 , sticky=tk.NW,columnspan=2, column=0,pady = 10,padx=20)


               resultelse.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               resultelse.grid(row =5, sticky=tk.NW, columnspan=5,column=2,pady = 10)

               Executenested.config(text ="Proceed",command =lambda row=rowCount, column=7: exceutenestedifelse1(svnestif,svnestif1,row, column),fg = "white",bg = "#ab4345",width=7)
               Executenested.grid(row = 5, column=6, sticky =tk.NW)
           elif(entervalue == "1 to 2"):


               omnestedif.grid(row=0,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
               omnestedif.config(height=0,bd=0,highlightthickness=0,width=7)
               omnestedif1.grid(row=2,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
               omnestedif1.config(height=0,bd=0,highlightthickness=0,width=7)
               omnestedif2.grid(row=4,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
               omnestedif2.config(height=0,bd=0,highlightthickness=0,width=7)

               v = StringVar()
               textvariable=v


               lbl_If.config(textvariable=ifmess)
               lbl_If.grid(row = 0 , sticky=tk.NW,column=0,pady = 10,padx=20)

               #Entr_ValA = Entry(canvasfunc)
               Entr_ValA.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               Entr_ValA.grid(row =0,  sticky=tk.NW,columnspan=2,column=1,pady = 10)
               add_placeholder_to(Entr_ValA, 'Int A')

               Entr_ValB.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               Entr_ValB.grid(row =0, sticky=tk.NW, column=5,pady = 10)

               nestPrintlbl1.config(textvariable=Printmess1)
               nestPrintlbl1.grid(row = 1 , sticky=tk.NW,columnspan=2, column=0,pady = 10,padx=20)


               resultif.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               resultif.grid(row =1, sticky=tk.NW, column=2,columnspan=5,pady = 10)
                       ########## elif row####################################################

               elifmess.set("Elseif")
               # omnestedif1 = OptionMenu( aWindow, self.sv1, *OPTIONS)
               omnestedif1.grid(row=2,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
               omnestedif1.config(height=0,bd=0,highlightthickness=0,width=7)

               lbl_elIf.config(textvariable=elifmess)
               lbl_elIf.grid(row = 2 , sticky=tk.NW, column=0,pady = 10,padx=20)

               Entr_ValA1.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               Entr_ValA1.grid(row =2, sticky=tk.NW,columnspan=2, column=1,pady = 10)
               add_placeholder_to(Entr_ValA1, 'Int A')

                   # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
               #Entr_ValC = Entry(canvasfunc)
               Entr_ValC.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               Entr_ValC.grid(row =2, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


               nestPrintlbl2.config(textvariable=Printmess1)
               nestPrintlbl2.grid(row = 3 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

               resultelseif.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               resultelseif.grid(row =3,  sticky=tk.NW,column=2,columnspan=5,pady = 10)

               ################### elif level 2 ################################################

               elifmess1.set("Elseif")
               #omnestedif2 = OptionMenu( aWindow, self.sv1, *OPTIONS)
               omnestedif2.grid(row=4,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
               omnestedif2.config(height=0,bd=0,highlightthickness=0,width=7)

               lbl_elIf1.config(textvariable=elifmess1)
               lbl_elIf1.grid(row = 4 , sticky=tk.NW, column=0,pady = 10,padx=20)

               Entr_ValA2.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               Entr_ValA2.grid(row =4, sticky=tk.NW,columnspan=2, column=1,pady = 10)
               add_placeholder_to(Entr_ValA2, 'Int A')

                   # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
              # Entr_ValD = Entry(canvasfunc)
               Entr_ValD.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               Entr_ValD.grid(row =4, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


               nestPrintlbl3.config(textvariable=Printmess1)
               nestPrintlbl3.grid(row = 5 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

               resultelseif1.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               resultelseif1.grid(row =5,  sticky=tk.NW,column=2,columnspan=5,pady = 10)


               ####### else #######################################################
               elmess.set("Else")
               lbl_el1.config(textvariable=elmess)
               lbl_el1.grid(row = 6 , sticky=tk.NW, column=0,pady = 10,padx=20)

               nestPrintlbldefault1.config(textvariable=Printmess1)
               nestPrintlbldefault1.grid(row = 7 , sticky=tk.NW,columnspan=2, column=0,pady = 10,padx=20)


               resultelse1.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               resultelse1.grid(row =7, sticky=tk.NW, columnspan=5,column=2,pady = 10)

               Executenested.config(text ="Proceed",command =lambda row=rowCount, column=7: exceutenestedifelse2(svnestif,svnestif1,svnestif2,row, column),fg = "white",bg = "#ab4345",width=7)
               Executenested.grid(row = 7, column=6, sticky =tk.NW)
           elif(entervalue == "1 to 3"):

                nestPrintlbldefault1.grid_forget()
                resultelse1.grid_forget()
                lbl_el1.grid_forget()








                omnestedif.grid(row=0,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
                omnestedif.config(height=0,bd=0,highlightthickness=0,width=7)
                omnestedif1.grid(row=2,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif1.config(height=0,bd=0,highlightthickness=0,width=7)
                omnestedif2.grid(row=4,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
                omnestedif2.config(height=0,bd=0,highlightthickness=0,width=7)
                omnestedif3.grid(row=6,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
                omnestedif3.config(height=0,bd=0,highlightthickness=0,width=7)






                lbl_If.config(textvariable=ifmess)
                lbl_If.grid(row = 0 , sticky=tk.NW,column=0,pady = 10,padx=20)
                v = StringVar()
                textvariable=v

                #Entr_ValA = Entry(canvasfunc)
                Entr_ValA.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA.grid(row =0,  sticky=tk.NW,columnspan=2,column=1,pady = 10)
                add_placeholder_to(Entr_ValA, 'Int A')


                # app = OptionMenuDemonestedIf(canvasfunc,rowCount,3)

                #Entr_ValB = Entry(canvasfunc)
                Entr_ValB.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValB.grid(row =0, sticky=tk.NW, column=5,pady = 10)


                nestPrintlbl1.config(textvariable=Printmess1)
                nestPrintlbl1.grid(row = 1 , sticky=tk.NW,columnspan=2, column=0,pady = 10,padx=20)


                resultif.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultif.grid(row =1, sticky=tk.NW, column=2,columnspan=5,pady = 10)
                        ########## elif row####################################################

                elifmess.set("Elseif")
                # omnestedif1 = OptionMenu( aWindow, self.sv1, *OPTIONS)
                omnestedif1.grid(row=2,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif1.config(height=0,bd=0,highlightthickness=0,width=7)

                lbl_elIf.config(textvariable=elifmess)
                lbl_elIf.grid(row = 2 , sticky=tk.NW, column=0,pady = 10,padx=20)

                Entr_ValA1.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA1.grid(row =2, sticky=tk.NW,columnspan=2, column=1,pady = 10)
                add_placeholder_to(Entr_ValA1, 'Int A')

                    # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
                #Entr_ValC = Entry(canvasfunc)
                Entr_ValC.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValC.grid(row =2, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


                nestPrintlbl2.config(textvariable=Printmess1)
                nestPrintlbl2.grid(row = 3 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

                resultelseif.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelseif.grid(row =3,  sticky=tk.NW,column=2,columnspan=5,pady = 10)

                ################### elif level 2 ################################################

                elifmess1.set("Elseif")
                #omnestedif2 = OptionMenu( aWindow, self.sv1, *OPTIONS)
                omnestedif2.grid(row=4,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif2.config(height=0,bd=0,highlightthickness=0,width=7)

                lbl_elIf1.config(textvariable=elifmess1)
                lbl_elIf1.grid(row = 4 , sticky=tk.NW, column=0,pady = 10,padx=20)

                Entr_ValA2.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA2.grid(row =4, sticky=tk.NW,columnspan=2, column=1,pady = 10)
                add_placeholder_to(Entr_ValA2, 'Int A')

                    # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
                #Entr_ValD = Entry(canvasfunc)
                Entr_ValD.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValD.grid(row =4, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


                nestPrintlbl3.config(textvariable=Printmess1)
                nestPrintlbl3.grid(row = 5 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

                resultelseif1.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelseif1.grid(row =5,  sticky=tk.NW,column=2,columnspan=5,pady = 10)


                ################### elif level 3 ################################################

                elifmess2.set("Elseif")
                omnestedif3.grid(row=6,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif3.config(height=0,bd=0,highlightthickness=0,width=7)

                lbl_elIf2.config(textvariable=elifmess2)
                lbl_elIf2.grid(row = 6 , sticky=tk.NW, column=0,pady = 10,padx=20)

                Entr_ValA3.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA3.grid(row =6, sticky=tk.NW,columnspan=2, column=1,pady = 10)
                add_placeholder_to(Entr_ValA3, 'Int A')

                    # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
                #Entr_ValE = Entry(canvasfunc)
                Entr_ValE.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValE.grid(row =6, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


                nestPrintlbl4.config(textvariable=Printmess2)
                nestPrintlbl4.grid(row = 7 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

                resultelseif2.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelseif2.grid(row =7,  sticky=tk.NW,column=2,columnspan=5,pady = 10)

                 ####### else #######################################################
                elmess.set("Else")
                lbl_el2.config(textvariable=elmess)
                lbl_el2.grid(row = 8 , sticky=tk.NW, column=0,pady = 10,padx=20)

                nestPrintlbldefault2.config(textvariable=Printmess3)
                nestPrintlbldefault2.grid(row = 9 , sticky=tk.NW,columnspan=2, column=0,pady = 10,padx=20)

                resultelse2.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelse2.grid(row =9, sticky=tk.NW, columnspan=5,column=2,pady = 10)

                Executenested.config(text ="Proceed",command =lambda row=rowCount, column=6: exceutenestedifelse3(svnestif,svnestif1,svnestif2,svnestif3,row, column),fg = "white",bg = "#ab4345",width=7)
                Executenested.grid(row = 9, column=6, sticky =tk.NW)
           elif(entervalue == "1 to 4"):

                lbl_If.config(textvariable=ifmess)
                lbl_If.grid(row = 0 , sticky=tk.NW,column=0,pady = 10,padx=20)
                v = StringVar()
                textvariable=v



                lbl_If.config(textvariable=ifmess)
                lbl_If.grid(row = 0 , sticky=tk.NW,column=0,pady = 10,padx=20)


                omnestedif.grid(row=0,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
                omnestedif.config(height=0,bd=0,highlightthickness=0,width=7)
                omnestedif1.grid(row=2,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif1.config(height=0,bd=0,highlightthickness=0,width=7)
                omnestedif2.grid(row=4,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
                omnestedif2.config(height=0,bd=0,highlightthickness=0,width=7)
                omnestedif3.grid(row=6,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
                omnestedif3.config(height=0,bd=0,highlightthickness=0,width=7)
                omnestedif4.grid(row=7,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
                omnestedif4.config(height=0,bd=0,highlightthickness=0,width=7)

                #Entr_ValA = Entry(canvasfunc)
                Entr_ValA.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA.grid(row =0,  sticky=tk.NW,columnspan=2,column=1,pady = 10)
                add_placeholder_to(Entr_ValA, 'Int A')

                #
                # app = OptionMenuDemonestedIf(canvasfunc,rowCount,3)

                #Entr_ValB = Entry(canvasfunc)
                Entr_ValB.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValB.grid(row =0, sticky=tk.NW, column=5,pady = 10)


                nestPrintlbl1.config(textvariable=Printmess1)
                nestPrintlbl1.grid(row = 1 , sticky=tk.NW,columnspan=2, column=0,pady = 10,padx=20)


                resultif.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultif.grid(row =1, sticky=tk.NW, column=2,columnspan=5,pady = 10)
                        ########## elif row####################################################

                elifmess.set("Elseif")
                #omnestedif1 = OptionMenu( aWindow, self.sv1, *OPTIONS)
                omnestedif1.grid(row=2,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif1.config(height=0,bd=0,highlightthickness=0,width=7)

                lbl_elIf.config(textvariable=elifmess)
                lbl_elIf.grid(row = 2 , sticky=tk.NW, column=0,pady = 10,padx=20)

                Entr_ValA1.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA1.grid(row =2, sticky=tk.NW,columnspan=2, column=1,pady = 10)
                add_placeholder_to(Entr_ValA1, 'Int A')

                    # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
                #Entr_ValC = Entry(canvasfunc)
                Entr_ValC.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValC.grid(row =2, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


                nestPrintlbl2.config(textvariable=Printmess1)
                nestPrintlbl2.grid(row = 3 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

                resultelseif.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelseif.grid(row =3,  sticky=tk.NW,column=2,columnspan=5,pady = 10)

                ################### elif level 2 ################################################

                elifmess1.set("Elseif")
                #omnestedif2 = OptionMenu( aWindow, self.sv1, *OPTIONS)
                omnestedif2.grid(row=4,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif2.config(height=0,bd=0,highlightthickness=0,width=7)

                lbl_elIf1.config(textvariable=elifmess1)
                lbl_elIf1.grid(row = 4 , sticky=tk.NW, column=0,pady = 10,padx=20)

                Entr_ValA2.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA2.grid(row =4, sticky=tk.NW,columnspan=2, column=1,pady = 10)
                add_placeholder_to(Entr_ValA2, 'Int A')

                    # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
                #Entr_ValD = Entry(canvasfunc)
                Entr_ValD.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValD.grid(row =4, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


                nestPrintlbl3.config(textvariable=Printmess1)
                nestPrintlbl3.grid(row = 5 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

                resultelseif1.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelseif1.grid(row =5,  sticky=tk.NW,column=2,columnspan=5,pady = 10)


                ################### elif level 3 ################################################

                elifmess2.set("Elseif")
                #omnestedif2 = OptionMenu( aWindow, self.sv1, *OPTIONS)
                omnestedif3.grid(row=6,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif3.config(height=0,bd=0,highlightthickness=0,width=7)

                lbl_elIf2.config(textvariable=elifmess2)
                lbl_elIf2.grid(row = 6 , sticky=tk.NW, column=0,pady = 10,padx=20)

                Entr_ValA3.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA3.grid(row =6, sticky=tk.NW,columnspan=2, column=1,pady = 10)
                add_placeholder_to(Entr_ValA3, 'Int A')

                    # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
                #Entr_ValE = Entry(canvasfunc)
                Entr_ValE.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValE.grid(row =6, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


                nestPrintlbl4.config(textvariable=Printmess2)
                nestPrintlbl4.grid(row = 7 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

                resultelseif2.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelseif2.grid(row =7,  sticky=tk.NW,column=2,columnspan=5,pady = 10)


                ################### elif level 4 ################################################

                elifmess3.set("Elseif")
                #omnestedif2 = OptionMenu( aWindow, self.sv1, *OPTIONS)
                omnestedif4.grid(row=8,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif4.config(height=0,bd=0,highlightthickness=0,width=7)

                lbl_elIf3.config(textvariable=elifmess3)
                lbl_elIf3.grid(row = 8 , sticky=tk.NW, column=0,pady = 10,padx=20)

                Entr_ValA4.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA4.grid(row =8, sticky=tk.NW,columnspan=2, column=1,pady = 10)
                add_placeholder_to(Entr_ValA4, 'Int A')

                    # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
                #Entr_ValF = Entry(canvasfunc)
                Entr_ValF.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValF.grid(row =8, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


                nestPrintlbl5.config(textvariable=Printmess4)
                nestPrintlbl5.grid(row = 9 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

                resultelseif3.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelseif3.grid(row =9,  sticky=tk.NW,column=2,columnspan=5,pady = 10)

                 ####### else #######################################################
                elmess.set("Else")
                lbl_el3.config(textvariable=elmess)
                lbl_el3.grid(row = 10 , sticky=tk.NW, column=0,pady = 10,padx=20)

                nestPrintlbldefault3.config(textvariable=Printmess4)
                nestPrintlbldefault3.grid(row = 11 , sticky=tk.NW,columnspan=2, column=0,pady = 10,padx=20)

                resultelse3.config(justify= 'right',width=11,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelse3.grid(row =11, sticky=tk.NW, columnspan=5,column=2,pady = 10,padx=20)

                Executenested.config(text ="Proceed",command =lambda row=rowCount, column=6: exceutenestedifelse4(svnestif,svnestif1,svnestif2,svnestif3,svnestif4,row, column),fg = "white",bg = "#ab4345",width=7)
                Executenested.grid(row = 11, column=6, sticky =tk.NW)
           elif(entervalue == "1 to 5"):

                lbl_el.grid_forget()

                nestPrintlbldefault.grid_forget()
                resultelse.grid_forget()
                lbl_el1.grid_forget()
                nestPrintlbldefault1.grid_forget()
                resultelse1.grid_forget()

                lbl_el2.grid_forget()
                nestPrintlbldefault2.grid_forget()
                resultelse2.grid_forget()

                lbl_el3.grid_forget()
                nestPrintlbldefault3.grid_forget()
                resultelse3.grid_forget()

                lbl_If.config(textvariable=ifmess)
                lbl_If.grid(row = 0 , sticky=tk.NW,column=0,pady = 10,padx=20)
                v = StringVar()
                textvariable=v


                omnestedif.grid(row=0,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
                omnestedif.config(height=0,bd=0,highlightthickness=0,width=7)
                omnestedif1.grid(row=2,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif1.config(height=0,bd=0,highlightthickness=0,width=7)
                omnestedif2.grid(row=4,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
                omnestedif2.config(height=0,bd=0,highlightthickness=0,width=7)
                omnestedif3.grid(row=6,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
                omnestedif3.config(height=0,bd=0,highlightthickness=0,width=7)
                omnestedif4.grid(row=rowCount+7,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
                omnestedif4.config(height=0,bd=0,highlightthickness=0,width=7)
                omnestedif5.grid(row=8,column= 3,columnspan=2, sticky =tk.NW,pady=10,padx=(0,0))
                omnestedif5.config(height=0,bd=0,highlightthickness=0,width=7)

                #Entr_ValA = Entry(canvasfunc)
                Entr_ValA.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA.grid(row =0,  sticky=tk.NW,columnspan=2,column=1,pady = 10)
                add_placeholder_to(Entr_ValA, 'Int  A')


                #app = OptionMenuDemonestedIf(canvasfunc,rowCount,3)

                #Entr_ValB = Entry(canvasfunc)
                Entr_ValB.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValB.grid(row =0, sticky=tk.NW, column=5,pady = 10)


                nestPrintlbl1.config(textvariable=Printmess1)
                nestPrintlbl1.grid(row = 1 , sticky=tk.NW,columnspan=2, column=0,pady = 10,padx=20)


                resultif.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultif.grid(row =1, sticky=tk.NW, column=2,columnspan=5,pady = 10)
                        ########## elif row####################################################

                elifmess.set("Elseif")
                #omnestedif1 = OptionMenu( aWindow, self.sv1, *OPTIONS)
                omnestedif1.grid(row=2,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif1.config(height=0,bd=0,highlightthickness=0,width=7)

                lbl_elIf.config(textvariable=elifmess)
                lbl_elIf.grid(row = 2 , sticky=tk.NW, column=0,pady = 10,padx=20)

                Entr_ValA1.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA1.grid(row =2, sticky=tk.NW,columnspan=2, column=1,pady = 10)


                    # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
                #Entr_ValC = Entry(canvasfunc)
                Entr_ValC.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValC.grid(row =2, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


                nestPrintlbl2.config(textvariable=Printmess1)
                nestPrintlbl2.grid(row = 3 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

                resultelseif.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelseif.grid(row =3,  sticky=tk.NW,column=2,columnspan=5,pady = 10)

                ################### elif level 2 ################################################

                elifmess1.set("Elseif")
                #omnestedif2 = OptionMenu( aWindow, self.sv1, *OPTIONS)
                omnestedif2.grid(row=4,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif2.config(height=0,bd=0,highlightthickness=0,width=7)

                lbl_elIf1.config(textvariable=elifmess1)
                lbl_elIf1.grid(row = 4 , sticky=tk.NW, column=0,pady = 10,padx=20)

                Entr_ValA2.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA2.grid(row =4, sticky=tk.NW,columnspan=2, column=1,pady = 10)


                    # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
                #Entr_ValD = Entry(canvasfunc)
                Entr_ValD.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValD.grid(row =4, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


                nestPrintlbl3.config(textvariable=Printmess1)
                nestPrintlbl3.grid(row = 5 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

                resultelseif1.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelseif1.grid(row =5,  sticky=tk.NW,column=2,columnspan=5,pady = 10)


                ################### elif level 3 ################################################

                elifmess2.set("Elseif")
                #omnestedif2 = OptionMenu( aWindow, self.sv1, *OPTIONS)
                omnestedif3.grid(row=6,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif3.config(height=0,bd=0,highlightthickness=0,width=7)

                lbl_elIf2.config(textvariable=elifmess2)
                lbl_elIf2.grid(row = 6 , sticky=tk.NW, column=0,pady = 10,padx=20)

                Entr_ValA3.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA3.grid(row =6, sticky=tk.NW,columnspan=2, column=1,pady = 10)


                    # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
                #Entr_ValE = Entry(canvasfunc)
                Entr_ValE.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValE.grid(row =6, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


                nestPrintlbl4.config(textvariable=Printmess2)
                nestPrintlbl4.grid(row = 7 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

                resultelseif2.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelseif2.grid(row =7,  sticky=tk.NW,column=2,columnspan=5,pady = 10)


                ################### elif level 4 ################################################

                elifmess3.set("Elseif")
                #omnestedif2 = OptionMenu( aWindow, self.sv1, *OPTIONS)
                omnestedif4.grid(row=8,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif4.config(height=0,bd=0,highlightthickness=0,width=7)

                lbl_elIf3.config(textvariable=elifmess3)
                lbl_elIf3.grid(row = 8 , sticky=tk.NW, column=0,pady = 10,padx=20)

                Entr_ValA4.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA4.grid(row =8, sticky=tk.NW,columnspan=2, column=1,pady = 10)


                    # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
                #Entr_ValF = Entry(canvasfunc)
                Entr_ValF.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValF.grid(row =8, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


                nestPrintlbl5.config(textvariable=Printmess4)
                nestPrintlbl5.grid(row = 9 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

                resultelseif3.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelseif3.grid(row =9,  sticky=tk.NW,column=2,columnspan=5,pady = 10)


                ################### elif level 5 ################################################

                elifmess4.set("Elseif")
                #omnestedif2 = OptionMenu( aWindow, self.sv1, *OPTIONS)
                omnestedif5.grid(row=10,column= 3,columnspan=2,sticky=tk.NW,pady=10,padx=(0,0))
                omnestedif5.config(height=0,bd=0,highlightthickness=0,width=7)

                lbl_elIf4.config(textvariable=elifmess4)
                lbl_elIf4.grid(row = 10 , sticky=tk.NW, column=0,pady = 10,padx=20)

                Entr_ValA5.config(justify= 'right',textvariable=v,width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValA5.grid(row =10, sticky=tk.NW,columnspan=2, column=1,pady = 10)


                    # app = OptionMenuDemonestedIf(canvasfunc,rowCount+2,2)
                #Entr_ValG = Entry(canvasfunc)
                Entr_ValG.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                Entr_ValG.grid(row =10, sticky=tk.NW, columnspan=2,column=5,pady = 10,padx=(5,0))


                nestPrintlbl6.config(textvariable=Printmess5)
                nestPrintlbl6.grid(row = 11 , sticky=tk.NW, columnspan=2,column=0,pady = 10,padx=20)

                resultelseif4.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelseif4.grid(row =11,  sticky=tk.NW,column=2,columnspan=5,pady = 10)

                  ####### else #######################################################
                elmess.set("Else")
                lbl_el4.config(textvariable=elmess)
                lbl_el4.grid(row = 12 , sticky=tk.NW, column=0,pady = 10,padx=20)
                #
                nestPrintlbldefault4.config(textvariable=Printmess5)
                nestPrintlbldefault4.grid(row = 13 , sticky=tk.NW,columnspan=2, column=0,pady = 10,padx=20)
                #
                resultelse4.config(justify= 'right',width=11,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                resultelse4.grid(row =13, sticky=tk.NW, columnspan=5,column=2,pady = 10)

                Executenested.config(text ="Proceed",command =lambda row=rowCount, column=7: exceutenestedifelse5(svnestif,svnestif1,svnestif2,svnestif3,svnestif4,svnestif5,row, column),fg = "white",bg = "#ab4345",width=7)
                Executenested.grid(row = 13, column=6, sticky =tk.NW)


       omnestedifcases = OptionMenu( aWindow, self.svcase, *sorted(Dic.keys()))
       case = CreateToolTip(omnestedifcases, "Select No.Of Loops")
       omnestedifcases.grid(row=0,column= 6, sticky =tk.NW,pady=10)
       omnestedifcases.config(height=0,bd=0,highlightthickness=0,width=4)
       self.svcase.trace("w", OPTIONSNestedCases)
       choices = [1,2,3,4,5]

       cancelnestedif.config(image = close,command =lambda row=rowCount, column=7: btncancelnestedif(omnestedif,omnestedif1,row, column) )
       cancelnestedif.grid(row = 0, column=7, sticky =tk.NW,pady=10)
       cancelnestedif.config(bd=0, highlightthickness=0,bg = "White")

       # Executenested.config(text ="Proceed",command =lambda row=rowCount, column=7: exceutenestedifelse(sv,sv1,sv2,sv3,sv4,sv5,row, column),fg = "white",bg = "#ab4345",width=7)
       # Executenested.grid(row = rowCount+2, column=7, sticky =tk.NW)
def nestedIfElse():
    global numlabel
    global numText
    global numText1
    global numText2
    global numText3
    global rowCount
    global cancelnestedif
    global varnestif
    global varnestelif
    global varnestelif
    global  drop_menunestedifelse
    global drop_menunestedifelse1
    global drop_menunestedifelse2
    global aText
    global bText
    global rowCount
    global cancelif
    global varif
    global Proceedif
    global drop_menuifcase1
    global lbl_ValA
    global lbl_ValB
    global lbl_ValC

    global Executenestif
    global construct
    global construct
    construct = 1
    clear_all()


    drop_menutexttype.grid_forget()
    Print1mess = tk.StringVar()
    Print2mess = tk.StringVar()
    Print1 = Label(canvasfunc,width = 20)
    Print2 = Label(canvasfunc,width = 20)

    nestedifmessage.set("If")
    nestedelsemessage.set("Elseif")
    elsemess.set("Else")
    valAmess.set("A")
    valBmess.set("B")
    valCmess.set("C")
    ifmess.set("If")
    elseifmess.set("Elseif")
    elsemess.set("Else")
    Printmess1.set("Print")
    Printmess2.set("Print")

    app = OptionMenuDemonestedIf(canvasfunc,rowCount,3)


    colconfig = (canvasfucnwidth-80)/8
    canvasfunc.columnconfigure(0, minsize = 8)
    canvasfunc.columnconfigure(1, minsize = colconfig-3)
    canvasfunc.columnconfigure(2, minsize = colconfig-3)
    canvasfunc.columnconfigure(3, minsize = colconfig-3)
    canvasfunc.columnconfigure(4, minsize = colconfig-3)
    canvasfunc.columnconfigure(5, minsize = colconfig-3)
    canvasfunc.columnconfigure(6, minsize = colconfig-3)
    canvasfunc.columnconfigure(7, minsize = colconfig-3)



    # rowCount = rowCount+1
def exceutenestedifelse1(nestifoptions,nestifoptn1,number,test):
    global lbl_If
    global drop_menuifcase1
    global drop_menuoptncase1
    global drop_menuoptncase2
    global rowCount
    global varnestif
    global varval
    global varvalnew
    global entervalue
    global entervalue2



    valA = Entr_ValA.get()
    valA1 = Entr_ValA.get()
    valB = Entr_ValB.get()
    valC = Entr_ValC.get()
    valD = Entr_ValD.get()
    valE = Entr_ValE.get()
    valF = Entr_ValF.get()
    valG = Entr_ValG.get()
    optn1 = nestifoptions.get()
    optn2 = nestifoptn1.get()
    ifresultval = resultif.get()
    elseifresultval = resultelseif.get()
    elseresultval = resultelse.get()
    elseifresultval1 =  resultelseif1.get()
    elseresultval1=   resultelse1.get()
    elseifresultval2=  resultelseif2.get()
    elseresultval2=   resultelse2.get()
    elseifresultval3 =      resultelseif3.get()
    elseresultval3 =   resultelse3.get()
    elseifresultval4 = resultelseif4.get()
    elseresultval4=    resultelse4.get()
    # if(optn1 == "Select option" and optn2 == "Select option"):
    #     shapesfeildsempty()

    if(not(valA.isdigit() and not(valB.isdigit() and not(valC.isdigit) and not(valA1.isdigit)))):
        ForInvalidInput()
    if((optn1 == "Operators" or valA) == ""  or (valA) == "Int A" or (valB) == ""  or (valB) == "Int B" or (valC) == ""  or (valC) == "Int C" or (valA1) == ""  or (valA1) == "Int A" ):
        shapesfeildsempty()
    if(len(valA) != 0 and len(valB) != 0 and len(valC)!= 0 and len(valA1) != 0):
        if(valA.isdigit() and valB.isdigit() and valC.isdigit() and valA.isdigit()):
            if(optn1 ==  "<"):

                if(int(valA) < int(valB)):

                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                else:
                    outputtext.insert(END, str(elseresultval)+ '\n')

            elif(optn1 ==  ">"):
                if(int(valA) > int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                #######################case 2 ###########################################


                else:

                    outputtext.insert(END, str(elseresultval)+ '\n')

            elif(optn1 ==  "=="):
                if(int(valA) == int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                else:
                    outputtext.insert(END, str(elseresultval)+ '\n')

            elif(optn1 ==  ">="):
                if(int(valA) >= int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                else:
                    outputtext.insert(END, str(elseresultval)+ '\n')

            elif(optn1 ==  "<="):
                if(int(valA) <= int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                else:
                    outputtext.insert(END, str(elseresultval)+ '\n')


    rowCount = rowCount+1
    def clearlog():
        outputtext.delete('1.0', END)
    Reset = Button(canvasleft,bg="#f2f2f2", text ="Clear Log",image = clearlogimage, compound= "left",command = clearlog,width=Buttonwidth,height=0,pady = -800)
    Reset.grid(row=4,column=5,pady=2)
def exceutenestedifelse2(nestifoptions,nestifoptn1,nestifoptn2,number,test):



    global lbl_If
    global drop_menuifcase1
    global drop_menuoptncase1
    global drop_menuoptncase2
    global rowCount
    global varnestif
    global varval
    global varvalnew
    global entervalue
    global entervalue2



    valA = Entr_ValA.get()
    valA1 = Entr_ValA.get()
    valB = Entr_ValB.get()
    valC = Entr_ValC.get()
    valD = Entr_ValD.get()
    valE = Entr_ValE.get()
    valF = Entr_ValF.get()
    valG = Entr_ValG.get()
    optn1 = nestifoptions.get()


    optn2 = nestifoptn1.get()

    optn3 = nestifoptn2.get()

    ifresultval = resultif.get()
    elseifresultval = resultelseif.get()
    elseresultval = resultelse.get()

    elseifresultval1 =  resultelseif1.get()
    elseresultval1=   resultelse1.get()

    elseifresultval2=  resultelseif2.get()
    elseresultval2=   resultelse2.get()

    elseifresultval3 =      resultelseif3.get()
    elseresultval3 =   resultelse3.get()

    elseifresultval4 = resultelseif4.get()
    elseresultval4=    resultelse4.get()
    # if(optn1 == "Select option" and optn2 == "Select option"):
    #     shapesfeildsempty()

    if(not(valA.isdigit() and not(valB.isdigit() and not(valC.isdigit) and not(valA1.isdigit)))):

        ForInvalidInput()
    if((optn1 == "Operators" or valA) == ""  or (valA) == "Int A" or (valB) == ""  or (valB) == "Int B" or (valC) == ""  or (valC) == "Int C" or (valA1) == ""  or (valA1) == "Int A" ):
        shapesfeildsempty()


    if(len(valA) != 0 and len(valB) != 0 and len(valC)!= 0 and len(valA1) != 0):
        if(valA.isdigit() and valB.isdigit() and valC.isdigit() and valA.isdigit()):
            if(optn1 ==  "<"):
                if(int(valA) < int(valB)):

                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')





                else:

                    outputtext.insert(END, str(elseresultval1)+ '\n')

            elif(optn1 ==  ">"):
                if(int(valA) > int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')


                else:


                    outputtext.insert(END, str(elseresultval1)+ '\n')

            elif(optn1 ==  "=="):
                if(int(valA) == int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')


                else:

                    outputtext.insert(END, str(elseresultval1)+ '\n')

            elif(optn1 ==  ">="):
                if(int(valA) >= int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                else:

                    outputtext.insert(END, str(elseresultval1)+ '\n')

            elif(optn1 ==  "<="):
                if(int(valA) <= int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                else:

                    outputtext.insert(END, str(elseresultval1)+ '\n')


    rowCount = rowCount+1
    def clearlog():
        outputtext.delete('1.0', END)
    Reset = Button(canvasleft,bg="#f2f2f2", text ="Clear Log",image = clearlogimage, compound= "left",command = clearlog,width=Buttonwidth,height=0,pady = -800)
    Reset.grid(row=4,column=5,pady=2)
def exceutenestedifelse3(nestifoptions,nestifoptn1,nestifoptn2,nestifoptn3,number,test):


    global lbl_If
    global drop_menuifcase1
    global drop_menuoptncase1
    global drop_menuoptncase2
    global rowCount
    global varnestif
    global varval
    global varvalnew
    global entervalue
    global entervalue2



    valA = Entr_ValA.get()
    valA1 = Entr_ValA.get()
    valB = Entr_ValB.get()
    valC = Entr_ValC.get()
    valD = Entr_ValD.get()
    valE = Entr_ValE.get()
    valF = Entr_ValF.get()
    valG = Entr_ValG.get()
    optn1 = nestifoptions.get()

    optn2 = nestifoptn1.get()

    optn3 = nestifoptn2.get()
    optn4 = nestifoptn3.get()

    ifresultval = resultif.get()
    elseifresultval = resultelseif.get()
    elseresultval = resultelse.get()

    elseifresultval1 =  resultelseif1.get()
    elseresultval1=   resultelse1.get()

    elseifresultval2=  resultelseif2.get()
    elseresultval2=   resultelse2.get()

    elseifresultval3 =      resultelseif3.get()
    elseresultval3 =   resultelse3.get()

    elseifresultval4 = resultelseif4.get()
    elseresultval4=    resultelse4.get()
    # if(optn1 == "Select option" and optn2 == "Select option"):
    #     shapesfeildsempty()

    if(not(valA.isdigit() and not(valB.isdigit() and not(valC.isdigit) and not(valA1.isdigit)))):

        ForInvalidInput()
    if((optn1 == "Operators" or valA) == ""  or (valA) == "Int A" or (valB) == ""  or (valB) == "Int B" or (valC) == ""  or (valC) == "Int C" or (valA1) == ""  or (valA1) == "Int A" ):
        shapesfeildsempty()


    if(len(valA) != 0 and len(valB) != 0 and len(valC)!= 0 and len(valA1) != 0):
        if(valA.isdigit() and valB.isdigit() and valC.isdigit() and valA.isdigit()):
            if(optn1 ==  "<"):
                if(int(valA) < int(valB)):

                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')




                else:

                    outputtext.insert(END, str(elseresultval2)+ '\n')

            elif(optn1 ==  ">"):
                if(int(valA) > int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')



                else:


                    outputtext.insert(END, str(elseresultval2)+ '\n')

            elif(optn1 ==  "=="):
                if(int(valA) == int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')

                else:

                    outputtext.insert(END, str(elseresultval2)+ '\n')

            elif(optn1 ==  ">="):
                if(int(valA) >= int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):
                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):
                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')

                else:

                    outputtext.insert(END, str(elseresultval2)+ '\n')

            elif(optn1 ==  "<="):
                if(int(valA) <= int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                else:

                    outputtext.insert(END, str(elseresultval2)+ '\n')


    rowCount = rowCount+1
    def clearlog():
        outputtext.delete('1.0', END)
    Reset = Button(canvasleft,bg="#f2f2f2", text ="Clear Log",image = clearlogimage, compound= "left",command = clearlog,width=Buttonwidth,height=0,pady = -800)
    Reset.grid(row=4,column=5,pady=2)
def exceutenestedifelse4(nestifoptions,nestifoptn1,nestifoptn2,nestifoptn3,nestifoptn4,number,test):


    global lbl_If
    global drop_menuifcase1
    global drop_menuoptncase1
    global drop_menuoptncase2
    global rowCount
    global varnestif
    global varval
    global varvalnew
    global entervalue
    global entervalue2



    valA = Entr_ValA.get()
    valA1 = Entr_ValA.get()
    valB = Entr_ValB.get()
    valC = Entr_ValC.get()
    valD = Entr_ValD.get()
    valE = Entr_ValE.get()
    valF = Entr_ValF.get()
    valG = Entr_ValG.get()
    optn1 = nestifoptions.get()


    optn2 = nestifoptn1.get()

    optn3 = nestifoptn2.get()
    optn4 = nestifoptn3.get()
    optn5 = nestifoptn4.get()

    ifresultval = resultif.get()
    elseifresultval = resultelseif.get()
    elseresultval = resultelse.get()

    elseifresultval1 =  resultelseif1.get()
    elseresultval1=   resultelse1.get()

    elseifresultval2=  resultelseif2.get()
    elseresultval2=   resultelse2.get()

    elseifresultval3 =      resultelseif3.get()
    elseresultval3 =   resultelse3.get()

    elseifresultval4 = resultelseif4.get()
    elseresultval4=    resultelse4.get()
    # if(optn1 == "Select option" and optn2 == "Select option"):
    #     shapesfeildsempty()

    if(not(valA.isdigit() and not(valB.isdigit() and not(valC.isdigit) and not(valA1.isdigit)))):

        ForInvalidInput()
    if((optn1 == "Operators" or valA) == ""  or (valA) == "Int A" or (valB) == ""  or (valB) == "Int B" or (valC) == ""  or (valC) == "Int C" or (valA1) == ""  or (valA1) == "Int A" ):
        shapesfeildsempty()


    if(len(valA) != 0 and len(valB) != 0 and len(valC)!= 0 and len(valA1) != 0):
        if(valA.isdigit() and valB.isdigit() and valC.isdigit() and valA.isdigit()):
            if(optn1 ==  "<"):
                if(int(valA) < int(valB)):

                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):

                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
               ############################## CASE 4 ############################################

                elif(optn5 ==  "<" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')



                else:

                    outputtext.insert(END, str(elseresultval3)+ '\n')

            elif(optn1 ==  ">"):
                if(int(valA) > int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')

                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
               ############################## CASE 4 ############################################

                elif(optn5 ==  "<" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')

                else:


                    outputtext.insert(END, str(elseresultval3)+ '\n')

            elif(optn1 ==  "=="):
                if(int(valA) == int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')

                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
               ############################## CASE 4 ############################################

                elif(optn5 ==  "<" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                else:

                    outputtext.insert(END, str(elseresultval3)+ '\n')

            elif(optn1 ==  ">="):
                if(int(valA) >= int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')

                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
               ############################## CASE 4 ############################################

                elif(optn5 ==  "<" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')

                else:

                    outputtext.insert(END, str(elseresultval3)+ '\n')

            elif(optn1 ==  "<="):
                if(int(valA) <= int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')

                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
               ############################## CASE 4 ############################################

                elif(optn5 ==  "<" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                else:

                    outputtext.insert(END, str(elseresultval3)+ '\n')


    rowCount = rowCount+1
    def clearlog():
        outputtext.delete('1.0', END)
    Reset = Button(canvasleft,bg="#f2f2f2", text ="Clear Log",image = clearlogimage, compound= "left",command = clearlog,width=Buttonwidth,height=0,pady = -800)
    Reset.grid(row=4,column=5,pady=2)
def exceutenestedifelse5(nestifoptions,nestifoptn1,nestifoptn2,nestifoptn3,nestifoptn4,nestifoptn5,number,test):



    global lbl_If

    global drop_menuifcase1
    global drop_menuoptncase1
    global drop_menuoptncase2
    global rowCount
    global varnestif
    global varval
    global varvalnew
    global entervalue
    global entervalue2



    valA = Entr_ValA.get()
    valA1 = Entr_ValA.get()
    valB = Entr_ValB.get()
    valC = Entr_ValC.get()
    valD = Entr_ValD.get()
    valE = Entr_ValE.get()
    valF = Entr_ValF.get()
    valG = Entr_ValG.get()
    optn1 = nestifoptions.get()


    optn2 = nestifoptn1.get()

    optn3 = nestifoptn2.get()
    optn4 = nestifoptn3.get()
    optn5 = nestifoptn4.get()
    optn6 = nestifoptn5.get()
    ifresultval = resultif.get()
    elseifresultval = resultelseif.get()
    elseresultval = resultelse.get()

    elseifresultval1 =  resultelseif1.get()
    elseresultval1=   resultelse1.get()

    elseifresultval2=  resultelseif2.get()
    elseresultval2=   resultelse2.get()

    elseifresultval3 =      resultelseif3.get()
    elseresultval3 =   resultelse3.get()

    elseifresultval4 = resultelseif4.get()
    elseresultval4=    resultelse4.get()
    # if(optn1 == "Select option" and optn2 == "Select option"):
    #     shapesfeildsempty()

    if(not(valA.isdigit() and not(valB.isdigit() and not(valC.isdigit) and not(valA1.isdigit)))):

        ForInvalidInput()
    if((optn1 == "Operators" or valA) == ""  or (valA) == "Int A" or (valB) == ""  or (valB) == "Int B" or (valC) == ""  or (valC) == "Int C" or (valA1) == ""  or (valA1) == "Int A" ):
        shapesfeildsempty()


    if(len(valA) != 0 and len(valB) != 0 and len(valC)!= 0 and len(valA1) != 0):
        if(valA.isdigit() and valB.isdigit() and valC.isdigit() and valA.isdigit()):
            if(optn1 ==  "<"):
                if(int(valA) < int(valB)):

                    outputtext.insert(END, str(ifresultval)+ '\n')

                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
               ############################## CASE 4 ############################################

                elif(optn5 ==  "<" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                ########################## CASE 5 #######################################

                elif(optn6 ==  "<" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')

                else:

                    outputtext.insert(END, str(elseresultval4)+ '\n')
            elif(optn1 ==  ">"):
                if(int(valA) > int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
               ############################## CASE 4 ############################################

                elif(optn5 ==  "<" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                ########################## CASE 5 #######################################

                elif(optn6 ==  "<" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')


                else:


                    outputtext.insert(END, str(elseresultval4)+ '\n')
            elif(optn1 ==  "=="):
                if(int(valA) == int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
               ############################## CASE 4 ############################################

                elif(optn5 ==  "<" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                ########################## CASE 5 #######################################

                elif(optn6 ==  "<" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                else:

                    outputtext.insert(END, str(elseresultval4)+ '\n')
            elif(optn1 ==  ">="):
                if(int(valA) >= int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
               ############################## CASE 4 ############################################

                elif(optn5 ==  "<" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                ########################## CASE 5 #######################################

                elif(optn6 ==  "<" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                else:

                    outputtext.insert(END, str(elseresultval4)+ '\n')
            elif(optn1 ==  "<="):
                if(int(valA) <= int(valB)):
                    outputtext.insert(END, str(ifresultval)+ '\n')
                elif(optn2 ==  "<" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "==" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  "<=" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) > int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) < int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) == int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) >= int(valC)):

                    outputtext.insert(END, str(elseifresultval)+ '\n')
                elif(optn2 ==  ">" and int(valA1) <= int(valC)):

                    outputtext.insert(END, str(elseresultval)+ '\n')

                ##################################### ELSE CASE 2 #############################################
                elif(optn3 ==  "<" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "==" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  "<=" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) > int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) < int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) == int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) >= int(valD)):
                    outputtext.insert(END, str(elseifresultval1)+ '\n')
                elif(optn3 ==  ">" and int(valA1) <= int(valD)):
                    outputtext.insert(END, str(elseresultval1)+ '\n')



                 ###################### ELSE CASE 3 ##############################################
                elif(optn4 ==  "<" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "==" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  "<=" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) > int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) < int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) == int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) >= int(valE)):
                    outputtext.insert(END, str(elseifresultval2)+ '\n')
                elif(optn4 ==  ">" and int(valA1) <= int(valE)):
                    outputtext.insert(END, str(elseresultval2)+ '\n')
               ############################## CASE 4 ############################################

                elif(optn5 ==  "<" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "==" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  "<=" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) > int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) < int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) == int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) >= int(valF)):
                    outputtext.insert(END, str(elseifresultval3)+ '\n')
                elif(optn5 ==  ">" and int(valA1) <= int(valF)):
                    outputtext.insert(END, str(elseresultval3)+ '\n')
                ########################## CASE 5 #######################################

                elif(optn6 ==  "<" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "==" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">=" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  "<=" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) > int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) < int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) == int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) >= int(valG)):
                    outputtext.insert(END, str(elseifresultval4)+ '\n')
                elif(optn6 ==  ">" and int(valA1) <= int(valG)):
                    outputtext.insert(END, str(elseresultval4)+ '\n')
                else:

                    outputtext.insert(END, str(elseresultval4)+ '\n')

    rowCount = rowCount+1
    def clearlog():
        outputtext.delete('1.0', END)
    Reset = Button(canvasleft,bg="#f2f2f2", text ="Clear Log",image = clearlogimage, compound= "left",command = clearlog,width=Buttonwidth,height=0,pady = -800)
    Reset.grid(row=4,column=5,pady=2)
def btncancelnestedif(om,om1,number,test):

    global lbl_If
    global nestediflblprint1
    global drop_menuifcase1
    global drop_menuoptncase1
    global drop_menuoptncase2
    global lbl_elIf
    global Proceedexe
    global nestediflblprint1
    global nestediflbl1
    global Proceedex2
    global PrintText1
    global construct
    if(construct ==1 ):
        clear_all()
    construct = 0

    omnestedif2.grid_remove()
    omnestedif3.grid_remove()
    omnestedif4.grid_remove()
    omnestedif5.grid_remove()
    omnestedif1.grid_remove()
    Executenested.grid_remove()


    lbl_elIf1.grid_forget()
    Entr_ValA2.grid_forget()
    Entr_ValD.grid_forget()
    nestPrintlbl3.grid_forget()
    resultelseif1.grid_forget()
    omnestedif3.grid_forget()
    lbl_elIf2.grid_forget()
    Entr_ValA3.grid_forget()
    Entr_ValE.grid_forget()
    nestPrintlbl4.grid_forget()
    resultelseif2.grid_forget()
    lbl_el2.grid_forget()
    nestPrintlbldefault2.grid_forget()
    resultelse2.grid_forget()

    omnestedif4.grid_forget()
    lbl_elIf3.grid_forget()
    Entr_ValA4.grid_forget()
    Entr_ValF.grid_forget()
    nestPrintlbl5.grid_forget()
    resultelseif3.grid_forget()
    lbl_el3.grid_forget()
    nestPrintlbldefault3.grid_forget()
    resultelse3.grid_forget()

    omnestedif5.grid_forget()
    lbl_elIf4.grid_forget()
    Entr_ValA5.grid_forget()
    Entr_ValG.grid_forget()
    nestPrintlbl6.grid_forget()
    resultelseif4.grid_forget()
    lbl_el4.grid_forget()
    nestPrintlbldefault4.grid_forget()
    resultelse4.grid_forget()

    Entr_ValD.grid_forget()

    Entr_ValA.grid_forget()
    Entr_ValB.grid_forget()
    nestPrintlbl1.grid_forget()
    resultif.grid_forget()
    lbl_elIf.grid_forget()
    Entr_ValA1.grid_forget()
    Entr_ValC.grid_forget()
    nestPrintlbl2.grid_forget()
    resultelseif.grid_forget()
    lbl_el.grid_forget()
    nestPrintlbldefault.grid_forget()
    resultelse.grid_forget()



    lbl_el1.grid_forget()
    nestPrintlbldefault1.grid_forget()
    resultelse1.grid_forget()



    for item in canvasfunc.grid_slaves():
        if int(item.grid_info()["row"]) == number:
            item.grid_forget()



############################################## SWITCH CASE ###################################################

add_placeholder_to(case1text, 'case 1')
add_placeholder_to(case3text, 'case 2')
add_placeholder_to(case5text, 'case 3')
add_placeholder_to(case6text, 'case 4')
add_placeholder_to(case7text, 'case 5')
add_placeholder_to(case8text, 'case 6')
add_placeholder_to(case9text, 'case 7')
add_placeholder_to(case10text, 'case 8')
add_placeholder_to(case11text, 'case 9')
add_placeholder_to(case12text, 'case 10')

add_placeholder_to(defaulttext5,'case default')
add_placeholder_to(defaulttext7,'case default')
add_placeholder_to(defaulttext8,'case default')
add_placeholder_to(defaulttext9,'case default')
add_placeholder_to(defaulttext10,'case default')
add_placeholder_to(defaulttext11,'case default')
add_placeholder_to(defaulttext6,'case default')
add_placeholder_to(defaulttext4,'case default')
add_placeholder_to(defaulttext3,'case default')
add_placeholder_to(defaulttext2,'case default')
add_placeholder_to(defaulttext1,'case default')

def caseonewidgets():
	defaultlabel2.grid_forget()
	#defaultlabel.grid_forget()
	defaultlabel1.grid_forget()
	defaultlabel3.grid_forget()
	defaultlabel4.grid_forget()
	defaultlabel5.grid_forget()
	defaultlabel6.grid_forget()
	defaultlabel7.grid_forget()
	defaultlabel8.grid_forget()
	defaultlabel9.grid_forget()
	defaultlabel10.grid_forget()
	#defaulttext1.grid_forget()
	defaulttext2.grid_forget()
	defaulttext3.grid_forget()
	defaulttext4.grid_forget()
	defaulttext5.grid_forget()
	defaulttext6.grid_forget()
	defaulttext7.grid_forget()
	defaulttext8.grid_forget()
	defaulttext9.grid_forget()
	defaulttext10.grid_forget()
	#dfeaultprintlabel1.grid_forget()
	dfeaultprintlabel2.grid_forget()
	dfeaultprintlabel3.grid_forget()
	dfeaultprintlabel4.grid_forget()
	dfeaultprintlabel5.grid_forget()
	dfeaultprintlabel6.grid_forget()
	dfeaultprintlabel7.grid_forget()
	dfeaultprintlabel8.grid_forget()
	dfeaultprintlabel9.grid_forget()
	dfeaultprintlabel10.grid_forget()

	defaulttext2.grid_forget()
	dfeaultprintlabel2.grid_forget()
	defaultlabel2.grid_forget()
	printlabel2.grid_forget()
	case3text.grid_forget()
	breaklabel.grid_forget()
	breaklabel2.grid_forget()
	caselabel2.grid_forget()
	printlabel3.grid_forget()
	case5text.grid_forget()
	breaklabel3.grid_forget()
	caselabel3.grid_forget()
	printlabel4.grid_forget()
	case6text.grid_forget()
	breaklabel4.grid_forget()
	caselabel4.grid_forget()
	printlabel5.grid_forget()
	case7text.grid_forget()
	breaklabel5.grid_forget()
	caselabel5.grid_forget()
	printlabel6.grid_forget()
	case8text.grid_forget()
	breaklabel6.grid_forget()
	caselabel6.grid_forget()
	printlabel7.grid_forget()
	case9text.grid_forget()
	breaklabel7.grid_forget()
	caselabel7.grid_forget()
	printlabel8.grid_forget()
	case10text.grid_forget()
	breaklabel8.grid_forget()
	caselabel8.grid_forget()
	printlabel9.grid_forget()
	case11text.grid_forget()
	breaklabel9.grid_forget()
	caselabel9.grid_forget()
	printlabel10.grid_forget()
	case12text.grid_forget()
	breaklabel10.grid_forget()
	defaultlabel11.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext11.grid_forget()
def casetwowidgets():
	#caselabel1.grid_forget()
    #printlabel2.grid_forget()
	#defaultlabel2.grid_forget()
	defaultlabel.grid_forget()
	defaultlabel1.grid_forget()
	defaultlabel3.grid_forget()
	defaultlabel4.grid_forget()
	defaultlabel5.grid_forget()
	defaultlabel6.grid_forget()
	defaultlabel7.grid_forget()
	defaultlabel8.grid_forget()
	defaultlabel9.grid_forget()
	defaultlabel10.grid_forget()
	defaulttext1.grid_forget()
	#defaulttext2.grid_forget()
	defaulttext3.grid_forget()
	defaulttext4.grid_forget()
	defaulttext5.grid_forget()
	defaulttext6.grid_forget()
	defaulttext7.grid_forget()
	defaulttext8.grid_forget()
	defaulttext9.grid_forget()
	defaulttext10.grid_forget()
	dfeaultprintlabel1.grid_forget()
	#dfeaultprintlabel2.grid_forget()
	dfeaultprintlabel3.grid_forget()
	dfeaultprintlabel4.grid_forget()
	dfeaultprintlabel5.grid_forget()
	dfeaultprintlabel6.grid_forget()
	dfeaultprintlabel7.grid_forget()
	dfeaultprintlabel8.grid_forget()
	dfeaultprintlabel9.grid_forget()
	dfeaultprintlabel10.grid_forget()

	#case3text.grid_forget()
	#breaklabel2.grid_forget()
	caselabel2.grid_forget()
	printlabel3.grid_forget()
	case5text.grid_forget()
	breaklabel3.grid_forget()
	caselabel3.grid_forget()
	printlabel4.grid_forget()
	case6text.grid_forget()
	breaklabel4.grid_forget()
	caselabel4.grid_forget()
	printlabel5.grid_forget()
	case7text.grid_forget()
	breaklabel5.grid_forget()
	caselabel5.grid_forget()
	printlabel6.grid_forget()
	case8text.grid_forget()
	breaklabel6.grid_forget()
	caselabel6.grid_forget()
	printlabel7.grid_forget()
	case9text.grid_forget()
	breaklabel7.grid_forget()
	caselabel7.grid_forget()
	printlabel8.grid_forget()
	case10text.grid_forget()
	breaklabel8.grid_forget()
	caselabel8.grid_forget()
	printlabel9.grid_forget()
	case11text.grid_forget()
	breaklabel9.grid_forget()
	caselabel9.grid_forget()
	printlabel10.grid_forget()
	case12text.grid_forget()
	breaklabel10.grid_forget()
	defaultlabel11.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext11.grid_forget()
def casethreewidgets():
	#caselabel1.grid_forget()
	#printlabel.grid_forget()
    #printlabel2.grid_forget()
	defaultlabel2.grid_forget()
	defaultlabel.grid_forget()
	defaultlabel1.grid_forget()
	#defaultlabel3.grid_forget()
	defaultlabel4.grid_forget()
	defaultlabel5.grid_forget()
	defaultlabel6.grid_forget()
	defaultlabel7.grid_forget()
	defaultlabel8.grid_forget()
	defaultlabel9.grid_forget()
	defaultlabel10.grid_forget()
	defaulttext1.grid_forget()
	defaulttext2.grid_forget()
	#defaulttext3.grid_forget()
	defaulttext4.grid_forget()
	defaulttext5.grid_forget()
	defaulttext6.grid_forget()
	defaulttext7.grid_forget()
	defaulttext8.grid_forget()
	defaulttext9.grid_forget()
	defaulttext10.grid_forget()
	dfeaultprintlabel1.grid_forget()
	dfeaultprintlabel2.grid_forget()
	#dfeaultprintlabel3.grid_forget()
	dfeaultprintlabel4.grid_forget()
	dfeaultprintlabel5.grid_forget()
	dfeaultprintlabel6.grid_forget()
	dfeaultprintlabel7.grid_forget()
	dfeaultprintlabel8.grid_forget()
	dfeaultprintlabel9.grid_forget()
	dfeaultprintlabel10.grid_forget()
	#case3text.grid_forget()
	#breaklabel2.grid_forget()
	#caselabel2.grid_forget()
	#printlabel3.grid_forget()
	#case5text.grid_forget()
	breaklabel3.grid_forget()
	caselabel3.grid_forget()
	printlabel4.grid_forget()
	case6text.grid_forget()
	breaklabel4.grid_forget()
	caselabel4.grid_forget()
	printlabel5.grid_forget()
	case7text.grid_forget()
	breaklabel5.grid_forget()
	caselabel5.grid_forget()
	printlabel6.grid_forget()
	case8text.grid_forget()
	breaklabel6.grid_forget()
	caselabel6.grid_forget()
	printlabel7.grid_forget()
	case9text.grid_forget()
	breaklabel7.grid_forget()
	caselabel7.grid_forget()
	printlabel8.grid_forget()
	case10text.grid_forget()
	breaklabel8.grid_forget()
	caselabel8.grid_forget()
	printlabel9.grid_forget()
	case11text.grid_forget()
	breaklabel9.grid_forget()
	caselabel9.grid_forget()
	printlabel10.grid_forget()
	case12text.grid_forget()
	breaklabel10.grid_forget()
	defaultlabel11.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext11.grid_forget()
def casefourwidgets():
	#caselabel1.grid_forget()
   # printlabel2.grid_forget()
	defaultlabel2.grid_forget()
	defaultlabel3.grid_forget()
	#defaultlabel4.grid_forget()
	defaultlabel5.grid_forget()
	defaultlabel6.grid_forget()
	defaultlabel7.grid_forget()
	defaultlabel8.grid_forget()
	defaultlabel9.grid_forget()
	defaultlabel10.grid_forget()
	dfeaultprintlabel1.grid_forget()
	dfeaultprintlabel2.grid_forget()
	dfeaultprintlabel3.grid_forget()
	#dfeaultprintlabel4.grid_forget()
	dfeaultprintlabel5.grid_forget()
	dfeaultprintlabel6.grid_forget()
	dfeaultprintlabel7.grid_forget()
	dfeaultprintlabel8.grid_forget()
	dfeaultprintlabel9.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext1.grid_forget()
	defaulttext2.grid_forget()
	defaulttext3.grid_forget()
	#defaulttext4.grid_forget()
	defaulttext5.grid_forget()
	defaulttext6.grid_forget()
	defaulttext7.grid_forget()
	defaulttext8.grid_forget()
	defaulttext9.grid_forget()
	defaulttext10.grid_forget()
	#case3text.grid_forget()
	#breaklabel2.grid_forget()
	#caselabel2.grid_forget()
	#printlabel3.grid_forget()
	#case5text.grid_forget()
	#breaklabel3.grid_forget()
	#caselabel3.grid_forget()
	#printlabel4.grid_forget()
	#case6text.grid_forget()
	#breaklabel4.grid_forget()
	caselabel4.grid_forget()
	printlabel5.grid_forget()
	case7text.grid_forget()
	breaklabel5.grid_forget()
	caselabel5.grid_forget()
	printlabel6.grid_forget()
	case8text.grid_forget()
	breaklabel6.grid_forget()
	caselabel6.grid_forget()
	printlabel7.grid_forget()
	case9text.grid_forget()
	breaklabel7.grid_forget()
	caselabel7.grid_forget()
	printlabel8.grid_forget()
	case10text.grid_forget()
	breaklabel8.grid_forget()
	caselabel8.grid_forget()
	printlabel9.grid_forget()
	case11text.grid_forget()
	breaklabel9.grid_forget()
	caselabel9.grid_forget()
	printlabel10.grid_forget()
	case12text.grid_forget()
	breaklabel10.grid_forget()
	defaultlabel11.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext11.grid_forget()
def casefivewidgets():

	defaultlabel2.grid_forget()
	defaultlabel3.grid_forget()
	defaultlabel4.grid_forget()
	#defaultlabel5.grid_forget()
	defaultlabel6.grid_forget()
	defaultlabel7.grid_forget()
	defaultlabel8.grid_forget()
	defaultlabel9.grid_forget()
	defaultlabel10.grid_forget()
	dfeaultprintlabel1.grid_forget()
	dfeaultprintlabel2.grid_forget()
	dfeaultprintlabel3.grid_forget()
	dfeaultprintlabel4.grid_forget()
	#dfeaultprintlabel5.grid_forget()
	dfeaultprintlabel6.grid_forget()
	dfeaultprintlabel7.grid_forget()
	dfeaultprintlabel8.grid_forget()
	dfeaultprintlabel9.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext1.grid_forget()
	defaulttext2.grid_forget()
	defaulttext3.grid_forget()
	defaulttext4.grid_forget()
	#defaulttext5.grid_forget()
	defaulttext6.grid_forget()
	defaulttext7.grid_forget()
	defaulttext8.grid_forget()
	defaulttext9.grid_forget()
	defaulttext10.grid_forget()
	#case3text.grid_forget()
	#breaklabel2.grid_forget()
	#caselabel2.grid_forget()
	#printlabel3.grid_forget()
	#case5text.grid_forget()
	#breaklabel3.grid_forget()
	#caselabel3.grid_forget()
	#printlabel4.grid_forget()
	#case6text.grid_forget()
	#breaklabel4.grid_forget()
	#caselabel4.grid_forget()
	#printlabel5.grid_forget()
	#case7text.grid_forget()
	#breaklabel5.grid_forget()
	caselabel5.grid_forget()
	printlabel6.grid_forget()
	case8text.grid_forget()
	breaklabel6.grid_forget()
	caselabel6.grid_forget()
	printlabel7.grid_forget()
	case9text.grid_forget()
	breaklabel7.grid_forget()
	caselabel7.grid_forget()
	printlabel8.grid_forget()
	case10text.grid_forget()
	breaklabel8.grid_forget()
	caselabel8.grid_forget()
	printlabel9.grid_forget()
	case11text.grid_forget()
	breaklabel9.grid_forget()
	caselabel9.grid_forget()
	printlabel10.grid_forget()
	case12text.grid_forget()
	breaklabel10.grid_forget()
	defaultlabel11.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext11.grid_forget()
def casesixwidgets():
	#caselabel1.grid_forget()
    #printlabel2.grid_forget()
	defaultlabel2.grid_forget()
	defaultlabel3.grid_forget()
	defaultlabel4.grid_forget()
	defaultlabel5.grid_forget()
	#defaultlabel6.grid_forget()
	defaultlabel7.grid_forget()
	defaultlabel8.grid_forget()
	defaultlabel9.grid_forget()
	defaultlabel10.grid_forget()
	dfeaultprintlabel1.grid_forget()
	dfeaultprintlabel2.grid_forget()
	dfeaultprintlabel3.grid_forget()
	dfeaultprintlabel4.grid_forget()
	dfeaultprintlabel5.grid_forget()
	#dfeaultprintlabel6.grid_forget()
	dfeaultprintlabel7.grid_forget()
	dfeaultprintlabel8.grid_forget()
	dfeaultprintlabel9.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext1.grid_forget()
	defaulttext2.grid_forget()
	defaulttext3.grid_forget()
	defaulttext4.grid_forget()
	defaulttext5.grid_forget()
	#defaulttext6.grid_forget()
	defaulttext7.grid_forget()
	defaulttext8.grid_forget()
	defaulttext9.grid_forget()
	defaulttext10.grid_forget()
	#case3text.grid_forget()
	#breaklabel2.grid_forget()
	#caselabel2.grid_forget()
	#printlabel3.grid_forget()
	#case5text.grid_forget()
	#breaklabel3.grid_forget()
	#caselabel3.grid_forget()
	#printlabel4.grid_forget()
	#case6text.grid_forget()
	#breaklabel4.grid_forget()
	#caselabel4.grid_forget()
	#printlabel5.grid_forget()
	#case7text.grid_forget()
	#breaklabel5.grid_forget()
	#caselabel5.grid_forget()
	#printlabel6.grid_forget()
	#case8text.grid_forget()
	#breaklabel6.grid_forget()
	caselabel6.grid_forget()
	printlabel7.grid_forget()
	case9text.grid_forget()
	breaklabel7.grid_forget()
	caselabel7.grid_forget()
	printlabel8.grid_forget()
	case10text.grid_forget()
	breaklabel8.grid_forget()
	caselabel8.grid_forget()
	printlabel9.grid_forget()
	case11text.grid_forget()
	breaklabel9.grid_forget()
	caselabel9.grid_forget()
	printlabel10.grid_forget()
	case12text.grid_forget()
	breaklabel10.grid_forget()
	defaultlabel11.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext11.grid_forget()
def casesevenwidgets():
	#caselabel1.grid_forget()
    #printlabel2.grid_forget()
	#printlabel2.grid_forget()
	defaultlabel2.grid_forget()
	defaultlabel3.grid_forget()
	defaultlabel4.grid_forget()
	defaultlabel5.grid_forget()
	defaultlabel6.grid_forget()
	#defaultlabel7.grid_forget()
	defaultlabel8.grid_forget()
	defaultlabel9.grid_forget()
	defaultlabel10.grid_forget()
	dfeaultprintlabel1.grid_forget()
	dfeaultprintlabel2.grid_forget()
	dfeaultprintlabel3.grid_forget()
	dfeaultprintlabel4.grid_forget()
	dfeaultprintlabel5.grid_forget()
	dfeaultprintlabel6.grid_forget()
	#dfeaultprintlabel7.grid_forget()
	dfeaultprintlabel8.grid_forget()
	dfeaultprintlabel9.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext1.grid_forget()
	defaulttext2.grid_forget()
	defaulttext3.grid_forget()
	defaulttext4.grid_forget()
	defaulttext5.grid_forget()
	defaulttext6.grid_forget()
	#defaulttext7.grid_forget()
	defaulttext8.grid_forget()
	defaulttext9.grid_forget()
	defaulttext10.grid_forget()
	#case3text.grid_forget()
	#breaklabel2.grid_forget()
	#caselabel2.grid_forget()
	#printlabel3.grid_forget()
	#case5text.grid_forget()
	#breaklabel3.grid_forget()
	#caselabel3.grid_forget()
	#printlabel4.grid_forget()
	#case6text.grid_forget()
	#breaklabel4.grid_forget()
	#caselabel4.grid_forget()
	#printlabel5.grid_forget()
	#case7text.grid_forget()
	#breaklabel5.grid_forget()
	#caselabel5.grid_forget()
	#printlabel6.grid_forget()
	#case8text.grid_forget()
	#breaklabel6.grid_forget()
	#caselabel6.grid_forget()
	#printlabel7.grid_forget()
	#case9text.grid_forget()
	#breaklabel7.grid_forget()
	caselabel7.grid_forget()
	printlabel8.grid_forget()
	case10text.grid_forget()
	breaklabel8.grid_forget()
	caselabel8.grid_forget()
	printlabel9.grid_forget()
	case11text.grid_forget()
	breaklabel9.grid_forget()
	caselabel9.grid_forget()
	printlabel10.grid_forget()
	case12text.grid_forget()
	breaklabel10.grid_forget()
	defaultlabel11.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext11.grid_forget()
def caseeightwidgets():
	#caselabel1.grid_forget()
    #printlabel2.grid_forget()
	#printlabel2.grid_forget()
	defaultlabel2.grid_forget()
	defaultlabel3.grid_forget()
	defaultlabel4.grid_forget()
	defaultlabel5.grid_forget()
	defaultlabel6.grid_forget()
	defaultlabel7.grid_forget()
	#defaultlabel8.grid_forget()
	defaultlabel9.grid_forget()
	defaultlabel10.grid_forget()
	dfeaultprintlabel1.grid_forget()
	dfeaultprintlabel2.grid_forget()
	dfeaultprintlabel3.grid_forget()
	dfeaultprintlabel4.grid_forget()
	dfeaultprintlabel5.grid_forget()
	dfeaultprintlabel6.grid_forget()
	dfeaultprintlabel7.grid_forget()
	#dfeaultprintlabel8.grid_forget()
	dfeaultprintlabel9.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext1.grid_forget()
	defaulttext2.grid_forget()
	defaulttext3.grid_forget()
	defaulttext4.grid_forget()
	defaulttext5.grid_forget()
	defaulttext6.grid_forget()
	defaulttext7.grid_forget()
	#defaulttext8.grid_forget()
	defaulttext9.grid_forget()
	defaulttext10.grid_forget()
	#case3text.grid_forget()
	#breaklabel2.grid_forget()
	#caselabel2.grid_forget()
	#printlabel3.grid_forget()
	#case5text.grid_forget()
	#breaklabel3.grid_forget()
	#caselabel3.grid_forget()
	#printlabel4.grid_forget()
	#case6text.grid_forget()
	#breaklabel4.grid_forget()
	#caselabel4.grid_forget()
	#printlabel5.grid_forget()
	#case7text.grid_forget()
	#breaklabel5.grid_forget()
	#caselabel5.grid_forget()
	#printlabel6.grid_forget()
	#case8text.grid_forget()
	#breaklabel6.grid_forget()
	#caselabel6.grid_forget()
	#printlabel7.grid_forget()
	#case9text.grid_forget()
	#breaklabel7.grid_forget()
	#caselabel7.grid_forget()
	#printlabel8.grid_forget()
	#case10text.grid_forget()
	#breaklabel8.grid_forget()
	caselabel8.grid_forget()
	printlabel9.grid_forget()
	case11text.grid_forget()
	breaklabel9.grid_forget()
	caselabel9.grid_forget()
	printlabel10.grid_forget()
	case12text.grid_forget()
	breaklabel10.grid_forget()
	defaultlabel11.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext11.grid_forget()
def caseninewidgets():
	#caselabel1.grid_forget()
    #printlabel2.grid_forget()
	#printlabel2.grid_forget()
	defaultlabel2.grid_forget()
	defaultlabel3.grid_forget()
	defaultlabel4.grid_forget()
	defaultlabel5.grid_forget()
	defaultlabel6.grid_forget()
	defaultlabel7.grid_forget()
	defaultlabel8.grid_forget()
	#defaultlabel9.grid_forget()
	defaultlabel10.grid_forget()
	dfeaultprintlabel1.grid_forget()
	dfeaultprintlabel2.grid_forget()
	dfeaultprintlabel3.grid_forget()
	dfeaultprintlabel4.grid_forget()
	dfeaultprintlabel5.grid_forget()
	dfeaultprintlabel6.grid_forget()
	dfeaultprintlabel7.grid_forget()
	dfeaultprintlabel8.grid_forget()
	#dfeaultprintlabel9.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext1.grid_forget()
	defaulttext2.grid_forget()
	defaulttext3.grid_forget()
	defaulttext4.grid_forget()
	defaulttext5.grid_forget()
	defaulttext6.grid_forget()
	defaulttext7.grid_forget()
	defaulttext8.grid_forget()
	#defaulttext9.grid_forget()
	defaulttext10.grid_forget()
	#case3text.grid_forget()
	#breaklabel2.grid_forget()
	#caselabel2.grid_forget()
	#printlabel3.grid_forget()
	#case5text.grid_forget()
	#breaklabel3.grid_forget()
	#caselabel3.grid_forget()
	#printlabel4.grid_forget()
	#case6text.grid_forget()
	#breaklabel4.grid_forget()
	#caselabel4.grid_forget()
	#printlabel5.grid_forget()
	#case7text.grid_forget()
	#breaklabel5.grid_forget()
	#caselabel5.grid_forget()
	#printlabel6.grid_forget()
	#case8text.grid_forget()
	#breaklabel6.grid_forget()
	#caselabel6.grid_forget()
	#printlabel7.grid_forget()
	#case9text.grid_forget()
	#breaklabel7.grid_forget()
	#caselabel7.grid_forget()
	#printlabel8.grid_forget()
	#case10text.grid_forget()
	#breaklabel8.grid_forget()
	#breaklabel9.grid_forget()
	#caselabel8.grid_forget()
	#printlabel9.grid_forget()
	#case11text.grid_forget()
	#breaklabel10.grid_forget()
	caselabel9.grid_forget()
	printlabel10.grid_forget()
	case12text.grid_forget()
	breaklabel10.grid_forget()
	defaultlabel11.grid_forget()
	dfeaultprintlabel10.grid_forget()
	defaulttext11.grid_forget()
def casetenwidgets():
	#caselabel1.grid_forget()
    #printlabel2.grid_forget()
	#printlabel2.grid_forget()
	defaultlabel2.grid_forget()
	defaultlabel3.grid_forget()
	defaultlabel4.grid_forget()
	defaultlabel5.grid_forget()
	defaultlabel6.grid_forget()
	defaultlabel7.grid_forget()
	defaultlabel8.grid_forget()
	defaultlabel9.grid_forget()
	#defaultlabel10.grid_forget()
	dfeaultprintlabel1.grid_forget()
	dfeaultprintlabel2.grid_forget()
	dfeaultprintlabel3.grid_forget()
	dfeaultprintlabel4.grid_forget()
	dfeaultprintlabel5.grid_forget()
	dfeaultprintlabel6.grid_forget()
	dfeaultprintlabel7.grid_forget()
	dfeaultprintlabel8.grid_forget()
	dfeaultprintlabel9.grid_forget()
	#dfeaultprintlabel10.grid_forget()
	defaulttext1.grid_forget()
	defaulttext2.grid_forget()
	defaulttext3.grid_forget()
	defaulttext4.grid_forget()
	defaulttext5.grid_forget()
	defaulttext6.grid_forget()
	defaulttext7.grid_forget()
	defaulttext8.grid_forget()
	defaulttext9.grid_forget()


class OptionMenuDemoswitch:

    def __init__(self, aWindow,row,col):
       global rowCount

       #A list of string options for the optionMenu
      # OPTIONS = ["Select option","1","1 TO 2","1 TO 3","1 TO 4","1 TO 5"]
       Dic={'1':1,'1 to 2':2,'1 to 3':3,'1 to 4':4,'1 to 5':5,'1 to 6':6,'1 to 7':7,'1 to 8':8,'1 to 9':9,'1 to 10':10}
       self.sv = StringVar()
       self.sv.set("Cases")

       casemess1.set("Case 1")
       casemess2.set("Case 2")
       casemess3.set("Case 3")
       casemess4.set("Case 4")
       casemess5.set("Case 5")
       casemess6.set("Case 6")
       casemess7.set("Case 7")
       casemess8.set("Case 8")
       casemess9.set("Case 9")
       casemess10.set("Case 10")
       printmess.set("Print")
       brkmess.set("break")
       defaultmess.set("default")


       def option_changedswitch(*args):
           global entervalue
           entervalue = self.sv.get()
           if(entervalue == "1"):

               caseonewidgets()

               caselabel1.grid_forget()
               printlabel2.grid_forget()
               case3text.grid_forget()
               breaklabel2.grid_forget()

               caselabel2.grid_forget()
               printlabel3.grid_forget()
               case5text.grid_forget()
               breaklabel3.grid_forget()
               defaultlabel3.grid_forget()


               printlabel4.grid_forget()
               case6text.grid_forget()
               breaklabel4.grid_forget()
               defaultlabel2.grid_forget()
               defaultlabel3.grid_forget()
               defaultlabel4.grid_forget()

               caselabel4.grid_forget()
               printlabel5.grid_forget()
               case7text.grid_forget()
               breaklabel5.grid_forget()
               defaultlabel5.grid_forget()

               printlabel6.grid_forget()
               case8text.grid_forget()
               breaklabel6.grid_forget()
               defaultlabel6.grid_forget()

               dfeaultprintlabel5.grid_forget()
               dfeaultprintlabel6.grid_forget()
               dfeaultprintlabel4.grid_forget()
               dfeaultprintlabel3.grid_forget()
               dfeaultprintlabel2.grid_forget()

               defaulttext5.grid_forget()
               defaulttext6.grid_forget()
               defaulttext4.grid_forget()
               defaulttext3.grid_forget()
               defaulttext2.grid_forget()


               ##################### case 1 ##########################################
               caselabel.config(textvariable=casemess1)
               caselabel.grid(row = rowCount+1 , column=0,pady = 2,sticky=tk.NW)
               printlabel.config(textvariable=printmess)
               printlabel.grid(row = rowCount+2 , column=0,pady = 5,sticky=tk.NW)
               case1text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               case1text.grid(row =rowCount+2, column=1,pady = 5)

               ###################### Default case ######################################
               breaklabel.config(textvariable=brkmess)
               breaklabel.grid(row = rowCount+3 , column=0,pady = 5,sticky=tk.NW)
               defaultlabel.config(textvariable=defaultmess)
               defaultlabel.grid(row = rowCount+4 , column=0,pady = 5,sticky=tk.NW)
               dfeaultprintlabel1.config(textvariable=printmess)
               dfeaultprintlabel1.grid(row = rowCount+5 , column=0,pady = 5,sticky=tk.NW)
               defaulttext1.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               defaulttext1.grid(row =rowCount+5, column=1,pady = 5)
           elif(entervalue == "1 to 2"):

               casetwowidgets()

               caselabel2.grid_forget()
               printlabel3.grid_forget()
               case5text.grid_forget()
               breaklabel3.grid_forget()
               defaultlabel3.grid_forget()
               printlabel4.grid_forget()
               case6text.grid_forget()
               breaklabel4.grid_forget()
               defaultlabel2.grid_forget()
               defaultlabel3.grid_forget()
               defaultlabel4.grid_forget()
               caselabel4.grid_forget()
               printlabel5.grid_forget()
               case7text.grid_forget()
               breaklabel5.grid_forget()
               defaultlabel5.grid_forget()
               dfeaultprintlabel5.grid_forget()
               dfeaultprintlabel4.grid_forget()
               dfeaultprintlabel3.grid_forget()
               defaulttext5.grid_forget()
               defaulttext4.grid_forget()
               defaulttext3.grid_forget()
               defaulttext1.grid_forget()
               printlabel6.grid_forget()
               case8text.grid_forget()
               breaklabel6.grid_forget()
               defaultlabel6.grid_forget()
               dfeaultprintlabel5.grid_forget()
               dfeaultprintlabel6.grid_forget()
               dfeaultprintlabel4.grid_forget()
               dfeaultprintlabel3.grid_forget()
               dfeaultprintlabel2.grid_forget()

               ##################### case 1 ##################################################
               caselabel.config(textvariable=casemess1)
               caselabel.grid(row = rowCount+1 , column=0,pady = 5,sticky=tk.NW)
               printlabel.config(textvariable=printmess)
               printlabel.grid(row = rowCount+2 , column=0,pady = 5,sticky=tk.NW)
               case1text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               case1text.grid(row =rowCount+2, column=1,pady = 5)
               #add_placeholder_to(case2text, 'case 1')

                #################### case 2#######################################
               breaklabel.config(textvariable=brkmess)
               breaklabel.grid(row = rowCount+3 , column=0,pady = 5,sticky=tk.NW)
               caselabel1.config(textvariable=casemess2)
               caselabel1.grid(row = rowCount+4 , column=0,pady = 5,sticky=tk.NW)
               printlabel2.config(textvariable=printmess)
               printlabel2.grid(row = rowCount+5 , column=0,pady = 5,sticky=tk.NW)
               case3text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               case3text.grid(row =rowCount+5, column=1,pady = 5)


               ####################### default case  ###################################
               breaklabel2.config(textvariable=brkmess)
               breaklabel2.grid(row = rowCount+6 , column=0,pady = 5,sticky=tk.NW)
               defaultlabel2.config(textvariable=defaultmess)
               defaultlabel2.grid(row = rowCount+7 , column=0,pady = 5,sticky=tk.NW)
               dfeaultprintlabel2.config(textvariable=printmess)
               dfeaultprintlabel2.grid(row = rowCount+8 , column=0,pady = 5,sticky=tk.NW)
               defaulttext2.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               defaulttext2.grid(row =rowCount+8, column=1,pady = 5)
           elif(entervalue == "1 to 3"):

               casethreewidgets()


               printlabel4.grid_forget()
               case6text.grid_forget()
               breaklabel4.grid_forget()
               defaultlabel2.grid_forget()
               caselabel3.grid_forget()
               defaultlabel4.grid_forget()
               caselabel4.grid_forget()
               printlabel5.grid_forget()
               case7text.grid_forget()
               breaklabel5.grid_forget()
               defaultlabel5.grid_forget()
               dfeaultprintlabel5.grid_forget()
               dfeaultprintlabel4.grid_forget()
               defaulttext5.grid_forget()
               defaulttext4.grid_forget()
               defaulttext1.grid_forget()
               defaulttext2.grid_forget()
               printlabel6.grid_forget()
               case8text.grid_forget()
               breaklabel6.grid_forget()
               defaultlabel6.grid_forget()

               dfeaultprintlabel5.grid_forget()
               dfeaultprintlabel6.grid_forget()
               dfeaultprintlabel4.grid_forget()
               dfeaultprintlabel3.grid_forget()
               dfeaultprintlabel2.grid_forget()


               ########################### case 1 #####################################
               caselabel.config(textvariable=casemess1)
               caselabel.grid(row = rowCount+1 , column=0,pady = 5,sticky=tk.NW)
               printlabel.config(textvariable=printmess)
               printlabel.grid(row = rowCount+2 , column=0,pady = 5,sticky=tk.NW)
               case1text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               case1text.grid(row =rowCount+2, column=1,pady = 5)
                # add_placeholder_to(case2text, 'case 1')

                # breaklabel1.config(textvariable=brkmess)
                # breaklabel1.grid(row = rowCount+3 , column=0,pady = 5,padx=2,sticky=W)

                ####################### case 2 ############################################
               breaklabel.config(textvariable=brkmess)
               breaklabel.grid(row = rowCount+3 , column=0,pady = 5,sticky=tk.NW)
               caselabel1.config(textvariable=casemess2)
               caselabel1.grid(row = rowCount+4 , column=0,pady = 5,sticky=tk.NW)
               printlabel2.config(textvariable=printmess)
               printlabel2.grid(row = rowCount+5 , column=0,pady = 5,sticky=tk.NW)
                # case4text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                # case4text.grid(row =rowCount+5, column=1,pady = 5,padx=2,sticky=W)
                # add_placeholder_to(case4text, 'case 2')
               case3text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               case3text.grid(row =rowCount+5, column=1,pady = 5)
                #add_placeholder_to(case3text, 'case 2')

                ############################### case 3 #################################
               breaklabel2.config(textvariable=brkmess)
               breaklabel2.grid(row = rowCount+6 , column=0,pady = 5,sticky=tk.NW)
               caselabel2.config(textvariable=casemess3)
               caselabel2.grid(row = rowCount+7 , column=0,pady = 5,sticky=tk.NW)
               printlabel3.config(textvariable=printmess)
               printlabel3.grid(row = rowCount+8 , column=0,pady = 5,sticky=tk.NW)
               case5text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               case5text.grid(row =rowCount+8, column=1,pady = 5)
               # add_placeholder_to(case5text, 'case 3')
                # printlabel4.config(textvariable=printmess)
                # printlabel4.grid(row = rowCount+8 , column=0,pady = 5,padx=2,sticky=W)

                #################################### case default ##################################
               breaklabel3.config(textvariable=brkmess)
               breaklabel3.grid(row = rowCount+9 , column=0,pady = 5,sticky=tk.NW)
               defaultlabel3.config(textvariable=defaultmess)
               defaultlabel3.grid(row = rowCount+10 , column=0,pady = 5,sticky=tk.NW)
               dfeaultprintlabel3.config(textvariable=printmess)
               dfeaultprintlabel3.grid(row = rowCount+11 , column=0,pady = 5,sticky=tk.NW)
               defaulttext3.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               defaulttext3.grid(row =rowCount+11, column=1,pady = 5)
           elif(entervalue == "1 to 4"):

               casefourwidgets()


               caselabel4.grid_forget()
               printlabel5.grid_forget()
               case7text.grid_forget()
               breaklabel5.grid_forget()
               defaultlabel5.grid_forget()
               dfeaultprintlabel5.grid_forget()
               defaulttext5.grid_forget()
               defaulttext1.grid_forget()
               defaulttext3.grid_forget()
               defaulttext2.grid_forget()
               printlabel6.grid_forget()
               case8text.grid_forget()
               breaklabel6.grid_forget()
               defaultlabel6.grid_forget()

               dfeaultprintlabel5.grid_forget()
               dfeaultprintlabel6.grid_forget()
               dfeaultprintlabel4.grid_forget()
               dfeaultprintlabel3.grid_forget()
               dfeaultprintlabel2.grid_forget()
               ######################## case 1 ##########################################
               caselabel.config(textvariable=casemess1)
               caselabel.grid(row = rowCount+1 , column=0,pady = 5,sticky=tk.NW)
               printlabel.config(textvariable=printmess)
               printlabel.grid(row = rowCount+2 , column=0,pady = 5,sticky=tk.NW)
               case1text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               case1text.grid(row =rowCount+2, column=1,pady = 5)

               ########################### case 2 #########################################
               breaklabel1.config(textvariable=brkmess)
               breaklabel1.grid(row = rowCount+3 , column=0,pady = 5,sticky=tk.NW)
               caselabel1.config(textvariable=casemess2)
               caselabel1.grid(row = rowCount+4 , column=0,pady = 5,sticky=tk.NW)
               printlabel2.config(textvariable=printmess)
               printlabel2.grid(row = rowCount+5 , column=0,pady = 5)

                # case4text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                # case4text.grid(row =rowCount+5, column=1,pady = 5,padx=2,sticky=W)
                # add_placeholder_to(case4text, 'case 2')
               case3text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               case3text.grid(row =rowCount+5, column=1,pady = 5,sticky=tk.NW)

               ####################### case 3 ################################################
               breaklabel2.config(textvariable=brkmess)
               breaklabel2.grid(row = rowCount+6 , column=0,pady = 5,sticky=tk.NW)
               caselabel2.config(textvariable=casemess3)
               caselabel2.grid(row = rowCount+7 , column=0,pady = 5,sticky=tk.NW)
               printlabel3.config(textvariable=printmess)
               printlabel3.grid(row = rowCount+8 , column=0,pady = 5,sticky=tk.NW)
               case5text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               case5text.grid(row =rowCount+8, column=1,pady = 5)
                # add_placeholder_to(case5text, 'case 3')

                ############################### case 4 #######################################
               breaklabel3.config(textvariable=brkmess)
               breaklabel3.grid(row = rowCount+9 , column=0,pady = 5,sticky=tk.NW)
               caselabel3.config(textvariable=casemess4)
               caselabel3.grid(row = rowCount+10 , column=0,pady = 5,sticky=tk.NW)
               printlabel4.config(textvariable=printmess)
               printlabel4.grid(row = rowCount+11 , column=0,pady = 5,sticky=tk.NW)
               case6text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               case6text.grid(row =rowCount+11, column=1,pady = 5)

               ############################## case 5 ###########################################
               breaklabel4.config(textvariable=brkmess)
               breaklabel4.grid(row = rowCount+12 , column=0,pady = 5,sticky=tk.NW)
               defaultlabel4.config(textvariable=defaultmess)
               defaultlabel4.grid(row = rowCount+13 , column=0,pady = 5,sticky=tk.NW)
               dfeaultprintlabel4.config(textvariable=printmess)
               dfeaultprintlabel4.grid(row = rowCount+14 , column=0,pady = 5,sticky=tk.NW)
               defaulttext4.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
               defaulttext4.grid(row =rowCount+14, column=1,pady = 5)
           elif(entervalue == "1 to 5"):


                defaulttext1.grid_forget()
                defaulttext4.grid_forget()
                defaulttext3.grid_forget()
                defaulttext2.grid_forget()
                printlabel6.grid_forget()
                case8text.grid_forget()
                breaklabel6.grid_forget()
                defaultlabel6.grid_forget()

                casefivewidgets()

                dfeaultprintlabel5.grid_forget()
                dfeaultprintlabel6.grid_forget()
                dfeaultprintlabel4.grid_forget()
                dfeaultprintlabel3.grid_forget()
                dfeaultprintlabel2.grid_forget()

               ######################### case 1######################################
                caselabel.config(textvariable=casemess1)
                caselabel.grid(row = rowCount+1 , column=0,pady = 5,sticky=tk.NW)
                printlabel.config(textvariable=printmess)
                printlabel.grid(row = rowCount+2 , column=0,pady = 5,sticky=tk.NW)

                case1text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case1text.grid(row =rowCount+2, column=1,pady = 5)

                ################# case 2 ###########################################
                breaklabel1.config(textvariable=brkmess)
                breaklabel1.grid(row = rowCount+3 , column=0,pady = 5,sticky=tk.NW)
                caselabel1.config(textvariable=casemess2)
                caselabel1.grid(row = rowCount+4 , column=0,pady = 5,sticky=tk.NW)
                printlabel2.config(textvariable=printmess)
                printlabel2.grid(row = rowCount+5 , column=0,pady = 5,sticky=tk.NW)

                 # case4text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                 # case4text.grid(row =rowCount+5, column=1,pady = 5,padx=2,sticky=W)
                 # add_placeholder_to(case4text, 'case 2')
                case3text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case3text.grid(row =rowCount+5, column=1,pady = 5)

                ######################## case 3 #####################################################
                breaklabel2.config(textvariable=brkmess)
                breaklabel2.grid(row = rowCount+6 , column=0,pady = 5,sticky=tk.NW)
                caselabel2.config(textvariable=casemess3)
                caselabel2.grid(row = rowCount+7 , column=0,pady = 5,sticky=tk.NW)
                printlabel3.config(textvariable=printmess)
                printlabel3.grid(row = rowCount+8 , column=0,pady = 5,sticky=tk.NW)
                case5text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case5text.grid(row =rowCount+8, column=1,pady = 5)
                 # add_placeholder_to(case5text, 'case 3')

                 #############################case 4 ###############################################

                breaklabel3.config(textvariable=brkmess)
                breaklabel3.grid(row = rowCount+9 , column=0,pady = 5,sticky=tk.NW)
                caselabel3.config(textvariable=casemess4)
                caselabel3.grid(row = rowCount+10 , column=0,pady = 5,sticky=tk.NW)
                printlabel4.config(textvariable=printmess)
                printlabel4.grid(row = rowCount+11 , column=0,pady = 5,sticky=tk.NW)
                case6text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case6text.grid(row =rowCount+11, column=1,pady = 5)

                ###############################case 5 #############################################

                breaklabel4.config(textvariable=brkmess)
                breaklabel4.grid(row = rowCount+12 , column=0,pady = 5,sticky=tk.NW)

                caselabel4.config(textvariable=casemess5)
                caselabel4.grid(row = rowCount+13 , column=0,pady = 5,sticky=tk.NW)
                printlabel5.config(textvariable=printmess)
                printlabel5.grid(row = rowCount+14 , column=0,pady = 5,sticky=tk.NW)
                case7text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case7text.grid(row =rowCount+14, column=1,pady = 5)

                ####################################case default #######################################
                breaklabel5.config(textvariable=brkmess)
                breaklabel5.grid(row = rowCount+15 , column=0,pady = 5,sticky=tk.NW)

                defaultlabel5.config(textvariable=defaultmess)
                defaultlabel5.grid(row = rowCount+16 , column=0,pady = 5,sticky=tk.NW)
                dfeaultprintlabel5.config(textvariable=printmess)
                dfeaultprintlabel5.grid(row = rowCount+17 , column=0,pady = 5,sticky=tk.NW)
                defaulttext5.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                defaulttext5.grid(row =rowCount+17, column=1,pady = 5)
           elif(entervalue == "1 to 6"):

                defaulttext1.grid_forget()
                defaulttext4.grid_forget()
                defaulttext3.grid_forget()
                defaulttext2.grid_forget()

                casesixwidgets()

               ######################### case 1######################################
                caselabel.config(textvariable=casemess1)
                caselabel.grid(row = rowCount+1 , column=0,pady = 5,sticky=tk.NW)
                printlabel.config(textvariable=printmess)
                printlabel.grid(row = rowCount+2 , column=0,pady = 5,sticky=tk.NW)

                case1text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case1text.grid(row =rowCount+2, column=1,pady = 5)

                ################# case 2 ###########################################
                breaklabel1.config(textvariable=brkmess)
                breaklabel1.grid(row = rowCount+3 , column=0,pady = 5,sticky=tk.NW)
                caselabel1.config(textvariable=casemess2)
                caselabel1.grid(row = rowCount+4 , column=0,pady = 5,sticky=tk.NW)
                printlabel2.config(textvariable=printmess)
                printlabel2.grid(row = rowCount+5 , column=0,pady = 5,sticky=tk.NW)

                 # case4text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                 # case4text.grid(row =rowCount+5, column=1,pady = 5,padx=2,sticky=W)
                 # add_placeholder_to(case4text, 'case 2')
                case3text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case3text.grid(row =rowCount+5, column=1,pady = 5)

                ######################## case 3 #####################################################
                breaklabel2.config(textvariable=brkmess)
                breaklabel2.grid(row = rowCount+6 , column=0,pady = 5,sticky=tk.NW)
                caselabel2.config(textvariable=casemess3)
                caselabel2.grid(row = rowCount+7 , column=0,pady = 5,sticky=tk.NW)
                printlabel3.config(textvariable=printmess)
                printlabel3.grid(row = rowCount+8 , column=0,pady = 5,sticky=tk.NW)
                case5text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case5text.grid(row =rowCount+8, column=1,pady = 5)
                 # add_placeholder_to(case5text, 'case 3')

                 #############################case 4 ###############################################

                breaklabel3.config(textvariable=brkmess)
                breaklabel3.grid(row = rowCount+9 , column=0,pady = 5,sticky=tk.NW)
                caselabel3.config(textvariable=casemess4)
                caselabel3.grid(row = rowCount+10 , column=0,pady = 5,sticky=tk.NW)
                printlabel4.config(textvariable=printmess)
                printlabel4.grid(row = rowCount+11 , column=0,pady = 5,sticky=tk.NW)
                case6text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case6text.grid(row =rowCount+11, column=1,pady = 5)

                ###############################case 5 #############################################

                breaklabel4.config(textvariable=brkmess)
                breaklabel4.grid(row = rowCount+12 , column=0,pady = 5,sticky=tk.NW)

                caselabel4.config(textvariable=casemess5)
                caselabel4.grid(row = rowCount+13 , column=0,pady = 5,sticky=tk.NW)
                printlabel5.config(textvariable=printmess)
                printlabel5.grid(row = rowCount+14 , column=0,pady = 5,sticky=tk.NW)
                case7text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case7text.grid(row =rowCount+14, column=1,pady = 5)

                ################ case 6 #########################################################

                breaklabel5.config(textvariable=brkmess)
                breaklabel5.grid(row = rowCount+18 , column=0,pady = 5,sticky=tk.NW)

                caselabel5.config(textvariable=casemess6)
                caselabel5.grid(row = rowCount+19 , column=0,pady = 5,sticky=tk.NW)
                printlabel6.config(textvariable=printmess)
                printlabel6.grid(row = rowCount+20 , column=0,pady = 5,sticky=tk.NW)
                case8text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case8text.grid(row =rowCount+20, column=1,pady = 5)


                ####################################case default #######################################
                breaklabel6.config(textvariable=brkmess)
                breaklabel6.grid(row = rowCount+21 , column=0,pady = 5,sticky=tk.NW)

                defaultlabel6.config(textvariable=defaultmess)
                defaultlabel6.grid(row = rowCount+22 , column=0,pady = 5,sticky=tk.NW)
                dfeaultprintlabel6.config(textvariable=printmess)
                dfeaultprintlabel6.grid(row = rowCount+23 , column=0,pady = 5,sticky=tk.NW)
                defaulttext6.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                defaulttext6.grid(row =rowCount+23, column=1,pady = 5)
           elif(entervalue == "1 to 7"):
                defaulttext1.grid_forget()
                defaulttext4.grid_forget()
                defaulttext3.grid_forget()
                defaulttext2.grid_forget()

                casesevenwidgets()

               ######################### case 1######################################
                caselabel.config(textvariable=casemess1)
                caselabel.grid(row = rowCount+1 , column=0,pady = 5,sticky=tk.NW)
                printlabel.config(textvariable=printmess)
                printlabel.grid(row = rowCount+2 , column=0,pady = 5,sticky=tk.NW)

                case1text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case1text.grid(row =rowCount+2, column=1,pady = 5)

                ################# case 2 ###########################################
                breaklabel1.config(textvariable=brkmess)
                breaklabel1.grid(row = rowCount+3 , column=0,pady = 5,sticky=tk.NW)
                caselabel1.config(textvariable=casemess2)
                caselabel1.grid(row = rowCount+4 , column=0,pady = 5,sticky=tk.NW)
                printlabel2.config(textvariable=printmess)
                printlabel2.grid(row = rowCount+5 , column=0,pady = 5,sticky=tk.NW)

                 # case4text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                 # case4text.grid(row =rowCount+5, column=1,pady = 5,padx=2,sticky=W)
                 # add_placeholder_to(case4text, 'case 2')
                case3text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case3text.grid(row =rowCount+5, column=1,pady = 5)

                ######################## case 3 #####################################################
                breaklabel2.config(textvariable=brkmess)
                breaklabel2.grid(row = rowCount+6 , column=0,pady = 5,sticky=tk.NW)
                caselabel2.config(textvariable=casemess3)
                caselabel2.grid(row = rowCount+7 , column=0,pady = 5,sticky=tk.NW)
                printlabel3.config(textvariable=printmess)
                printlabel3.grid(row = rowCount+8 , column=0,pady = 5,sticky=tk.NW)
                case5text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case5text.grid(row =rowCount+8, column=1,pady = 5)
                 # add_placeholder_to(case5text, 'case 3')

                 #############################case 4 ###############################################

                breaklabel3.config(textvariable=brkmess)
                breaklabel3.grid(row = rowCount+9 , column=0,pady = 5,sticky=tk.NW)
                caselabel3.config(textvariable=casemess4)
                caselabel3.grid(row = rowCount+10 , column=0,pady = 5,sticky=tk.NW)
                printlabel4.config(textvariable=printmess)
                printlabel4.grid(row = rowCount+11 , column=0,pady = 5,sticky=tk.NW)
                case6text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case6text.grid(row =rowCount+11, column=1,pady = 5)

                ###############################case 5 #############################################

                breaklabel4.config(textvariable=brkmess)
                breaklabel4.grid(row = rowCount+12 , column=0,pady = 5,sticky=tk.NW)

                caselabel4.config(textvariable=casemess5)
                caselabel4.grid(row = rowCount+13 , column=0,pady = 5,sticky=tk.NW)
                printlabel5.config(textvariable=printmess)
                printlabel5.grid(row = rowCount+14 , column=0,pady = 5,sticky=tk.NW)
                case7text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case7text.grid(row =rowCount+14, column=1,pady = 5)

                ################ case 6 #########################################################

                breaklabel5.config(textvariable=brkmess)
                breaklabel5.grid(row = rowCount+18 , column=0,pady = 5,sticky=tk.NW)

                caselabel5.config(textvariable=casemess6)
                caselabel5.grid(row = rowCount+19 , column=0,pady = 5,sticky=tk.NW)
                printlabel6.config(textvariable=printmess)
                printlabel6.grid(row = rowCount+20 , column=0,pady = 5,sticky=tk.NW)
                case8text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case8text.grid(row =rowCount+20, column=1,pady = 5)

                ################ case 7 #########################################################

                breaklabel6.config(textvariable=brkmess)
                breaklabel6.grid(row = rowCount+21 , column=0,pady = 5,sticky=tk.NW)

                caselabel6.config(textvariable=casemess7)
                caselabel6.grid(row = rowCount+22 , column=0,pady = 5,sticky=tk.NW)
                printlabel7.config(textvariable=printmess)
                printlabel7.grid(row = rowCount+23 , column=0,pady = 5,sticky=tk.NW)
                case9text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case9text.grid(row =rowCount+23, column=1,pady = 5)

                ####################################case default #######################################
                breaklabel7.config(textvariable=brkmess)
                breaklabel7.grid(row = rowCount+24 , column=0,pady = 5,sticky=tk.NW)

                defaultlabel7.config(textvariable=defaultmess)
                defaultlabel7.grid(row = rowCount+25 , column=0,pady = 5,sticky=tk.NW)
                dfeaultprintlabel7.config(textvariable=printmess)
                dfeaultprintlabel7.grid(row = rowCount+26 , column=0,pady = 5,sticky=tk.NW)
                defaulttext7.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                defaulttext7.grid(row =rowCount+26, column=1,pady = 5)
           elif(entervalue == "1 to 8"):
                defaulttext1.grid_forget()
                defaulttext4.grid_forget()
                defaulttext3.grid_forget()
                defaulttext2.grid_forget()

                caseeightwidgets()

               ######################### case 1######################################
                caselabel.config(textvariable=casemess1)
                caselabel.grid(row = rowCount+1 , column=0,pady = 5,sticky=tk.NW)
                printlabel.config(textvariable=printmess)
                printlabel.grid(row = rowCount+2 , column=0,pady = 5,sticky=tk.NW)

                case1text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case1text.grid(row =rowCount+2, column=1,pady = 5)

                ################# case 2 ###########################################
                breaklabel1.config(textvariable=brkmess)
                breaklabel1.grid(row = rowCount+3 , column=0,pady = 5,sticky=tk.NW)
                caselabel1.config(textvariable=casemess2)
                caselabel1.grid(row = rowCount+4 , column=0,pady = 5,sticky=tk.NW)
                printlabel2.config(textvariable=printmess)
                printlabel2.grid(row = rowCount+5 , column=0,pady = 5,sticky=tk.NW)

                 # case4text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                 # case4text.grid(row =rowCount+5, column=1,pady = 5,padx=2,sticky=W)
                 # add_placeholder_to(case4text, 'case 2')
                case3text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case3text.grid(row =rowCount+5, column=1,pady = 5)

                ######################## case 3 #####################################################
                breaklabel2.config(textvariable=brkmess)
                breaklabel2.grid(row = rowCount+6 , column=0,pady = 5,sticky=tk.NW)
                caselabel2.config(textvariable=casemess3)
                caselabel2.grid(row = rowCount+7 , column=0,pady = 5,sticky=tk.NW)
                printlabel3.config(textvariable=printmess)
                printlabel3.grid(row = rowCount+8 , column=0,pady = 5,sticky=tk.NW)
                case5text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case5text.grid(row =rowCount+8, column=1,pady = 5)
                 # add_placeholder_to(case5text, 'case 3')

                 #############################case 4 ###############################################

                breaklabel3.config(textvariable=brkmess)
                breaklabel3.grid(row = rowCount+9 , column=0,pady = 5,sticky=tk.NW)
                caselabel3.config(textvariable=casemess4)
                caselabel3.grid(row = rowCount+10 , column=0,pady = 5,sticky=tk.NW)
                printlabel4.config(textvariable=printmess)
                printlabel4.grid(row = rowCount+11 , column=0,pady = 5,sticky=tk.NW)
                case6text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case6text.grid(row =rowCount+11, column=1,pady = 5)

                ###############################case 5 #############################################

                breaklabel4.config(textvariable=brkmess)
                breaklabel4.grid(row = rowCount+12 , column=0,pady = 5,sticky=tk.NW)

                caselabel4.config(textvariable=casemess5)
                caselabel4.grid(row = rowCount+13 , column=0,pady = 5,sticky=tk.NW)
                printlabel5.config(textvariable=printmess)
                printlabel5.grid(row = rowCount+14 , column=0,pady = 5,sticky=tk.NW)
                case7text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case7text.grid(row =rowCount+14, column=1,pady = 5)

                ################ case 6 #########################################################

                breaklabel5.config(textvariable=brkmess)
                breaklabel5.grid(row = rowCount+18 , column=0,pady = 5,sticky=tk.NW)

                caselabel5.config(textvariable=casemess6)
                caselabel5.grid(row = rowCount+19 , column=0,pady = 5,sticky=tk.NW)
                printlabel6.config(textvariable=printmess)
                printlabel6.grid(row = rowCount+20 , column=0,pady = 5,sticky=tk.NW)
                case8text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case8text.grid(row =rowCount+20, column=1,pady = 5)

                ################ case 7 #########################################################

                breaklabel6.config(textvariable=brkmess)
                breaklabel6.grid(row = rowCount+21 , column=0,pady = 5,sticky=tk.NW)

                caselabel6.config(textvariable=casemess7)
                caselabel6.grid(row = rowCount+22 , column=0,pady = 5,sticky=tk.NW)
                printlabel7.config(textvariable=printmess)
                printlabel7.grid(row = rowCount+23 , column=0,pady = 5,sticky=tk.NW)
                case9text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case9text.grid(row =rowCount+23, column=1,pady = 5)

                ################ case 7 #########################################################

                breaklabel7.config(textvariable=brkmess)
                breaklabel7.grid(row = rowCount+24 , column=0,pady = 5,sticky=tk.NW)

                caselabel7.config(textvariable=casemess8)
                caselabel7.grid(row = rowCount+25 , column=0,pady = 5,sticky=tk.NW)
                printlabel8.config(textvariable=printmess)
                printlabel8.grid(row = rowCount+26 , column=0,pady = 5,sticky=tk.NW)
                case10text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case10text.grid(row =rowCount+26, column=1,pady = 5)
                ####################################case default #######################################
                breaklabel8.config(textvariable=brkmess)
                breaklabel8.grid(row = rowCount+27 , column=0,pady = 5,sticky=tk.NW)

                defaultlabel8.config(textvariable=defaultmess)
                defaultlabel8.grid(row = rowCount+28 , column=0,pady = 5,sticky=tk.NW)
                dfeaultprintlabel8.config(textvariable=printmess)
                dfeaultprintlabel8.grid(row = rowCount+29 , column=0,pady = 5,sticky=tk.NW)
                defaulttext9.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                defaulttext9.grid(row =rowCount+29, column=1,pady = 5)
           elif(entervalue == "1 to 9"):
                defaulttext1.grid_forget()
                defaulttext4.grid_forget()
                defaulttext3.grid_forget()
                defaulttext2.grid_forget()

                caseninewidgets()

               ######################### case 1######################################
                caselabel.config(textvariable=casemess1)
                caselabel.grid(row = rowCount+1 , column=0,pady = 5,sticky=tk.NW)
                printlabel.config(textvariable=printmess)
                printlabel.grid(row = rowCount+2 , column=0,pady = 5,sticky=tk.NW)

                case1text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case1text.grid(row =rowCount+2, column=1,pady = 5)

                ################# case 2 ###########################################
                breaklabel1.config(textvariable=brkmess)
                breaklabel1.grid(row = rowCount+3 , column=0,pady = 5,sticky=tk.NW)
                caselabel1.config(textvariable=casemess2)
                caselabel1.grid(row = rowCount+4 , column=0,pady = 5,sticky=tk.NW)
                printlabel2.config(textvariable=printmess)
                printlabel2.grid(row = rowCount+5 , column=0,pady = 5,sticky=tk.NW)

                 # case4text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                 # case4text.grid(row =rowCount+5, column=1,pady = 5,padx=2,sticky=W)
                 # add_placeholder_to(case4text, 'case 2')
                case3text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case3text.grid(row =rowCount+5, column=1,pady = 5)

                ######################## case 3 #####################################################
                breaklabel2.config(textvariable=brkmess)
                breaklabel2.grid(row = rowCount+6 , column=0,pady = 5,sticky=tk.NW)
                caselabel2.config(textvariable=casemess3)
                caselabel2.grid(row = rowCount+7 , column=0,pady = 5,sticky=tk.NW)
                printlabel3.config(textvariable=printmess)
                printlabel3.grid(row = rowCount+8 , column=0,pady = 5,sticky=tk.NW)
                case5text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case5text.grid(row =rowCount+8, column=1,pady = 5)
                 # add_placeholder_to(case5text, 'case 3')

                 #############################case 4 ###############################################

                breaklabel3.config(textvariable=brkmess)
                breaklabel3.grid(row = rowCount+9 , column=0,pady = 5,sticky=tk.NW)
                caselabel3.config(textvariable=casemess4)
                caselabel3.grid(row = rowCount+10 , column=0,pady = 5,sticky=tk.NW)
                printlabel4.config(textvariable=printmess)
                printlabel4.grid(row = rowCount+11 , column=0,pady = 5,sticky=tk.NW)
                case6text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case6text.grid(row =rowCount+11, column=1,pady = 5)

                ###############################case 5 #############################################

                breaklabel4.config(textvariable=brkmess)
                breaklabel4.grid(row = rowCount+12 , column=0,pady = 5,sticky=tk.NW)

                caselabel4.config(textvariable=casemess5)
                caselabel4.grid(row = rowCount+13 , column=0,pady = 5,sticky=tk.NW)
                printlabel5.config(textvariable=printmess)
                printlabel5.grid(row = rowCount+14 , column=0,pady = 5,sticky=tk.NW)
                case7text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case7text.grid(row =rowCount+14, column=1,pady = 5)

                ################ case 6 #########################################################

                breaklabel5.config(textvariable=brkmess)
                breaklabel5.grid(row = rowCount+18 , column=0,pady = 5,sticky=tk.NW)

                caselabel5.config(textvariable=casemess6)
                caselabel5.grid(row = rowCount+19 , column=0,pady = 5,sticky=tk.NW)
                printlabel6.config(textvariable=printmess)
                printlabel6.grid(row = rowCount+20 , column=0,pady = 5,sticky=tk.NW)
                case8text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case8text.grid(row =rowCount+20, column=1,pady = 5)

                ################ case 7 #########################################################

                breaklabel6.config(textvariable=brkmess)
                breaklabel6.grid(row = rowCount+21 , column=0,pady = 5,sticky=tk.NW)

                caselabel6.config(textvariable=casemess7)
                caselabel6.grid(row = rowCount+22 , column=0,pady = 5,sticky=tk.NW)
                printlabel7.config(textvariable=printmess)
                printlabel7.grid(row = rowCount+23 , column=0,pady = 5,sticky=tk.NW)
                case9text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case9text.grid(row =rowCount+23, column=1,pady = 5)

                ################ case 8 #########################################################

                breaklabel7.config(textvariable=brkmess)
                breaklabel7.grid(row = rowCount+24 , column=0,pady = 5,sticky=tk.NW)

                caselabel7.config(textvariable=casemess8)
                caselabel7.grid(row = rowCount+25 , column=0,pady = 5,sticky=tk.NW)
                printlabel8.config(textvariable=printmess)
                printlabel8.grid(row = rowCount+26 , column=0,pady = 5,sticky=tk.NW)
                case10text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case10text.grid(row =rowCount+26, column=1,pady = 5)

                ################ case 9 #########################################################

                breaklabel8.config(textvariable=brkmess)
                breaklabel8.grid(row = rowCount+27 , column=0,pady = 5,sticky=tk.NW)

                caselabel8.config(textvariable=casemess9)
                caselabel8.grid(row = rowCount+28 , column=0,pady = 5,sticky=tk.NW)
                printlabel9.config(textvariable=printmess)
                printlabel9.grid(row = rowCount+29 , column=0,pady = 5,sticky=tk.NW)
                case11text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case11text.grid(row =rowCount+29, column=1,pady = 5)
                ####################################case default #######################################
                breaklabel9.config(textvariable=brkmess)
                breaklabel9.grid(row = rowCount+30 , column=0,pady = 5,sticky=tk.NW)

                defaultlabel9.config(textvariable=defaultmess)
                defaultlabel9.grid(row = rowCount+31 , column=0,pady = 5,sticky=tk.NW)
                dfeaultprintlabel9.config(textvariable=printmess)
                dfeaultprintlabel9.grid(row = rowCount+32 , column=0,pady = 5,sticky=tk.NW)
                defaulttext10.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                defaulttext10.grid(row =rowCount+32, column=1,pady = 5)
           elif(entervalue == "1 to 10"):
                defaulttext1.grid_forget()
                defaulttext4.grid_forget()
                defaulttext3.grid_forget()
                defaulttext2.grid_forget()

                casetenwidgets()

               ######################### case 1######################################
                caselabel.config(textvariable=casemess1)
                caselabel.grid(row = rowCount+1 , column=0,pady = 5,sticky=tk.NW)
                printlabel.config(textvariable=printmess)
                printlabel.grid(row = rowCount+2 , column=0,pady = 5,sticky=tk.NW)

                case1text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case1text.grid(row =rowCount+2, column=1,pady = 5)

                ################# case 2 ###########################################
                breaklabel1.config(textvariable=brkmess)
                breaklabel1.grid(row = rowCount+3 , column=0,pady = 5,sticky=tk.NW)
                caselabel1.config(textvariable=casemess2)
                caselabel1.grid(row = rowCount+4 , column=0,pady = 5,sticky=tk.NW)
                printlabel2.config(textvariable=printmess)
                printlabel2.grid(row = rowCount+5 , column=0,pady = 5,sticky=tk.NW)

                 # case4text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                 # case4text.grid(row =rowCount+5, column=1,pady = 5,padx=2,sticky=W)
                 # add_placeholder_to(case4text, 'case 2')
                case3text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case3text.grid(row =rowCount+5, column=1,pady = 5)

                ######################## case 3 #####################################################
                breaklabel2.config(textvariable=brkmess)
                breaklabel2.grid(row = rowCount+6 , column=0,pady = 5,sticky=tk.NW)
                caselabel2.config(textvariable=casemess3)
                caselabel2.grid(row = rowCount+7 , column=0,pady = 5,sticky=tk.NW)
                printlabel3.config(textvariable=printmess)
                printlabel3.grid(row = rowCount+8 , column=0,pady = 5,sticky=tk.NW)
                case5text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case5text.grid(row =rowCount+8, column=1,pady = 5)
                 # add_placeholder_to(case5text, 'case 3')

                 #############################case 4 ###############################################

                breaklabel3.config(textvariable=brkmess)
                breaklabel3.grid(row = rowCount+9 , column=0,pady = 5,sticky=tk.NW)
                caselabel3.config(textvariable=casemess4)
                caselabel3.grid(row = rowCount+10 , column=0,pady = 5,sticky=tk.NW)
                printlabel4.config(textvariable=printmess)
                printlabel4.grid(row = rowCount+11 , column=0,pady = 5,sticky=tk.NW)
                case6text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case6text.grid(row =rowCount+11, column=1,pady = 5)

                ###############################case 5 #############################################

                breaklabel4.config(textvariable=brkmess)
                breaklabel4.grid(row = rowCount+12 , column=0,pady = 5,sticky=tk.NW)

                caselabel4.config(textvariable=casemess5)
                caselabel4.grid(row = rowCount+13 , column=0,pady = 5,sticky=tk.NW)
                printlabel5.config(textvariable=printmess)
                printlabel5.grid(row = rowCount+14 , column=0,pady = 5,sticky=tk.NW)
                case7text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case7text.grid(row =rowCount+14, column=1,pady = 5)

                ################ case 6 #########################################################

                breaklabel5.config(textvariable=brkmess)
                breaklabel5.grid(row = rowCount+18 , column=0,pady = 5,sticky=tk.NW)

                caselabel5.config(textvariable=casemess6)
                caselabel5.grid(row = rowCount+19 , column=0,pady = 5,sticky=tk.NW)
                printlabel6.config(textvariable=printmess)
                printlabel6.grid(row = rowCount+20 , column=0,pady = 5,sticky=tk.NW)
                case8text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case8text.grid(row =rowCount+20, column=1,pady = 5)

                ################ case 7 #########################################################

                breaklabel6.config(textvariable=brkmess)
                breaklabel6.grid(row = rowCount+21 , column=0,pady = 5,sticky=tk.NW)

                caselabel6.config(textvariable=casemess7)
                caselabel6.grid(row = rowCount+22 , column=0,pady = 5,sticky=tk.NW)
                printlabel7.config(textvariable=printmess)
                printlabel7.grid(row = rowCount+23 , column=0,pady = 5,sticky=tk.NW)
                case9text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case9text.grid(row =rowCount+23, column=1,pady = 5)

                ################ case 8 #########################################################

                breaklabel7.config(textvariable=brkmess)
                breaklabel7.grid(row = rowCount+24 , column=0,pady = 5,sticky=tk.NW)

                caselabel7.config(textvariable=casemess8)
                caselabel7.grid(row = rowCount+25 , column=0,pady = 5,sticky=tk.NW)
                printlabel8.config(textvariable=printmess)
                printlabel8.grid(row = rowCount+26 , column=0,pady = 5,sticky=tk.NW)
                case10text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case10text.grid(row =rowCount+26, column=1,pady = 5)

                ################ case 9 #########################################################

                breaklabel8.config(textvariable=brkmess)
                breaklabel8.grid(row = rowCount+27 , column=0,pady = 5,sticky=tk.NW)

                caselabel8.config(textvariable=casemess9)
                caselabel8.grid(row = rowCount+28 , column=0,pady = 5,sticky=tk.NW)
                printlabel9.config(textvariable=printmess)
                printlabel9.grid(row = rowCount+29 , column=0,pady = 5,sticky=tk.NW)
                case11text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case11text.grid(row =rowCount+29, column=1,pady = 5)

                ################ case 10 #########################################################

                breaklabel9.config(textvariable=brkmess)
                breaklabel9.grid(row = rowCount+30 , column=0,pady = 5,sticky=tk.NW)

                caselabel9.config(textvariable=casemess10)
                caselabel9.grid(row = rowCount+31 , column=0,pady = 5,sticky=tk.NW)
                printlabel10.config(textvariable=printmess)
                printlabel10.grid(row = rowCount+32 , column=0,pady = 5,sticky=tk.NW)
                case12text.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                case12text.grid(row =rowCount+32, column=1,pady = 5)

                ####################################case default #######################################
                breaklabel10.config(textvariable=brkmess)
                breaklabel10.grid(row = rowCount+33 , column=0,pady = 5,sticky=tk.NW)

                defaultlabel11.config(textvariable=defaultmess)
                defaultlabel11.grid(row = rowCount+34 , column=0,pady = 5,sticky=tk.NW)
                dfeaultprintlabel10.config(textvariable=printmess)
                dfeaultprintlabel10.grid(row = rowCount+35 , column=0,pady = 5,sticky=tk.NW)
                defaulttext11.config(justify= 'right',width=10,bg="#47a3a5",borderwidth=0,highlightthickness=0)
                defaulttext11.grid(row =rowCount+35, column=1,pady = 5)

       omswitch = OptionMenu( aWindow, self.sv, *sorted(Dic.keys()))
       omswitch.grid(row=row,column= col,sticky=tk.NW,columnspan=2,pady = 10)
       omswitch.config(height=0,bd=0,highlightthickness=0,width=4)
       self.sv.trace("w", option_changedswitch)
       choices = [1,2,3,4,5]

       # self.b = Button(aWindow,text=setVal,command=lambda: optionChanged2(self.sv,1,2))
       proceedswitch = Button(canvasfunc)
       proceedswitch.config(text ="Proceed",command =lambda row=rowCount,columnspan=1, column=6: switchcase(self.sv,row, column) ,fg= "white" ,bg = "#ab4345",width=7)
       proceedswitch.grid(row =rowCount,sticky=tk.NW, column=6,pady = 10)

       cancelswitch = Button(canvasfunc)
       cancelswitch.config(image = close,command =lambda row=rowCount, column=7: dltswitch(row, column)  ,bd=0, highlightthickness=0,bg = "White")
       cancelswitch.grid(row = rowCount,sticky=tk.NW,column=7,pady = 10,padx=2)
def switch():

    global rowCount
    global cancelswitch
    global switchlabel
    global switchVal1
    global Proceedswitch
    global construct

    construct = 1


    clear_all()

    switchmessage.set("Switch Case")
    # for i in range(1):
    switchlabel = Label(canvasfunc)
    switchlabel.config(width = 15,textvariable=switchmessage)
    switchlabel.grid(row = rowCount ,columnspan=2, sticky=tk.NW,column=0,pady = 10)

    app = OptionMenuDemoswitch(canvasfunc,rowCount,2)

    switchVal1 = Entry(canvasfunc)
    switchVal1.config(justify= 'right',width=5,bg="#47a3a5",borderwidth=0,highlightthickness=0)
    switchVal1.grid(row =rowCount, sticky=tk.NW,columnspan=2, column=4,pady = 10,ipady=3)
    add_placeholder_to(switchVal1, 'Int i')

        # Proceedswitch = Button(canvasfunc, text ="Proceed",fg = "white",command = lambda row=rowCount, column=3: switchcase(row, column) ,bg = "#ab4345",width=20,height=0,pady = -800)
        # # Proceedswitch.place(relx=1.0,rely=0.98, x=-170, y=2, anchor=S)
        # Proceedswitch.grid(row = rowCount, column=3,padx=5)
        #populate_menu(drop_menuswitch, one=one,two=two,three=three,four=four,five=five,six = six,seven=seven,eight=eight,nine=nine,ten=ten,eleven=eleven,twelve=twelve,change=change_menu)

    rowCount = rowCount+1
    # colconfig = canvasfucnwidth/10
    # canvasfunc.columnconfigure('all', minsize = colconfig)


    colconfig = (canvasfucnwidth-80)/7
    canvasfunc.columnconfigure(0, minsize = 80)
    canvasfunc.columnconfigure(1, minsize = colconfig-5)
    canvasfunc.columnconfigure(2, minsize = colconfig-5)
    canvasfunc.columnconfigure(3, minsize = colconfig-5)
    canvasfunc.columnconfigure(4, minsize = colconfig-5)
    canvasfunc.columnconfigure(5, minsize = colconfig-5)
    canvasfunc.columnconfigure(6, minsize = colconfig-5)
    canvasfunc.columnconfigure(7, minsize = colconfig-5)
def dltswitch(number,test):
    if(caselabel.winfo_exists()):
        caselabel.grid_forget()
    if(printlabel.winfo_exists()):
        printlabel.grid_forget()
    if(case1text.winfo_exists()):
        case1text.grid_forget()
    if(breaklabel.winfo_exists()):
        breaklabel.grid_forget()
    if(defaultlabel.winfo_exists()):
        defaultlabel.grid_forget()
    if(dfeaultprintlabel1.winfo_exists()):
        dfeaultprintlabel1.grid_forget()
    if(defaulttext1.winfo_exists()):
        defaulttext1.grid_forget()
    if(caselabel1.winfo_exists()):
        caselabel1.grid_forget()
    if(printlabel2.winfo_exists()):
        printlabel2.grid_forget()
    if(case3text.winfo_exists()):
        case3text.grid_forget()
    if(breaklabel2.winfo_exists()):
        breaklabel2.grid_forget()
    if(caselabel2.winfo_exists()):
        caselabel2.grid_forget()
    if(printlabel3.winfo_exists()):
        printlabel3.grid_forget()
    if(case5text.winfo_exists()):
        case5text.grid_forget()
    if(breaklabel3.winfo_exists()):
        breaklabel3.grid_forget()
    if(defaultlabel3.winfo_exists()):
        defaultlabel3.grid_forget()
    if(printlabel4.winfo_exists()):
        printlabel4.grid_forget()
    if(case6text.winfo_exists()):
        case6text.grid_forget()
    if(breaklabel4.winfo_exists()):
        breaklabel4.grid_forget()
    if(defaultlabel2.winfo_exists()):
        defaultlabel2.grid_forget()
    if(defaultlabel3.winfo_exists()):
        defaultlabel3.grid_forget()
    if(defaultlabel4.winfo_exists()):
        defaultlabel4.grid_forget()
    if(caselabel4.winfo_exists()):
        caselabel4.grid_forget()
    if(printlabel5.winfo_exists()):
        printlabel5.grid_forget()
    if(case7text.winfo_exists()):
        case7text.grid_forget()
    if(breaklabel5.winfo_exists()):
        breaklabel5.grid_forget()
    if(defaultlabel5.winfo_exists()):
        defaultlabel5.grid_forget()
    if(dfeaultprintlabel5.winfo_exists()):
        dfeaultprintlabel5.grid_forget()
    if(dfeaultprintlabel4.winfo_exists()):
        dfeaultprintlabel4.grid_forget()
    if(dfeaultprintlabel3.winfo_exists()):
        dfeaultprintlabel3.grid_forget()
    if(dfeaultprintlabel2.winfo_exists()):
        dfeaultprintlabel2.grid_forget()
    if(defaulttext5.winfo_exists()):
        defaulttext5.grid_forget()
    if(defaulttext4.winfo_exists()):
        defaulttext4.grid_forget()
    if(defaulttext3.winfo_exists()):
        defaulttext3.grid_forget()
    if(defaulttext2.winfo_exists()):
        defaulttext2.grid_forget()
    if(caselabel3.winfo_exists()):
        caselabel3.grid_forget()
        breaklabel1
    if(breaklabel2.winfo_exists()):
        breaklabel2.grid_forget()
    if(breaklabel3.winfo_exists()):
        breaklabel3.grid_forget()
    if(breaklabel4.winfo_exists()):
        breaklabel4.grid_forget()
    if(breaklabel5.winfo_exists()):
        breaklabel5.grid_forget()
    if(breaklabel1.winfo_exists()):
        breaklabel1.grid_forget()
    if(proceedswitch.winfo_exists()):
        proceedswitch.grid_forget()

    caseonewidgets()
    casetwowidgets()
    casethreewidgets()
    casefourwidgets()
    casefivewidgets()
    casesixwidgets()
    casesevenwidgets()
    caseeightwidgets()
    caseninewidgets()
    casetenwidgets()


    for item in canvasfunc.grid_slaves():
        if int(item.grid_info()["row"]) == number:
            item.grid_forget()
def switchcase(switchsv,number,test):

    global case1text
    global case3text
    global case5text
    global case6text
    global case7text
    global switchVal1
    global l6

    caseval = switchsv.get()
    switchvalue = switchVal1.get()


    if(switchvalue == "Int i"):
        ForInvalidInput()
    if(not(switchvalue.isdigit())):

        ForInvalidInput()
    if(int(switchvalue) == ""  or int(switchvalue) == "Define i" ):

        emptyfields()



    case1print = case1text.get()
    case2print = case3text.get()
    case3print = case5text.get()
    case4print = case6text.get()
    case5print = case7text.get()
    case6print = case8text.get()
    case7print = case9text.get()
    case8print = case10text.get()
    case9print = case11text.get()
    case10print = case12text.get()
    default6 = defaulttext6.get()
    default7 = defaulttext7.get()
    default8 = defaulttext8.get()
    default9 = defaulttext9.get()
    default10 = defaulttext10.get()
    default5 = defaulttext5.get()
    default4 = defaulttext4.get()
    default3 = defaulttext3.get()
    default2= defaulttext2.get()
    default1= defaulttext1.get()

    try:
        if(switchvalue.isdigit()):

            if(caseval == "1" and switchvalue == "1"):
                outputtext.insert(END, str(case1print)+ '\n')
            if(caseval == "1" and switchvalue != "1"):
                outputtext.insert(END, str(default1)+ '\n')
            if(caseval == "1 to 2" and switchvalue == "2"):
                outputtext.insert(END, str(case2print)+ '\n')
            if(caseval == "1 to 2" and  switchvalue == "1"):
                outputtext.insert(END, str(case1print)+ '\n')
            if(caseval == "1 to 2" and switchvalue != "1" and switchvalue != "2" ):
                outputtext.insert(END, str(default2)+ '\n')
            if(caseval == "1 to 3" and switchvalue == "1"  ):
                outputtext.insert(END, str(case1print)+ '\n')
            if(caseval == "1 to 3" and switchvalue == "2"  ):
                outputtext.insert(END, str(case2print)+ '\n')
            if(caseval == "1 to 3" and switchvalue == "3"  ):
                outputtext.insert(END, str(case3print)+ '\n')
            if(caseval == "1 to 3" and switchvalue != "3" and switchvalue != "2"  and switchvalue != "1"  ):
                outputtext.insert(END, str(default3)+ '\n')
            if(caseval == "1 to 4" and switchvalue == "4"  ):
                outputtext.insert(END, str(case4print)+ '\n')
            if(caseval == "1 to 4" and switchvalue == "3"  ):
                outputtext.insert(END, str(case3print)+ '\n')
            if(caseval == "1 to 4" and switchvalue == "2"  ):
                outputtext.insert(END, str(case2print)+ '\n')
            if(caseval == "1 to 4" and switchvalue == "1"  ):
                outputtext.insert(END, str(case1print)+ '\n')
            if(caseval == "1 to 4" and switchvalue != "4"  and switchvalue != "3" and switchvalue != "2"  and switchvalue != "1"  ):
                outputtext.insert(END, str(default4)+ '\n')
            if(caseval == "1 to 5" and switchvalue == "1"  ):
                outputtext.insert(END, str(case1print)+ '\n')
            if(caseval == "1 to 5" and switchvalue == "2"  ):
                outputtext.insert(END, str(case2print)+ '\n')
            if(caseval == "1 to 5" and switchvalue == "3"  ):
                outputtext.insert(END, str(case3print)+ '\n')
            if(caseval == "1 to 5" and switchvalue == "4"  ):
                outputtext.insert(END, str(case4print)+ '\n')
            if(caseval == "1 to 5" and switchvalue == "5"  ):
                outputtext.insert(END, str(case5print)+ '\n')
            if(caseval == "1 to 5" and switchvalue != "4" and switchvalue != "5" and switchvalue != "3" and switchvalue != "2"  and switchvalue != "1"  ):
                outputtext.insert(END, str(default5)+ '\n')
            if(caseval == "1 to 6" and switchvalue == "1"  ):
                outputtext.insert(END, str(case1print)+ '\n')
            if(caseval == "1 to 6" and switchvalue == "2"  ):
                outputtext.insert(END, str(case2print)+ '\n')
            if(caseval == "1 to 6" and switchvalue == "3"  ):
                outputtext.insert(END, str(case3print)+ '\n')
            if(caseval == "1 to 6" and switchvalue == "4"  ):
                outputtext.insert(END, str(case4print)+ '\n')
            if(caseval == "1 to 6" and switchvalue == "5"  ):
                outputtext.insert(END, str(case5print)+ '\n')
            if(caseval == "1 to 6" and switchvalue == "6"  ):
                outputtext.insert(END, str(case6print)+ '\n')
            if(caseval == "1 to 6" and switchvalue != "6" and switchvalue != "4" and switchvalue != "5" and switchvalue != "3" and switchvalue != "2"  and switchvalue != "1"  ):
                outputtext.insert(END, str(default5)+ '\n')
            if(caseval == "1 to 7" and switchvalue == "1"  ):
                outputtext.insert(END, str(case1print)+ '\n')
            if(caseval == "1 to 7" and switchvalue == "2"  ):
                outputtext.insert(END, str(case2print)+ '\n')
            if(caseval == "1 to 7" and switchvalue == "3"  ):
                outputtext.insert(END, str(case3print)+ '\n')
            if(caseval == "1 to 7" and switchvalue == "4"  ):
                outputtext.insert(END, str(case4print)+ '\n')
            if(caseval == "1 to 7" and switchvalue == "5"  ):
                outputtext.insert(END, str(case5print)+ '\n')
            if(caseval == "1 to 7" and switchvalue == "6"  ):
                outputtext.insert(END, str(case6print)+ '\n')
            if(caseval == "1 to 7" and switchvalue == "7"  ):
                outputtext.insert(END, str(case7print)+ '\n')
            if(caseval == "1 to 7"  and switchvalue != "7" and switchvalue != "6" and switchvalue != "4" and switchvalue != "5" and switchvalue != "3" and switchvalue != "2"  and switchvalue != "1"  ):
                outputtext.insert(END, str(default5)+ '\n')
            if(caseval == "1 to 8" and switchvalue == "1"  ):
                outputtext.insert(END, str(case1print)+ '\n')
            if(caseval == "1 to 8" and switchvalue == "2"  ):
                outputtext.insert(END, str(case2print)+ '\n')
            if(caseval == "1 to 8" and switchvalue == "3"  ):
                outputtext.insert(END, str(case3print)+ '\n')
            if(caseval == "1 to 8" and switchvalue == "4"  ):
                outputtext.insert(END, str(case4print)+ '\n')
            if(caseval == "1 to 8" and switchvalue == "5"  ):
                outputtext.insert(END, str(case5print)+ '\n')
            if(caseval == "1 to 8" and switchvalue == "6"  ):
                outputtext.insert(END, str(case6print)+ '\n')
            if(caseval == "1 to 8" and switchvalue == "7"  ):
                outputtext.insert(END, str(case7print)+ '\n')
            if(caseval == "1 to 8" and switchvalue == "8"  ):
                outputtext.insert(END, str(case8print)+ '\n')
            if(caseval == "1 to 8"  and switchvalue != "8" and switchvalue != "7" and switchvalue != "6" and switchvalue != "4" and switchvalue != "5" and switchvalue != "3" and switchvalue != "2"  and switchvalue != "1"  ):
                outputtext.insert(END, str(default5)+ '\n')
            if(caseval == "1 to 9" and switchvalue == "1"  ):
                outputtext.insert(END, str(case1print)+ '\n')
            if(caseval == "1 to 9" and switchvalue == "2"  ):
                outputtext.insert(END, str(case2print)+ '\n')
            if(caseval == "1 to 9" and switchvalue == "3"  ):
                outputtext.insert(END, str(case3print)+ '\n')
            if(caseval == "1 to 9" and switchvalue == "4"  ):
                outputtext.insert(END, str(case4print)+ '\n')
            if(caseval == "1 to 9" and switchvalue == "5"  ):
                outputtext.insert(END, str(case5print)+ '\n')
            if(caseval == "1 to 9" and switchvalue == "6"  ):
                outputtext.insert(END, str(case6print)+ '\n')
            if(caseval == "1 to 9" and switchvalue == "7"  ):
                outputtext.insert(END, str(case7print)+ '\n')
            if(caseval == "1 to 9" and switchvalue == "8"  ):
                outputtext.insert(END, str(case8print)+ '\n')
            if(caseval == "1 to 9" and switchvalue == "9"  ):
                outputtext.insert(END, str(case9print)+ '\n')
            if(caseval == "1 to 9"  and switchvalue != "9" and switchvalue != "8" and switchvalue != "7" and switchvalue != "6" and switchvalue != "4" and switchvalue != "5" and switchvalue != "3" and switchvalue != "2"  and switchvalue != "1"  ):
                outputtext.insert(END, str(default5)+ '\n')
            if(caseval == "1 to 10" and switchvalue == "1"  ):
                outputtext.insert(END, str(case1print)+ '\n')
            if(caseval == "1 to 10" and switchvalue == "2"  ):
                outputtext.insert(END, str(case2print)+ '\n')
            if(caseval == "1 to 10" and switchvalue == "3"  ):
                outputtext.insert(END, str(case3print)+ '\n')
            if(caseval == "1 to 10" and switchvalue == "4"  ):
                outputtext.insert(END, str(case4print)+ '\n')
            if(caseval == "1 to 10" and switchvalue == "5"  ):
                outputtext.insert(END, str(case5print)+ '\n')
            if(caseval == "1 to 10" and switchvalue == "6"  ):
                outputtext.insert(END, str(case6print)+ '\n')
            if(caseval == "1 to 10" and switchvalue == "7"  ):
                outputtext.insert(END, str(case7print)+ '\n')
            if(caseval == "1 to 10" and switchvalue == "8"  ):
                outputtext.insert(END, str(case8print)+ '\n')
            if(caseval == "1 to 10" and switchvalue == "9"  ):
                outputtext.insert(END, str(case9print)+ '\n')
            if(caseval == "1 to 10" and switchvalue == "10"  ):
                outputtext.insert(END, str(case10print)+ '\n')
            if(caseval == "1 to 10" and switchvalue != "10" and switchvalue != "9" and switchvalue != "8" and switchvalue != "7" and switchvalue != "6" and switchvalue != "4" and switchvalue != "5" and switchvalue != "3" and switchvalue != "2"  and switchvalue != "1"  ):
                outputtext.insert(END, str(default5)+ '\n')
    except ValueError:
        if(not(switchvalue.isdigit())):

            ForInvalidInput()
        if(int(switchvalue) == ""  or int(switchvalue) == "Define i" ):

            emptyfields()


    def clearlog():
        outputtext.delete('1.0', END)
    Reset = Button(canvasleft,bg="#f2f2f2", text ="Clear Log",image = clearlogimage, compound= "left",command = clearlog,width=Buttonwidth,height=0,pady = -800)

    Reset.grid(row=4,column=5,pady=2)
    #Reset.place(relx=0.80,rely=0.970, x=-170, y=2, anchor=S)

########################################END SWITCH CASE #######################################################
################################# MENU BAR BUTTON #########################################################################
add1btn = PhotoImage(file = "Images/add_icon.gif")
addconstructbtn = PhotoImage(file = "Images/add1.gif")
addcolrbtn = PhotoImage(file = "Images/add2.gif")
addgeneralbtn = PhotoImage(file = "Images/add3.gif")

contructphto = ImageTk.PhotoImage(file = "Images/construct.jpg")
Basicloops=Label(canvasright,image=contructphto,height=0)
Basicloops.grid(row =1 , column=0,sticky=W,pady = 3,padx=0)
Basicloops.config(bd=0, highlightthickness=0)


For=tk.Button(canvasright,relief="raised",width = 15,fg = "white", text= "Loop",command = Forloop,bg = "#213872")
For.grid(row =2 , column=0,pady = 3)

addbtn=tk.Button(canvasright,image = add1btn,compound= "left",bg= "#47a3a5", command = Forloop, bd=0, highlightthickness=0)
addbtn.grid(row=2,column=1,padx=(0,10))

Ifelsephoto = ImageTk.PhotoImage(file = "Images/if_else.jpg")
Ifelse=Button(canvasright,relief="raised",width = 15,fg = "white", text= "If-Else",command = ifElse,bg = "#213872" )
Ifelse.grid(row =3 , column=0,pady = 3)

addifbtn=Button(canvasright,image = add1btn, command = ifElse,bg= "#47a3a5",bd = 0 , highlightthickness = 0)
addifbtn.grid(row=3,column=1,padx=(0,10))

Nestedphoto = ImageTk.PhotoImage(file = "Images/nested.jpg")
NestedIfElse=Button(canvasright,relief="raised",bg = "#213872",width = 15,text= "Nested If",fg = "white",command = nestedIfElse)
NestedIfElse.grid(row =4 , column=0,pady = 3)
addnestedifbtn=Button(canvasright,image = add1btn,command = nestedIfElse,bg= "#47a3a5",bd = 0 , highlightthickness = 0)
addnestedifbtn.grid(row=4,column=1,padx=(0,10))

Switchphoto = ImageTk.PhotoImage(file = "Images/switch_case.jpg")
Switch=Button(canvasright,relief="raised",bg = "#213872",width = 15,text= "Switch Case",fg = "white",command = switch)
Switch.grid(row =5 , column=0,pady = 3)
addswitchbtn=Button(canvasright,image = add1btn, command = switch,bg= "#47a3a5",bd = 0 , highlightthickness = 0)
addswitchbtn.place(relx=1.8,rely=0.223, x=-194, y=2, anchor=N)
addswitchbtn.grid(row=5,column=1,padx=(0,10))

Drawphoto = ImageTk.PhotoImage(file = "Images/draw.jpg")
shapesLabel=Label(canvasright,image=Drawphoto)
shapesLabel.grid(row =6 , column=0,sticky=W,pady = 3,padx=0)
shapesLabel.config(bd=0, highlightthickness=0)
rectanglephoto = ImageTk.PhotoImage(file = "Images/rectangles.jpg")
Rectangle=Button(canvasright,relief="raised",bg = "#f29e24",width = 15,text= "Rectangles",fg = "white",command = RectangleButton)
Rectangle.grid(row =7 , column=0,pady = 3)
addrectbtn=Button(canvasright,image = addconstructbtn, command = RectangleButton,bg= "#47a3a5",bd = 0 , highlightthickness = 0)

addrectbtn.grid(row=7,column=1,padx=(0,10))
sqaurephoto = ImageTk.PhotoImage(file = "Images/squares.jpg")
Sqaures=Button(canvasright,relief="raised",bg = "#f29e24",width = 15,text= "Squares",fg = "white",command = SqaureButton)
Sqaures.grid(row =8 , column=0,pady =3)
addsqbtn=Button(canvasright,image = addconstructbtn, command = SqaureButton,bg= "#47a3a5",bd = 0 , highlightthickness = 0)

addsqbtn.grid(row=8,column=1,padx=(0,10))

circlephoto = ImageTk.PhotoImage(file = "Images/circle.jpg")
Circle=Button(canvasright,relief="raised",bg = "#f29e24",text= "Circle",fg = "white",width = 15,command = CircleButton)
Circle.grid(row =9 , column=0,pady = 3)
addcirbtn=Button(canvasright,image = addconstructbtn, command = CircleButton,bg= "#47a3a5",bd = 0 , highlightthickness = 0)

addcirbtn.grid(row=9,column=1,padx=(0,10))

linephoto = ImageTk.PhotoImage(file = "Images/line.jpg")
Line=Button(canvasright,relief="raised",bg = "#f29e24",width = 15,command = LineButton,text= "Lines",fg = "white")
Line.grid(row =10 , column=0,pady = 3)
addlinebtn=Button(canvasright,image = addconstructbtn, command = LineButton,bg= "#47a3a5",bd = 0 , highlightthickness = 0)

addlinebtn.grid(row=10,column=1,padx=(0,10))

coloringophto = ImageTk.PhotoImage(file = "Images/coloring.jpg")

Coloring=Label(canvasright,image=coloringophto)
Coloring.grid(row =11 , column=0,sticky=W,pady = 3,padx=0)
Coloring.config(bd=0, highlightthickness=0)

Textcolorphoto = ImageTk.PhotoImage(file = "Images/text-color.jpg")
TextColor=Button(canvasright,relief="raised",command= textcolor,text= "Text Color",fg = "white",bg = "#85d231",width = 15)
TextColor.grid(row =12 , column=0,pady = 3)
addtextbtn=Button(canvasright,image = addcolrbtn, command = textcolor,bg= "#47a3a5",bd = 0 , highlightthickness = 0)
addtextbtn.grid(row=12,column=1,padx=(0,10))

backgroundphoto = ImageTk.PhotoImage(file = "Images/background.jpg")
Background=Button(canvasright,relief="raised",text= "Background",fg = "white",bg = "#85d231",width = 15,command = Background)
Background.grid(row =13 , column=0,pady = 3)
addbgbtn=Button(canvasright,image = addcolrbtn,command = Background,bg= "#47a3a5",bd = 0 , highlightthickness = 0)

addbgbtn.grid(row=13,column=1,padx=(0,10))
generalphoto = ImageTk.PhotoImage(file = "Images/general.jpg")

Genenral=Label(canvasright,image=generalphoto,anchor='w')
Genenral.grid(row =14 , column=0,sticky=W,pady = 3,padx=0)
Genenral.config(bd=0, highlightthickness=0)
Genenral.grid_rowconfigure(14, weight=1)
texttypephoto = ImageTk.PhotoImage(file = "Images/text_type.jpg")

TextType=Button(canvasright,relief="raised",command = texttype,text= "Text Type",fg = "white",bg = "#bd4143",width = 15)
TextType.grid(row =15 , column=0,pady = 3)
TextType.config(bd=0, highlightthickness=0,highlightcolor="#ab4345")
addtexttypebtn=Button(canvasright,image = addgeneralbtn, command = texttype,bg= "#47a3a5",bd = 0 , highlightthickness = 0)
addtexttypebtn.grid(row=15,column=1,padx=(0,10))


root.mainloop()
