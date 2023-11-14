import random

random_valeur = random.randint(1, 15)
liste_nombres_carres = [random.randint(1, 100) ** 2 for i in range(random_valeur)]

print(liste_nombres_carres)
