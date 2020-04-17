#coding:utf-8

"""
apprendre python

Classes héritées
"""


# classe mère
class Vehicule:
    def __init__(self, nom_vcl, carburant_vcl):
        self.nom = nom_vcl
        self.carburant = carburant_vcl

    def montrerVehicule(self):
        return self.nom
    def deplacement(self):
        return "Je me déplace..."

# classe fille
class Voiture(Vehicule):
    def __init__(self, nom_voit, carburant_voit, puissance, roues=4):
        Vehicule.__init__(self, nom_voit, carburant_voit)
        self.puissance = puissance
        self.roues = roues
    
    def deplacement(self):
        return "Je roule..."

class Avion(Vehicule):
    def __init__(self, nom, carburant, transport):
        Vehicule.__init__(self, nom, carburant)
        self.transport = transport

    def deplacement(self):
        return "Je vole!"

class Bateau(Vehicule):
    pass

# Classe à héritage multiple:
class Amphibie(Voiture, Bateau):
    pass

raptor = Avion("F22 Raptor", 2400, "Arsenal ")
print(raptor.nom)
print(str(raptor.carburant) + ' l')

v2 = Voiture("Toyota Yaris", 90, 40)
print(v2.nom)
print(str(v2.carburant) + ' l')

airbus = Avion("Airbus A380", 320000, "passagers")
print(airbus.deplacement())

# Vérification de l'objet (classe renseignée)
print(isinstance(airbus, Vehicule)) # Objet airbus est de la classe donnée 
print(issubclass(Bateau, Vehicule)) # première classe herite de la seconde


