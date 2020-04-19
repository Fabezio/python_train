# coding:utf-8
"""
  PYTHON

  Dicos
"""

import copy

# myDict = {1: "papa", 2: "maman", 3: "enfant"}
EngFr = {"english" : "anglais", "french": "français"}
# ajouter une paire: 
EngFr["spanish"] = "espagnol"
# print("type de myDict:\n{}\n".format(type(myDict)))
print("Contenu du dictionnaire:\n{}\n".format(EngFr))
#maintenant,  pour afficher un élément, on l'appelle comme pour une liste, à ceci prés que la clé remplace l'indice:
"""print("English:", EngFr["english"])"""
# et à présent le contenu
"""
for word in EngFr:
  print(word + ":", EngFr[word])
"""
# faisons une fonction de ce dico en assignant la variable de dico comme paramètre...
def echoDict(myDict):
  for word in EngFr:
    print(word + ":", myDict[word])
# ...et appliquons-la
"""
echoDict(EngFr)
"""
#tiens, que veut dire "German"?
EngFr["german"] = "allemand"
# redemandons-lui!
echoDict(EngFr)
