# coding: utf-8
 
from tkinter import * 

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

# label
label = Label(fenetre, text="Texte par défaut", bg="yellow")
label.pack()

value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=string, width=30)
entree.pack()

fenetre.mainloop()