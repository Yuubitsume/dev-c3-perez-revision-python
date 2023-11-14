# Création d'un dictionnaire avec des noms, prénoms et notes associées
notes_eleves = {
    'Alice Smith': 15,
    'Bob Johnson': 12,
    'Claire Williams': 17,
    'Claire Michel': 17,
    'David Brown': 14,
    'Emma Davis': 16
}


notes_max = 0
nom_notes_max = ''

for key, valeur in notes_eleves.items():
    if notes_max <= valeur:
        notes_max = valeur
        nom_notes_max = key
    
print(notes_eleves)
print(notes_max, nom_notes_max)
