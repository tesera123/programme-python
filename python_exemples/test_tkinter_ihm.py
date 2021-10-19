import tkinter
import tkinter as tk
from tkinter import messagebox

#top = tkinter.Tk()

#def helloCallBack():
#   messagebox.showinfo( "Hello Python", "Hello World")
#B = tkinter.Button(top, text ="Hello", command = helloCallBack)

#B.pack()
#top.mainloop()


gui = tk.Tk()
gui.geometry("300x200")

def getEntry():
    res = myEntry.get()
    print(res)

def getEntry2():
    var = myEntry2.get()
    print(var)

myEntry2 = tk.Entry(gui, width=40)
myEntry2.pack(pady=20)
btn = tk.Button(gui, height=1, width=10, text="Lire", command=getEntry2)

myEntry = tk.Entry(gui, width=40)
myEntry.pack(pady=20)
btn = tk.Button(gui, height=1, width=10, text="Lire", command= lambda:[getEntry2(), getEntry()])

btn.pack()
gui.mainloop()