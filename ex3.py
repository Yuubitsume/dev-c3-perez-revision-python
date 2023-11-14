import re

#demande à l'utilisateur le calcul souhaité
expression = input("Entrez une expression mathématique (ex: 2*6-4*4) : ")

#permet de séparer le calcul sur les différents opérateurs avec du regex
termes = re.split(r'(\+|\-|\*|\/)', expression)

#permet de séparer le chiffre 1 puis l'opération puis le chiffre 2
nombre1 = float(termes[0])
nombre2 = float(termes[2])
operateur = termes[1]

#On fais des conditions sur tous les opérateurs possible sur une calculatrice basique
if operateur == '+':
    resultat = nombre1 + nombre2
elif operateur == '-':
    resultat = nombre1 - nombre2
elif operateur == '*':
    resultat = nombre1 * nombre2
elif operateur == '/':
    if nombre1 != 0 and nombre2 != 0:  # Vérifier que ni le numérateur ni le dénominateur ne soient égales à zéro
        resultat = nombre1 / nombre2
    else:
        print("Division par zéro impossible")
        resultat = None

#Afficher le résultat si tous se passe bien
if resultat != None:
    print("Le résultat est", resultat)