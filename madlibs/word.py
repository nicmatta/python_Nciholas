
phrases = []
consignes = []

# changer seulement les lignes dans mon_mad_lib ci-dessous
# --> supprimer les phrases.append et consignes.append
# --> ajouter vos propres phrases et consignes
#
# NE CHANGER RIEN D'AUTRE DANS LE PROGRAMME
#
# Si tout le monde fais ça, je vais pouvoir intégrer le
# travail dans un "livre" de mad libs que vous pourrez
# jouer avec votre famille pendant le temps des fêtes
#

def mon_mad_lib():
    """Préparer les phrases à trou""" 

    # le trou dans la phrase est indiqué par les {}
    phrases.append("Aujourd'hui nous allons au restarant {} .")
    consignes.append("nom propre")
    phrases.append(" car on c'est mon {} aujourdh'hui.")
    consignes.append("un célébration")
    phrases.append(" Le president ma donner 50$ pour manger des {}.")
    consignes.append(" nom propre ")
    phrases.append(" mais le {} a manger mon argen ")
    consignes.append("nom comun")
    phrases.append(" Aprée {} on quit le restarant ")
    consignes.append("temp")
    phrases.append("quand soudainement un {} nous attacke")
    consignes.append(" nom comun")
    phrases.append("Avec le aide de {} on le/la arréte")
    consignes.append("superhéro")
    phrases.append("pour célébré tout mond comence a {}")
    consignes.append("verbe")



mon_mad_lib()

# Obtenir les réponses de l'utilisateur
mots = []
# on demande un mot pour chaque consigne, utilisant la boucle 'for each'
for c in consignes:
    # ici le print utilise la méthode .format() qui remplace chaque {}
    # dans le texte avec la valeur dans le .format()
    print("Taper un mot qui est un(e) {}".format(c))
    mots.append(input())


# Afficher le résultat
print("Quand tu est prêt(e) pour le résultat, tape Enter")
input() # attend

for i in range(len(phrases)):
    # les trous {} dans les phrases sont remplacés par les mots.
    print(phrases[i].format(mots[i]))

print("\nMerci d'avoir joué!")
  