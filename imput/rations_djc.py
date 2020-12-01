# Nicholas Matta exemple de utilisation de Imput Le 30 novembre 2020
print('bleu ou rouge noir ou mystère?')
choix=input()
if choix.lower()=='rouge':
  print('+50 point gangnant')
if choix.lower()=='bleu':
  print('-50 point perdant')
if choix.lower()=='noir':
  print('+1000000 point gangnant')
if choix.lower()=='mystère':
  print(1000*100)
print('Game over')
print('Programmer par:Nicholas Matta')