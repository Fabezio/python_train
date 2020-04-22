# coding:utf-8
"""
  PYTHON

  Widgets avancés
"""

import tkinter as tk
# module pour le modal:
from tkinter import messagebox

app = tk.Tk()

"""
# configuration de la boîte de dialogue
"""
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()
thisWidth = screenWidth
thisHeigth = screenHeight
minWidth = screenWidth // 3
minHeight = screenHeight // 9 * 10
posX = (screenWidth - minWidth)//2
posY = (screenHeight - minHeight) // 2
inputWidth = minWidth // 16

# app.minsize(minWidth)
# app.maxsize(1600, 900)
app.resizable(width=True, height=True)
# app.positionfrom("user")
# app.sizefrom("user")
app.geometry("{}x{}+{}+{}".format(minWidth, minHeight, posX, posY))

"""
# Barre de titres
"""
app.title("boîtes de dialogue")

"""
# Fenêtre
"""
# Titre
label = "modals"
labelWelcome = tk.Label(app, text=label)
labelWelcome.pack()

# Intro
# newLabel = "Voici un paragraphe"
# MessageText = tk.Message(app, text=newLabel, width=60)
# MessageText.pack()

# input
# entryName = tk.Entry(app, width=inputWidth, text="entre un texte")
# entryName.pack()

# input avec entrée masquée
# entryPW = tk.Entry(app, width=inputWidth, show="*", text="entre ton mdp")
# entryPW.pack()

# case à cocher
# checkbox = tk.Checkbutton(app, text="T'es d'accord? Sinon tant pis!")
# checkbox.pack()

# options uniques (radio)
# radioYes = tk.Radiobutton(app, text="oui", value=1)
# radioYes.pack()
# radioNo = tk.Radiobutton(app, text="non", value=0)
# radioNo.pack()

# curseurs
# scaleW = tk.Scale(app, from_=10, to=25, tickinterval=5)
# scaleW.pack()

# champ numéral
# spin = tk.Spinbox(app, from_="1", to="12")
# spin.pack()

# champ mutliple
# listbox = tk.Listbox(app, height=3)
# listbox.insert(1, "windows")
# listbox.insert(2, "linux")
# listbox.insert(3, "macOS/BSD")
# listbox.insert(4, "unix BSD")
# listbox.pack()

"""
# modals
"""
# message d'erreur


def showModalWindow():
    messagebox.showerror("ERREUR", "Un problème est survenu...")


errorBtn = tk.Button(app, text="Déclencher une erreur",
                     command=showModalWindow)
errorBtn.pack()
# msgBx = messagebox.

# message d'information


def showInfo():
    messagebox.showinfo("information", "si t'es perdu demande au SAV")


infoBtn = tk.Button(app, text="J'ai besoin d'infos", command=showInfo)
infoBtn.pack()

# message d'avertissement


def showWarning():
    messagebox.showwarning("Attention!", "Fais gaffe où tu cliques, abruti!")


warnBtn = tk.Button(app, text="Tiens, c'est quoi, ça?", command=showWarning)
warnBtn.pack()

# demande de confirmation de commande


def askMe():
    messagebox.askquestion("demande de confirmation",
                           "Tu veux VRAIMENT faire ça ?")


askBtn = tk.Button(app, text="Je veux faire ça", command=askMe)
askBtn.pack()

# demande de confirmation d'annulation


def cancelMe():
    messagebox.askokcancel("Demande d'annulation",
                           "Annuler? (commande irréversible)")


cancelBtn = tk.Button(app, text="Annuler / Effacer", command=cancelMe)
cancelBtn.pack()

# Oui ou non


def yesOrNo():
    messagebox.askyesno("Oui ou Non",
                        "C'est oui ou c'est non?")


ynBtn = tk.Button(app, text="oui ou non", command=yesOrNo)
ynBtn.pack()

# réessayer


def retryAsk():
    messagebox.askretrycancel("oops...",
                              "ca n'a pas marché. voulez-vous réessayer?")


retryBtn = tk.Button(app, text="tentative", command=retryAsk)
retryBtn.pack()


# Bouton de validation
# def hello():
#     print("Bravo, vous avez cliqué sur le bouton et ça s'affiche ici!")


# submitButton = tk.Button(
#     app, text="Envoyer", width=inputWidth-3, height=2, command=hello)
# submitButton.pack()

# labelWelcome.config(text=newLabel)
# labelWelcome["text"] = label

# print(labelWelcome.cget("text"))


app.mainloop()
