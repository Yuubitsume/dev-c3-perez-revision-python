# Lire le fichier texte input.txt
with open('C:/Users/Julien/Documents/Dev_pyth_atl/input.txt', 'r', encoding="utf-8") as fichier:
    contenu = fichier.read()
    print(contenu)

# Compte le nombre de mots
mots = contenu.split()
nombre_mots = len(mots)
print(nombre_mots)