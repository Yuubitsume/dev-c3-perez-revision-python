phrase = input("Entrez une phrase : ")

print("Phrase en majuscules :", phrase.upper())
print("Phrase en minuscules :", phrase.lower())

mots = phrase.split()  # Divise la phrase en une liste de mots
nombre_mots = len(mots)  # Compte le nombre d'éléments dans la liste

print("Nombre de mots dans la phrase :", nombre_mots)
