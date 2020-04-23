# coding:utf-8
"""
  PYTHON

  Synchro
    Gestion du temps
"""

from time import *
# afficher des textes successivement
print("premier texte")
sleep(0.5)
print ("texte suivant")

# affichage du temps écoulé
print(f"Temps écoulé en secondes depuis le début de l'ère informatique: {int(time())} secondes.")

"""
#estimer un intervalle entre deux opérations:
begin = time()
print("debut")
sleep(2)
end = time()
print("fin")

print("Intervalle écoulé entre début et fin:")
sleep(1)
print(f"{int(end - begin)} seconde.s")
"""

# print(time())
# print(localtime())


# tps = localtime()
# print(tps)
# print(mktime(tps))

myTime = strftime("%d/%m/%Y, %I:%M %P (s%V) - in %Z")
print(f"Aujourd'hui: {myTime}")