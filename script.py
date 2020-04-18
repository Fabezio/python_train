# coding:utf-8
"""
  PYTHON

  Listes
"""
phrase = "Bonjour tout le monde!"
items = "    tunique    gants    arc    carquois    fleches"
items.strip(" ")
inv = items.split(" ")
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
print("Nombre d'arcs: ", inv.count('arc'))
# del inv
# print(inv)
# try:
#   print(inv)
# except NameError:
#   print("pas d'inventaire")

items = " ".join(inv)
print(items)
