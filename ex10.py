def tri_insertion(liste):
    for i in range(0, len(liste)):
        cle = liste[i]  # Élément à insérer dans la liste triée
        j = i - 1  # Commencer la comparaison avec l'élément précédent

        #Déplacer l'élément à gauche à sa droite jusqu'à ce qu'il soit inférieur à celui à sa gauche
        while j >= 0 and cle < liste[j]:
            liste[j + 1] = liste[j] #Décale le nombre vers la droite
            j -= 1 #incrémente j-1 pour la condition

        liste[j + 1] = cle  # Insérer la clé dans la position correcte
    
    return liste

liste_numbers = [12, 45, 78, 23, 56, 89, 43, 46, 84, 21]
print("Liste non triée :", liste_numbers)
print("Liste triée :", tri_insertion(liste_numbers))
