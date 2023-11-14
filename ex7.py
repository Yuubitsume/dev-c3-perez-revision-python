# Lire le fichier texte input.txt
with open('C:/Users/Julien/Documents/Dev_pyth_atl/input.txt', 'r', encoding="utf-8") as fichier:
    contenu = fichier.read()
    print(contenu)

# Compte le nombre de mots
mots = contenu.split()
nombre_mots = len(mots)

# Écrire le résultat dans un autre fichier output.txt
with open('C:/Users/Julien/Documents/Dev_pyth_atl/output.txt', 'w', encoding="utf-8") as file_output:
    file_output.write(f'Le nombre de mots dans le fichier est : {nombre_mots}')
