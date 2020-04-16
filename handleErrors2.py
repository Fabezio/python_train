#coding:utf-8

""" 
Gestion des erreurs
# exemple d'une entree erronee
age = input("Quel âge as-tu? ")
try:
    age = int(age)
except:
    print(":( L'entrée n'est pas un nombre !")
else:
    print("Tu as donc {} ans.".format(age))
finally:
    print("PROGRAMME TERMINE")

# erreurs de types multiples

nb1 = 100
nb2 = input("Choisis un nombre pour diviser: ")
try:
    nb2 = int(nb2)
    res = nb1 / nb2
except ZeroDivisionError:
    print("division par 0 impossible")
except ValueError:
    print("Vous devez entrer un nombre")
except:
    print("Erreur inconnue.")
else:
    print("{}/{}={}; reste {}".format(nb1, nb2, nb1 // nb2, nb1 % nb2)) 
    # print("bravo!")
finally:
    print("terminé!")
"""

# exemple d'une entree erronee
age = input("Quel âge as-tu? ")
try:
    age = int(age)
except:
    print(":( L'entrée n'est pas un nombre !")
else:
    print("Tu as donc {} ans.".format(age))
finally:
    print("PROGRAMME TERMINE")
