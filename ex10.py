def tri_insertion(liste):
    # Parcours de la liste à partir du deuxième élément
    for i in range(0, len(liste)):
        cle = liste[i]  # Élément à insérer dans la liste triée
        j = i - 1  # Commencer la comparaison avec l'élément précédent

        #Déplacer les éléments de la liste triée qui sont plus grands que la clé
        while j >= 0 and cle < liste[j]:
            liste[j + 1] = liste[j]  #Décale le nombre vers la droite
            j -= 1

        liste[j + 1] = cle  # Insérer la clé dans la position correcte
    
    return liste

liste_numbers = [12, 45, 78, 23, 56, 89, 43, 46, 84, 21]
print("Liste non triée :", liste_numbers)
print("Liste triée :", tri_insertion(liste_numbers))
