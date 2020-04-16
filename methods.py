#coding:utf-8

"""
CLASSES

méthodes
"""

class Humain:
    """
    Classe des êtres humains
    """

    unIndividu = 0
    lieuHabitation = "Terre"
    def __init__(self, sonNom, sonAge):
        # print("Creation d'un être humain", self)
        self.nom = sonNom
        self.age = sonAge
        Humain.unIndividu += 1

    # Methodes:
    # - Methode standard ou d'instanciation

    def parler(self, sonMessage):
        print("{}: {}".format(self.nom, sonMessage))
        
    # - Methode de classe 
    def changerHabitation(cls, nouvelleHabitation):
        Humain.lieuHabitation = nouvelleHabitation

    changerHabitation = classmethod(changerHabitation)
        
    # - Methode statique
    def definition():
        print("L'être humain est reconnu comme étant l'animal le plus intelligent de la planète.")
    definition = staticmethod(definition)
    
print("Lancement du programme...\n")
Dave = Humain("David", 31)
print(Humain.unIndividu)
Dave.parler("Bonjour, tout le monde! Je m'appelle {} et j'ai {} ans.".format(Dave.nom, Dave.age))
Dave.parler("Au fait j'habite sur {}.".format(Humain.lieuHabitation))
print("\nQuelques temps plus tard...")
Dave.changerHabitation("Mars")
Dave.parler("J'ai déménagé, maintenant j'habite {}.".format(Humain.lieuHabitation))
Humain.definition()


# print("{} de sexe {}".format(Humain().name, Femme.sexe))

# class Continent:
#     continents = 0
#     def __init__(self, c_nom):
#         self.nom = c_nom
#         Continent.continents += 1

# Eurasie = Continent("Eurasie")
# Amerique = Continent("Amérique")
# Australie = Continent("Australie")
# Afrique = Continent("Afrique")
# Arctique = Continent("Arctique")
# Antarctique = Continent("Antarctique")
# print("Nombre de continents:", Continent.continents)

