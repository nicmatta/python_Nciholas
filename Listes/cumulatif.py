# Programer par: Nicholas Matta 
# Le date: le 17 déc 2020
# adress couriel: matnic02@ecolecatholique.ca 
print("Run or quit")
choix=input().lower()
christmas=True 

while christmas:
    
    liste = [1,5,10,15,20,25,30,35,40,45,50,55]
    if choix=="run":
        for i in liste:
            #print ("voici le list ")
            if i > 50:
                    print("sa c'est des bon de 5")
                    break
            print(i)
        print("")
        v = "Passer un joyeuse noël est bon nouvel année 2021"
        for lettre in v:
            print(lettre)
        print("")
        i = 0
        while i < 15:
            print("🎅 🤶 🎄 🎁 👼  ")
            i = i +1
            christmas=False
    elif choix=="quit":
        christmas=False 
        print("ok joyeux noël")
my_list = [] 
my_list.append(574) 
my_list.append('joyeuse,noel')
print(my_list) 
print(my_list[0]) 
print(my_list[0]) 
print(len(my_list)) 
for element in my_list:
    element *= 4
    print(element)
