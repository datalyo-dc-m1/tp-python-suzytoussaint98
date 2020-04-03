somme = 0

n = int(input("Saisir un entier"))
print  ("Boucle Pour ")
for i in range(1, 2*n, 2):
    print (i)
    print(f"Entier: {i}")
    somme += i
    print(f"--> somme vaut: {somme}")  # je repète l'action 2 fois

print (somme)


