#coding:utf-8

"""
gestion des erreurs
"""

age = input("entrez votre age: ")
try:
    age = int(age)
    assert age >= 18
except AssertionError:
    print("vous devez avoir au moins 18 ans")
except ValueError:
    print("Vous devez entrer un nombre")
else:
    print("Vous avez", age, "ans. Bienvenue!")
