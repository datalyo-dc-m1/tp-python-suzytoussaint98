n = 0
i = 0
somme = 0

n = int(input("Saisir un entier"))
print  ("Boucle Pour ")
for i in range(1, 2*n, 2):  # pour i allant de 1 à 5 par pas de 2
    print(f"--> i vaut: {i}")  # je repète l'action 2 fois

somme = (i + i)
print (somme)