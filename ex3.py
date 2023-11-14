import re

#demande à l'utilisateur le calcul souhaité
expression = input("Entrez une expression mathématique (ex: 3+1-4*4) : ")

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
    resultat = nombre1 / nombre2
    
print("Le résultat est : ", resultat)