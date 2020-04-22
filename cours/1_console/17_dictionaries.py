# coding:utf-8
"""
  PYTHON

  Dicos
"""

# import copy

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
  for (e, s) in EngFr.items():
    print("{}: {}".format(e.capitalize(), s.capitalize()))

# ...et appliquons-la
"""
echoDict(EngFr)
"""
#tiens, que veut dire "German"?
EngFr["german"] = "allemand"

# redemandons-lui!
# echoDict(EngFr)
# print('\n')
# print(EngFr.in("greman"))

# Copions le contenu de EngFr
EngToFrench = EngFr.copy()
# ajoutons une entrée dans la copie et apppelons le deux dicos
EngFr["italian"] = "italien"
echoDict(EngFr)
print('\n')
echoDict(EngToFrench)

# creation de dico avec des parametres nommés
def creerDico(**params):
  print(params)

creerDico(nom="ami", verbe="être")