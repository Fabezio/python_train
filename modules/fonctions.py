#coding:utf-8

""" 
fonctions 


saluer()

dire("moi", saluer())
# lister éléments
def list_items(*itemList):
  for item in itemList:
    print (item)

list_items("papa", "maman", "enfant")
print(additionner(1,2))

# test
if __name__ == "__fonctions__":
  print("test:\n\n", dire("Auteur", "Bonjour tout le monde! :)"))
else: print("oops")

"""

def additionner(a, b):
  return "a + b = {}".format(a + b)
def saluer():
  return("Bonjour tout le monde")

def dire(nom, message):
  return("{}: {}".format(nom, message))
