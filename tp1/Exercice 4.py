n = 0
i = 0
n = int (input("Saisire entre 1 et 100 : "))
if n < 1 or n > 100 :

    print (n, "n'est pas entre 1 et 100")
else :
    print("Boucle Pour ")
    for i in range(1, 1 * n ):
        print(i)
