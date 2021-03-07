import tkinter
from tkinter import *

ex1 = tkinter.Tk()
ex1.title("EX1")
label1 = tkinter.Label(ex1, text = "A",bg = "Red").pack(side = "left",fill=BOTH,expand=YES,)
label3 = tkinter.Label(ex1, text = "C",bg = "blue").pack(side = "left",fill=BOTH,expand=YES,)

ex2 = tkinter.Tk()
ex2.title("EX2")
relwin = Frame(ex2)
relwin.place(relx=0.5, rely=0.5, anchor=CENTER,relwidth=0.67,relheight=1)
labela = tkinter.Label(relwin, text = "A",bg = "Red").pack(fill=BOTH,expand=YES,)
labelb = tkinter.Label(relwin, text = "B",bg = "yellow").pack(fill=BOTH,expand=YES,)
labelc = tkinter.Label(relwin, text = "C",bg = "blue").pack(fill=BOTH,expand=YES,)


window = tkinter.Tk()
window.title("EX3")
win = Frame(window,bd=5, relief=RIDGE)
win2 = Frame(window,bd=5, relief=RAISED)
win.pack(side = "left",fill=BOTH,expand=YES)
win2.pack(side = "right",fill=BOTH,expand=YES)

label1 = tkinter.Label(win, text = "label1",bg = "blue").pack(fill=BOTH,expand=YES,)
label2 = tkinter.Label(win, text = "label2",bg = "white").pack(fill=BOTH,expand=YES)
label3 = tkinter.Label(win2, text = "label3",bg = "white").pack(fill=BOTH,expand=YES,)
label4 = tkinter.Label(win2, text = "label4",bg = "blue").pack(fill=BOTH,expand=YES)



ex4 = tkinter.Tk()
ex4.title("EX4")
ex4.geometry("640x480")
#labelw = tkinter.Label(ex4, text = "test",bg = "red").place( x=5, y=5,relwidth=1, relheight=1,width=-10, height=-10)
labela = tkinter.Label(ex4, text = "yellow",bg = "yellow").place(x = 100,y=5)
labelb = tkinter.Label(ex4, text = "Blue",bg = "blue").place(relx=0.5, rely=0.5, anchor=CENTER)
labelc = tkinter.Label(ex4, text = "green",bg = "green").place(anchor=CENTER,relx=0.5, rely=0.5,x = 100, y =50)
labeld = tkinter.Label(ex4, text = "orange",bg = "orange").place(anchor=NE,relx=1,x=-5,y=5)



ex5 = tkinter.Tk()
ex5.title("EX5")
Label(ex5, text = "Amount of loan:").grid(row = 0, column = 0,sticky=NSEW)
Label(ex5, text = "Interest rate(as %):").grid(row = 1,column = 0,sticky=NSEW)
Entry(ex5).grid(row = 0, column = 1,sticky=NSEW)
Entry(ex5).grid(row = 1, column = 1,sticky=NSEW)
Button(ex5, text = "Calculate Monthly Payment").grid(row = 2,columnspan = 2,sticky=NSEW)
Label(ex5, text = "Monthly Payment:").grid(row = 3,column = 0,sticky=NSEW)
Entry(ex5).grid(row = 3, column = 1,sticky=NSEW)
ex5.columnconfigure(0, weight=1)
ex5.columnconfigure(1, weight=1)
ex5.rowconfigure(0, weight=1)
ex5.rowconfigure(1, weight=1)
ex5.rowconfigure(2, weight=1)
ex5.rowconfigure(3, weight=1)

mainloop()