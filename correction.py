
# 1. Hello World :
print("Hello, World!")


# 2. Manipulation de chaînes :
phrase = input("Entrez une phrase : ")
print("En majuscules :", phrase.upper())
print("En minuscules :", phrase.lower())
print("Nombre de mots :", len(phrase.split()))


# 3. Calculatrice simple :
expression = input("Entrez une expression mathématique : ")
resultat = eval(expression)
print("Résultat de l'expression :", resultat)


# 4. Listes :
liste_nombres = [2, 8, 3, 1, 7, 5, 10, 4, 6, 9]

# Maximum
maximum = max(liste_nombres)
print("Maximum :", maximum)

# Minimum
minimum = min(liste_nombres)
print("Minimum :", minimum)

# Moyenne
moyenne = sum(liste_nombres) / len(liste_nombres)
print("Moyenne :", moyenne)


# 5. Fonctions :
def factoriel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factoriel(n - 1)

nombre = int(input("Entrez un nombre pour calculer son factoriel : "))
print("Factoriel de", nombre, ":", factoriel(nombre))


# 6. Modules :
from datetime import datetime

maintenant = datetime.now()
print("Date et heure actuelles :", maintenant)


# 7. Fichiers :
# Lecture du fichier texte
with open('fichier.txt', 'r') as fichier:
    contenu = fichier.read()
    nombre_mots = len(contenu.split())

# Écriture du résultat dans un autre fichier
with open('resultat.txt', 'w') as resultat_fichier:
    resultat_fichier.write(f"Nombre de mots dans le fichier : {nombre_mots}")


# 8. Dictionnaires :
notes_eleves = {"Alice": 90, "Bob": 85, "Charlie": 95, "David": 88, "Eva": 92}

meilleur_eleve = max(notes_eleves, key=notes_eleves.get)
print(f"Meilleur élève : {meilleur_eleve} avec la note {notes_eleves[meilleur_eleve]}")


# 9. Compréhension de liste :
liste_carres = [x**2 for x in range(1, 11)]
print("Liste des carrés :", liste_carres)


# 10. Tri par insertion :
def tri_insertion(liste):
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i - 1
        while j >= 0 and cle < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = cle

# Exemple d'utilisation
liste_numbers = [12, 4, 5, 6, 7, 3, 1, 15, 14, 2]
tri_insertion(liste_numbers)
print("Liste triée par insertion :", liste_numbers)


