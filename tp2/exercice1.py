n=0
i=0
n = int(input("Saisir votre poids"))
i = int(input("Saisir un taille en m"))

imc= n/i*i
print(imc)

if imc < 18.5:
    print(f"{imc} vous êtes dans la catégorie maigreur")
if  imc > 18.5:
    print(f"{imc} vous êtes dans la catégorie normal")
    if imc > 24.9:
        print(f"{imc} vous êtes dans la catégorie en sur poid")


