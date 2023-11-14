import random

#permet de générer une liste de taille aléatoire entre 1 et 15 compris
random_valeur = random.randint(1,15)
#ajout de cette random dans la liste, génère donc entre 1 et 15 valeurs comprise entre 1 et 1000
liste_nombre = [random.randint(1,1000) for i in range(random_valeur)]

max = max(liste_nombre)
min = min(liste_nombre)

moy = sum(liste_nombre) / random_valeur

print(liste_nombre)
print("La valeur maximale est :", max)
print("La valeur minimale est :", min)
print("La moyenne de la liste est de :", moy)