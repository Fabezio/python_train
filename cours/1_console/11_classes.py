#coding:utf-8

"""
POO

classes
"""

# class Humain:
#     """
#     Classe des êtres humains
#     """
#     def __init__(self, c_type, c_sex):
#         # print("Creation d'un être humain", self)
#         self.name = "humain"
#         self.diet = "omnivore"
#         self.specy = "hominidés"
#         self.family = "mammifère"
#         self.geno = "vivipare"
#         self.intelligence = "intuitive"
#         self.type = c_type
#         self.sex = c_sex

# print("Lancement du programme...")

# Homme = Humain("Homme", "mâle")
# print("{}: être {} {}".format(Homme.type, Homme.name, Homme.sex))

# Femme = Humain("Femme", "femelle")
# print("{}: être {} {}".format(Femme.type, Femme.name, Femme.sex))
# # print("{} de sexe {}".format(Humain().name, Femme.sexe))

class Continent:
	continents = 0
	def __init__(self, c_nom):
		self.nom = c_nom
		Continent.continents += 1

Eurasie = Continent("Eurasie")
Amerique = Continent("Amérique")
Australie = Continent("Australie")
Afrique = Continent("Afrique")
Arctique = Continent("Arctique")
Antarctique = Continent("Antarctique")
print("Nombre de continents:", Continent.continents)

