# coding:utf-8
"""
  PYTHON

  WIDGETS (basic)
"""

import tkinter as tk

app = tk.Tk()
app.title("fenêtre")
labelWelcome = tk.Label(app, text="Hello world!")


screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()
thisWidth = screenWidth
thisHeigth = screenHeight
minWidth = 800
minHeight = 450
posX = (screenWidth - minWidth)//2
posY= (screenHeight - minHeight)//2
app.minsize(minWidth, minHeight)
# app.maxsize(1600, 900)
app.resizable(width = False, height=True)
# app.positionfrom("user")
# app.sizefrom("user")
app.geometry("{}x{}+{}+{}".format(minWidth, minHeight, posX, posY))
app.mainloop()

 