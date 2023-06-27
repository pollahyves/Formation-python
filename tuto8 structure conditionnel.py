"""
operateur de comparaison : 
==
<
>
<=
>=
!=

condition multiple

and (et)
or (ou)
in (dans)
not in (pas dans)
"""
"""
operateur de comparaison : 
==
<
>
<=
>=
!=

condition multiple

and (et)
or (ou)
in (dans)
not in (pas dans)

si (condition)
instruction

sinon si(condition)
instruction

sinon

"""

nom="yves"
password = "237yves"

name = input("entrer votre nom ")
motDePass = input("entrer votre mot de pass ")

if name == nom and motDePass == password:
    print("Connexion reussi Bienvenu "+name)
    print("je suis plus dans le if")

lettre = input("entrer une lettre: ")

if lettre in "aeiou":
    print("je suis une voyel")
elif lettre in "bfcdghjklmnopqrstz":
    print("je suis une consonne")  
else:
    print("cest pas un alphabet")      



