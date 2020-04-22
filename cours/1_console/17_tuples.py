# coding:utf-8
"""
  PYTHON

  Tuples
"""

import copy
monTuple = (1, "objet")
print(monTuple)

# exemple d'assignation multiple
nb1, nb2 = 1, 2
print(nb1, nb2)
# l'assignation de tuple peut se faire decette façon:
(nb1, nb2) = (1, 2)
print((nb1, nb2))
# :-| l'assignation de tuple implique  de ne JAMAIS en ajouter ou modifier le contenu
# nb1, nb2 = 3, 4
myTuple = (nb1, nb2)
nb2 = nb1
print(myTuple)

# en revanche on peut tupler dans une fonction
def getGlayerCoords(x,y):
  (x, y) = (920, 460)
  return (x, y)
(posX, posY) = (0, 0)
print((posX, posY))
# appliquons le contenu de ce tuple à la fonction:
print(getGlayerCoords(posX, posY))
#Et voilà!

# Alors, à quoi sert un tuple si son contenu est immuable? Simple: un affichage de valeurs définitives, comme par exemple dans un formulaire.
