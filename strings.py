# coding:utf-8
"""
  PYTHON

  Chaines de caracteres
"""

# help (str)

maChaine = "bonjour tOut le monde!"
# maChaineCap = maChaine

# mettre en majuscules / minuscules / capitalizer 1ere lettre de la chaine / de chaque mot
maChaineCap = maChaine.capitalize()
maChaineMaj = maChaine.upper()
maChaineMin = maChaine.lower()
maChaineTitre = maChaine.title()
# print(len(maChaine))

# centrage d'une chaine
maChaineCentree = maChaineCap.center(len(maChaine) + 2, )
maChaineCentree2 = maChaineCentree.center(len(maChaine) + 10, "-")
# print(maChaineCap[0])

# recherche de position d'un terme dans une chaine
mot = "nuit"
print('Mot: "{}"'.format(mot))
positionMot = maChaineCap.find(mot)
# if positionMot < 0:
#   print('"{}" ne figure pas dans "{}"'.format(mot, maChaineCap))
# else:
#   print('Position de "{}": {}'.format(mot, positionMot))
# print(maChaineCap.index("soir"))
try:
  # print(maChaineCap.find("soir" ))
  assert positionMot >= 0
  print('Position de "{}": {}'.format(mot, positionMot))
  # print(maChaineCap.index(mot))
except ValueError:
  print('Mot "{}" non trouvé :-('.format(mot))
except AssertionError:
  print('Mot "{}" non trouvé :-('.format(mot))

# enlever des espaces
chaineEntiere = maChaineCap.center(len(maChaineCap) + 10)
chaineTronquee = chaineEntiere.strip()
# print(chaineEntiere)
print(chaineTronquee)

# remplacer un terme dans une chaine
maChaineModifiee = maChaineCap.replace('ou', 'u', 2)
print(maChaineModifiee)
# help(str)

# transformer une chaine en liste en utilisant un caracere comme repere
maListe = maChaineTitre.split(" ")
# afficher chaque element de la liste
for mot in maListe:
  print(mot)
