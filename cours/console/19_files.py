# coding:utf-8
"""
  PYTHON

  Fichiers
"""
with open("text.txt", "r") as fic:
  content = fic.read()
  # line = fic.readline()
  # print(line)
  # lines = fic.readlines()
  # print(content)
  # print(type(content) == str)
  # fic.close()
  # if not fic.closed:
  #   print("N'oublie pas de fermer le fichier!")

with open("empty.txt", "w") as fic:
  text = "hello world"
  print(text)
  fic.write(text)

with open("overwrite.txt", "w") as fic:
  # content = fic.read()
  print(content)
  newtext = "pour voir"
  fic.write(newtext)

with open("postscript.txt", "a") as fic:
  # content = fic.read()
  print(content)
  shift = "\n"
  newtext = "oops! on a un probleme de saut de ligne"
  print(newtext)
  fic.write(shift)
  fic.write(newtext)

# créons maintenant diverses fonctions destinées à l'intégration de texte dans un fichier
def writethis(content):
  with open("autre_texte.txt", "w") as fic:
    print(content)
    if type(content) != str:
      content = str(content)
    fic.write(content)
    fic.write("\n")

def overwritethis(content):
  with open("texte-sauvegardé.txt", "a") as fic:
    print(content)
    if type(content) != str:
      content = str(content)
    fic.write(content)
    fic.write("\n")

writethis(3)
writethis("Hello World!")
overwritethis("Je fais un essai")

# enregistrement dans un bichier binaire:
class Player:
  def __init__(self, name, level):
    self.name = name
    self.level = level

  def whoami(self):
    print("Joueur: {};\nNiveau: {}".format(self.name, self.level))

# p1 = Player("Fabezio", 5)
# p2 = Player("godkiller", 100)


import pickle
def exportData(filename, data):
  with open("{}.bin".format(filename), "wb") as fic:
    rec = pickle.Pickler(fic)
    rec.dump(data)
    print(data)

def importData(filename):
  try: 
    with open("{}.bin".format(filename), "rb") as fic:
      rec = pickle.Unpickler(fic)
      data = rec.load()
      data.whoami()
  except FileNotFoundError:
    print("Fichier non trouvé.")

    

importData("player-one")
# p1.whoami()
"""
"""

importData("playerTwo")
