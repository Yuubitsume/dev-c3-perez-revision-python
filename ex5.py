valeur = input("entrez un nombre ")
resultat = 1

# int(valeur) pour forcer le typage et que le user ne puisse pas mettre de flottant mais aussi et surtout
# pour utiliser la valeur du input dans la boucle
for i in range(1, int(valeur) + 1):
    resultat *= i #le factoriel correspond de 4 par exemple, correspond à 4 * 3 * 2 * 1 = 24
    
print(resultat)