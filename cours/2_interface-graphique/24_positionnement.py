# coding:utf-8
"""
  PYTHON

  Widgets 
    Positionnements
"""
from tkinter import *

# création du widget
app = Tk()
app.title("Positionnement")
app.geometry("800x450")

# widget

# cadre
bg = "cyan"
mainframe = Frame(
    app,
    width=640,
    height=360,
    relief="solid",
    bd=1,
    bg=bg
)
label = Label(app, text="Bienvenue!")
parag = Label(mainframe, text="texte", bg=bg)
insbtn = Button(mainframe, text="bouton")
btn = Button(app, text="Clique ici")
brand = Label(app, text="Positionnnement")
brand.place(x=10, y=10)
label.pack(side="top")
mainframe.pack(pady=16)
btn.pack(fill="x", padx=100, ipady=32)

parag.grid(row=0, column=0, padx=10)
insbtn.grid(row=0, column=1)

app.mainloop()
