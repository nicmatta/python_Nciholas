# Nicholas Matta exemple de utilisation de Imput Le 30 novembre 2020
score=100 
print('what is your name?')
name=input()
print("hi",name,"pick a color")
print('bleu ou rouge noir ou mystère?')
choix=input().lower()
if choix=='rouge':
  print(score + 50, 'point gangnant')
elif choix=='bleu':
  print(score-50, 'point perdant')
elif choix=='noir':
  print(score+1000000, 'point gangnant')
elif choix=='mystère':
  print(score*100, 'point gangnant')
print("Game over thank you for playing",name,)
print('Programmer par:Nicholas Matta')
