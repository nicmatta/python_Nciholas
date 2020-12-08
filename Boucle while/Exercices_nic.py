# Programmer par:Nicholas Matta 
# projet sommatif:interactif à la console
# crée le 3 décembre 2020 
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
# je fait un code qui depandand du choix fait vas exucuter un action 
choix=input()
if choix=='A':
    print("Exellent le météor était détruit")
elif choix=='B':
     print("Le météor a frapper ton nouveaux voiture ")
else:
    print('commande pas compris faire certaine que a et b sont majuscule')
print("")
print("")
print("Le premier ministre du Canada te offre du alchool")
print("")
print("Est-ce A tu accept, B did non merci, ou C déclare la guerre")
print("")
choix=input()
if choix=='A':
    print("Tu devien malade est vomir sur le premier ministre. Fâcher il déclare guerre")
elif choix=='B':
    print("Le premier ministre sen insulté est déclare guerre")
elif choix=='C':
    print("tu déclare guerre est tu giflé premier ministre")
else:
    print("commande pas compris faire certane que tu choisie une des opision A,b,ou C")
print("")
print("")
print("President",name,"les canadiens veux arreter la guerre est retourner des ami")
print("")
print("Est-ce que tu A accepte ou B laucher des missile nucléaire")
print("")
choix=input()
if choix=='A':
    print("Le gurre arrêté est tout mond commence a chanter est dancer dans les rue")
elif choix=='B':
    print("Les missile détruit le Canada est le meilleur équipe de hockey les Sénateur sont tuer")
print("")
print("")
#je donne le variable 'popularité' un valeur 
popularité=70
print("président",name,"le guerre a causer que l'économie descendre est ta popularité est just 70% si ca descend de moin que 50% tu sera plue président. Ont a just deux options A de élever les taxes ou B emprunter du argen des bank. Quel plan veux tu faire?")
choix=input()
if choix=='A':
  print("président",name,"les citoyen so frustrer des taxe est ton popularité a descendu à ",popularité-30,"qui est trop petit pour étre président tu était assassiné par la population est mouru aux hopitale :(")
elif choix=='B':
  print("président",name,"les citoyen sont tellement conton que tu a relver le économie qui a causer que ton popularité a augementer a",popularité+30,"qui fait que tu vas rester presiden pour tout ta vie :)")
print("")
print("game over")
print('programer par Nicholas Matta')