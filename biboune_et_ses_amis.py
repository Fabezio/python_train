#coding:utf-8

# Présentation de la joyeuse bande de Biboune, adorable oursonne en peluche

class Peluche:
    present = 0
    def __init__(self, sonNom, sonEspece, sonGenre, sonAlimentation="omnivore"):
        self.nom = sonNom
        self.espece = sonEspece
        self.gender = sonGenre
        self.alimentation = sonAlimentation
        Peluche.present += 1
        print("{} est un {}, de genre {} et est {} ".format(sonNom, sonEspece, sonGenre, sonAlimentation))

Biboune = Peluche("Biboune", "ours", "fille")
Bibou = Peluche("Bibou", "ours", "garçon")
Lili = Peluche("Lili", "humain", "fille")
Roussin = Peluche("Roussin", "requin", "garçon", "végétarien")
Leonie = Peluche("Léonie", "lion", "fille")
Leonidas = Peluche("Léonidas", "lion", "garçon")
Timber = Peluche("Timber", "chien", "garçon")
Bill = Peluche("Bill", "ours", "garçon")
Amber = Peluche("Amber", "Lapin", "fille")
Nathan = Peluche("Nathan", "chien", "garçon")
print(Peluche.present)

        