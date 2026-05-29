# On demande ton prénom
prenom = input("Comment tu t'appelles ? ")

# L'ordinateur te répond personnellement
print(f"Enchanté {prenom} ! On va faire un petit calcul ensemble.")

# On demande deux chiffres
chiffre1 = input("Donne-moi un premier chiffre : ")
chiffre2 = input("Donne-moi un deuxième chiffre : ")

# Python calcule le total (on transforme le texte en vrai nombre avec 'int')
total = int(chiffre1) + int(chiffre2)

# On affiche le résultat
print(f"Le résultat de {chiffre1} + {chiffre2} est égal à : {total} !")