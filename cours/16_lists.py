# coding:utf-8
"""
  PYTHON

  Listes
"""

import copy
phrase = "Bonjour tout le monde!"
# items = "    tunique    gants    arc    carquois    fleches"
# phrase.strip(" ")
inv = phrase.split(" ")
# inv.append('arc')
# print(inv[:])
# for el in inv:
#   # print(el)
#   if el == "":
#     del el
  

# print("Nombre d'éléments:", len(inv))
# inv.sort()
# inv.reverse()
# print(inv)
# print("Position de 'arc':", inv.index('arc'))
# print("Nombre d'arcs: ", inv.count('arc'))
# del inv
print(inv)
# try:
#   print(inv)
# except NameError:
#   print("pas d'inventaire")

# items = " ".join(inv)
# print(items)
"""
pour copier le contenu d'une liste:
NE JAMAIS FAIRE DE COPIE DIRECTE, SOUS PEINE D'ENTRAINER DES MODIFICATIONS SUR LES DEUX LISTES 
Apres avoir importe le module 'copy', il suffit d'utiliser ce dernier pour l'assigner à la liste cible.
Pour exemple, disons que je veux dupliquer "inv" en "invCopy". D'abord je vais renommer inv en invSave par sécurité:
"""
invSave = inv
invCopy = copy.deepcopy(inv)
# ci-dessus j'ai copié le CONTENU de la liste, tandis que invSave est une copie de inv. voyons la difference avec un ajout.
inv.append("Yeah!")
# affichons toutes les listes
print(inv[:])
print(invSave[:])
print(invCopy[:])

# seule invSave a été également modifiée. Ajoutons des élément à la copie et voyons ce qui se passe.
invCopy.append("C'est")
invCopy.append("cool")
invCopy.append("d'être")
invCopy.append("là!")
print(inv[:])
print(invSave[:])
print(invCopy)
# cette fois seule invCopy a été modifiée

