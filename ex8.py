notes_eleves = {
    'Alice Smith': 15,
    'Bob Johnson': 12,
    'Claire Williams': 17,
    'Claire Michel': 17,
    'Claire Alie': 17,
    'David Brown': 14,
    'Emma Davis': 16,
    'Frank Thomas': 15,
    'George Harris': 13,
    'Helen Taylor': 16,
    'Isabel Clark': 14,
    'Jackie Lee': 18,
    'Kate Turner': 17,
    'Liam Walker': 16,
    'Mia Garcia': 15,
    'Nathan Allen': 17,
    'Olivia Martinez': 18,
    'Wendy Green': 15,
    'Xavier Brooks': 16,
    'Yvonne Reed': 14,
    'Zoe Hall': 18
}


# Initialisation des variables pour stocker les informations sur la note maximale
max_note = 0
eleves_max_notes = []

# Parcourir le dictionnaire pour trouver la note maximale
for i, (eleve, note) in enumerate(notes_eleves.items()):
    if note > max_note:
        max_note = note
       