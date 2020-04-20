from random import randint

nbr = randint(1,10)
print(nbr)

user_propal = int(input("Saisir un entier entre 0 et 10 :"))
if user_propal > 10:
    print(f"{user_propal} est pas entre 0 et 10")

if nbr != user_propal :
    print ('ce nest pas bon')

elif user_propal > nbr :
    print("ton chiffre est plus grand")

else:
    print ('gagné')