# coding:utf-8
"""
  PYTHON

  Widgets 
    variables de contrôle
"""
from tkinter import *

"""
creation d'un ecouteur d'evenement
"""


def updateLabel(*args):
    varLabel.set(varEntry.get())


app = Tk()
app.title("Variables de contrôle")
app.geometry("800x450")

# widget
varEntry = StringVar()
varEntry.trace("w", updateLabel)

entry = Entry(app, textvariable=varEntry, width=25)
entry.pack()

varLabel = StringVar()
label = Label(
    app, textvariable=varLabel)
# varLabel.set("Une façon simple et rapide de contrôler son affichage: les variables")
label.pack()


app.mainloop()
