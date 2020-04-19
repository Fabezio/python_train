# coding:utf-8
"""
  PYTHON

  Fichiers
"""
fic = open("textes/text.txt", "r")
content = fic.read()
line = fic.readline()
print(line)
lines = fic.readlines()
print(content)
# print(type(content) == str)
fic.close()
if not fic.closed:
  print("N'oublie pas de fermer le fichier!")