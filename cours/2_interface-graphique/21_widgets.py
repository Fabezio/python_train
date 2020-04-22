# coding:utf-8
"""
  PYTHON

  WIDGETS (basic)
"""

import tkinter as tk

app = tk.Tk()

"""
# configuration de la boîte de dialogue
"""
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()
thisWidth = screenWidth
thisHeigth = screenHeight
minWidth = screenWidth // 3
minHeight = screenHeight // 3
posX = (screenWidth - minWidth)//2
posY = (screenHeight - minHeight) // 2
inputWidth = minWidth // 16

app.minsize(minWidth, minHeight)
# app.maxsize(1600, 900)
app.resizable(width=True, height=True)
# app.positionfrom("user")
# app.sizefrom("user")
app.geometry("{}x{}+{}+{}".format(minWidth, minHeight, posX, posY))

"""
# Barre de titres
"""
app.title("fenêtre")

"""
# Fenêtre
"""
# Titre
label = "Bienvenue dans ce widget!"
labelWelcome = tk.Label(app, text=label)
labelWelcome.pack()

# Intro
# newLabel = "Voici un paragraphe"
# MessageText = tk.Message(app, text=newLabel, width=60)
# MessageText.pack()

# input
entryName = tk.Entry(app, width=inputWidth)
entryName.pack()

# input avec entrée masquée
entryPW = tk.Entry(app, width=inputWidth, show="*")
entryPW.pack()

# Bouton de validation


def hello():
    print("Bravo, vous avez cliqué sur le bouton et ça s'affiche ici!")


submitButton = tk.Button(
    app, text="Envoyer", width=inputWidth-3, height=2, command=hello)
submitButton.pack()

# labelWelcome.config(text=newLabel)
# labelWelcome["text"] = label

# print(labelWelcome.cget("text"))


app.mainloop()
