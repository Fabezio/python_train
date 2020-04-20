# coding:utf-8
"""
  PYTHON

  tkinter
"""

import tkinter as tk

mainapp = tk.Tk()
mainapp.title("fenêtre")
thisWidth = 1920
thisHeigth = 1050
minWidth = 800
minHeight = 450
screenWidth = mainapp.winfo_screenwidth()
screenHeight = mainapp.winfo_screenheight()
posX = (screenWidth - minWidth)//2
posY= (screenHeight - minHeight)//2
mainapp.minsize(minWidth, minHeight)
# mainapp.maxsize(1600, 900)
mainapp.resizable(width = False, height=True)
# mainapp.positionfrom("user")
# mainapp.sizefrom("user")
mainapp.geometry("{}x{}+{}+{}".format(minWidth, minHeight, posX, posY))
mainapp.mainloop()

 