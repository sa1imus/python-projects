import random

leprix=random.randint (0,1000)

print("Bienvenue au juste prix")
n = int(input("Devinez un nombre entre 0 et 1000 : "))

while leprix != n:
    if leprix < n:
        print("Plus petit !")
        n = int(input("Proposez autre chose : "))

    elif leprix > n:
        print("Plus grand !")
        n = int(input("Proposez autre chose : "))
else:
    print("felicitation !!! vous avez trouver le bon numero.")

