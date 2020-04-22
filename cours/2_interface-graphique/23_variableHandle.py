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

# entrée radio:


def updateRadio(*args):
    # print("""  """f"Sexe: {varGender.get()}")
    msg = ""
    if varGender.get():
        msg = "salut mec!"
    else:
        msg = "Mes hommages, madame!"
    return varLabelGender.set(msg)


varGender = IntVar()
varGender.trace("w", updateRadio)
radio1 = Radiobutton(app, text="homme", variable=varGender, value=1)
radio2 = Radiobutton(app, text="femme", variable=varGender, value=0)

radio1.pack()
radio2.pack()

varLabelGender = StringVar()

radioLabel = Label(app, textvariable=varLabelGender)
# varLabelGender.set(varGender.get())
radioLabel.pack()


app.mainloop()
