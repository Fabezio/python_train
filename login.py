#coding:utf-8

id = ""
pw = ""

id_Input = "Entrez votre Identifiant: "
pw_Input = "Entrez votre Mot de passe: "

if id and pw:

  print("Interface de connexion")
  
  user_id = input(id_Input)
  user_pw = input(pw_Input)

  if user_pw == pw and user_id == id:
    print("Bonjour,", user_id)
  else:
    print('Le nom ou le mot de passe est incorrect')
else:
  sign_up = input("Données non répertoriées, voulez-vous vous inscrire? (O/N)")
  if sign_up == "O" or sign_up == "o":
    id = user_id 
    pw = user_pw
    print("Données enregistrées, merci de votre confiance.")
  
print("A bientôt")
      