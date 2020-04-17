#coding:utf-8

"""
PYTHON

Propriétés d'encapsulation
"""

class Humain:
    """
    Classe des êtres humains
    """

    population = 0
    lieuHabitation = "Terre"

    def __init__(self, nom, age):
        print("Creation d'un être humain...")
        self._nom = nom
        self._age = age
        Humain.population += 1
    def showPopulation(cls):
        word = "individus"
        if Humain.population <= 1:
            word = "individu"
        return "Il y a {} {}".format(Humain.population, word)
    showPopulation = classmethod(showPopulation)

    def _getNom(self):
        # print("Récupération prohibée")
        try: 
            return self._nom
        except AttributeError:
            return print("Nom effacé.")

    def _setNom(self, nouveauNom):
        if nouveauNom < 0:
            self._nom = 0
        else:
            self._nom = nouveauNom

    def _delNom(self):
        del self._nom

    nom = property(_getNom, _setNom, _delNom, "Je nomme la personne")

    def _getAge(self):
        # print("Récupération prohibée")
        try:
            word = ""
            if self._age <= 1:
                word = "an"
            else:
                word = "ans"
            return "{} {}".format(self._age, word)
        except AttributeError:
            return print("Age effacé.")

    def _setAge(self, nouvelAge):
        if nouvelAge < 0:
            self._age = 0
        else:
            self._age = nouvelAge

    def _delAge(self):
        del self._age

    age = property(_getAge, _setAge, _delAge, "Je représente l'âge de la personne")

# h1 = Humain("Dave", 31)
h2 = Humain("Fabezio", 47)
# h1.age = 1
# print("{} a {}".format(h1.nom, h1.age))
print("{} a {}".format(h2.nom, h2.age))
print(Humain.showPopulation())

