# coding:utf-8
"""
  PYTHON

  Widgets 
    Créer un menu
"""
from tkinter import *

# création du widget
app = Tk()
app.title("Positionnement")
app.geometry("800x450")

# widget
# fonctions


def hello():
    print("Hello User!")


def about():
    aboutWindow = Toplevel(app, height=100, width=160)
    aboutWindow.title("Présentation")
    aboutWindow.resizable(height=False, width=False)
    lb = Label(aboutWindow, text="Oui, c'est bien moi!")
    lb.pack()
    print("Fenetre 'a propos' ouverte")


mainmenu = Menu(app)
firstMenu = Menu(mainmenu, tearoff=0)
firstMenu.add_command(label="Option 1")
firstMenu.add_command(label="Option 2")
firstMenu.add_separator()
firstMenu.add_command(label="Quitter", command=app.quit)

secondMenu = Menu(mainmenu, tearoff=0)
secondMenu.add_command(label="Saluer", command=hello)
secondMenu.add_command(label="Commande 2")
secondMenu.add_command(label="A propos", command=about)

mainmenu.add_cascade(label="Options", menu=firstMenu)
mainmenu.add_cascade(label="Commandes", menu=secondMenu)

# mainmenu.pack()


# Boucle (affichage permanent)
app.config(menu=mainmenu)
app.mainloop()
