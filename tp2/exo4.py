"""""
t = [1, 2, 3, 4, 5]
a = t[0] + t[3]
b = t[-1]
c = t[3:]
a = a + t[-2]

abc=["A","B","C","D","E"]
print(abc[3])
#afficher les trois dernier nombre
print(abc[-3:])


liste = [1, 4, 1, 2, 1, 5, 3, 1, 12]
a = len(liste)
b = liste[0]
liste.append(0)
c = len(liste)
d = liste[-1]

print(a,b,c,d)
print (len(liste)) #longueur de la liste
print (liste)

liste.append(2)
liste.append(9)
liste.append(1)# ajoute 1 la liste
print (liste)

liste.insert(0,"toto") # ajoute toto en position 0
print (liste)

liste.extend([2, 9, 1]) # ajoute plusieurs élément
print (liste)

liste.remove(1) #enlever le premier 1
print (liste)


while liste.count(1) > 0 : # enlever tous les 1
  liste.remove(1)
print (liste)

liste = [1, 4, 1, 2, 1, 5, 3, 1, 12]

while liste.count(1) > 0:
  liste.remove(1)

print(liste)

liste.sort() #ranger dans l'odre

print(liste)


print("Maximum ", liste[0], "Minimum ", liste[len(liste)-1])
print("Minimum ", min(liste), "Maximum ", max(liste))

print("Somme", sum(liste)) #somme

"""
#moyenne de classe
grades = [8, 12, 15, 6, 10, 19, 18, 7, 13, 15, 8, 15, 17, 13, 12, 15, 16, 9, 10, 3, 19, 20, 15]
print(grades)
grades.sort()
print(grades)

print("Minimum ", min(grades), "Maximum ", max(grades))
ecart= max(grades)/min(grades)
print(ecart) #afficher l'écart

#Afficher le nombre d'élèvres :
print (len(grades))

#Rajouter cette note à la liste des notes:
grades.insert(12,14)
print(grades)

#Modifier sa note:
grades.remove(8)
grades.insert(4,13)
print(grades)

moyenne = sum(grades)/(len(grades))
print (moyenne)