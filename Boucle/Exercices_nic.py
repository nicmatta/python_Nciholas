# Programmer par:Nicholas Matta 
# projet sommatif:interactif à la console
# crée le 9 décembre 2020 
# modifier le 6 décembre 2020
# adress couriel:matnic02@ecolecatholique.ca

#je commence avec demander le utilisateur des question avec 'print' 

print("Bonjour après une election fédérale tu est electer président du monde quel vas étre ton nom presidencial ?")
#je donne le choix a l'utilisateur de choisir le nom en utilisan le comand 'input'
name=input()
print("")
print("Bon matin président",name,"le premier chose dans ton agenda est un situation qui développe dans l'espace un météor vas frapper le planet dans deux jour")
print("")
print("veux tu A laucher un explosive qui le détruit, ou B faire rien")
choix=input()
if choix=='A':
 print("")
 print("tu doit mttre cette code pour les laucher")
 for i in range(0,10):
  print(i)
if choix=='B':
  print("tout mond est mort")
choix=input()
if choix==("0123456789"):
    print("brovo")
else:
  print('pas compri faire certaine que nombre sont en order est coller')
  