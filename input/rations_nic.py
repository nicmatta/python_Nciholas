# Programmer par:Nicholas Matta 
# exemple de utilisation de Imput et elif
# Le 30 novembre 2020
#adress couriel:matnic02@ecolecatholique.ca
score=100 
print('Quel est votre nom?')
name=input()
print("Bonjour",name,"vous devrez choisir une porte et essayer de   rester au-dessus de 100 points bonne chance")
print('')
print('veuillez choisir une porte') 
print('1, 2, 3, ou mystère?')
choix=input().lower()
if choix=='1':
  print(score + 50, 'Bravo tu a rester au-dessus 100 point vous gagnes')
elif choix=='2':
  print(score-50, 'point tu perde')
elif choix=='3':
  print(score+1000000, 'Bravo tu a rester au-dessus 100 point vous gagnes')
elif choix=='mystère':
  print(score*100, 'Bravo tu a rester au-dessus 100 point vous gagnes')
print("Game over Merci d'avoir joué",name,)
print('Programmer par:Nicholas Matta')
