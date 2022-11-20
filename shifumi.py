from random import *

def choix_utilisateur():
    print("écris ton choix parmi ceux la")
    joueur = input("Pierre\nfeuille\nCiseaux\n")
    while joueur not in ["pierre", "feuille", "ciseaux"]:
        print("choisissez un de ces 3 mots en le copiant")
        joueur = input("pierre\nfeuille\nciseaux\n")
    return (joueur)


def choix_ordinateur():
    n = randint(1, 3)
    if n == 1:
        ordi = "pierre"
    elif n == 2:
        ordi = "feuille"
    else:
        ordi = "ciseaux"
    return (ordi)


a = choix_utilisateur()
b = choix_ordinateur()
print(b)
if a == "pierre" and b == "ciseaux":
    print("Vous avez gagne.")
elif a == "pierre" and b == "feuille":
    print("Vous avez perdu.")
elif a == "pierre" and b == "pierre":
    print("Egalite.")

if a == "feuille" and b == "pierre":
    print("Vous avez gagne.")
elif a == "feuille" and b == "ciseaux":
    print("Vous avez perdu.")
elif a == "feuille" and b == "feuille":
    print("Egalite.")

if a == "ciseaux" and b == "feuille":
    print("Vous avez gagne.")
elif a == "ciseaux" and b == "pierre":
    print("Vous avez perdu.")
elif a == "ciseaux" and b == "ciseaux":
    print("Egalite.")