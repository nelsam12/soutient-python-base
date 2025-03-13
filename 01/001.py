# Affichage d'un texte  : print(texte_a_afficher)
# print("Hello World !")
# Affichage d'un nombre : print(nombre_a_afficher)
# print(42)
# Affichage d'une variable : print(variable_a_afficher)
# a = 42 # Variable : Un carton dans lequel on met une chose
# print(a)
# Les types de variables : int, float, str, bool
# a = 42 # int - <class 'int'>
# b = 42.0 # float
# c = "42" # str
# d = True # bool (True = 1, False = 0)
# print(type(d))
# print(0 == False)

# Exercice 1
# Afficher "Hello World !" en utilisant une variable
# texte = "Hello World !"
# print(texte)

# Saisie de l'utilisateur : input("Texte à afficher")
# saisir ou lire ===> input("Texte à afficher")
# input = saisir + écrire(afficher) / saisir ou lire

# Exercice 2
# Demander à l'utilisateur son nom et son prénom
# Afficher le nom et le prénom de l'utilisateur

# __ approche 1 __
# nom = input("Entrez votre nom : ")
# prenom = input("Entrez votre prénom : ")
# print("Nom :", nom)
# print("Prénom :", prenom)

# __ approche 2 __ (universelle)
# print("Entrez votre nom : ") # Ecrire ("Entrez votre nom : ")
# nom = input() # Lire (nom) { déclaration et initialisation de la variable nom }
# print("Entrez votre prénom : ") # Ecrire ("Entrez votre prénom : ")
# prenom = input() # Lire (prenom) { déclaration et initialisation de la variable prenom }
# print("Nom :", nom) # Ecrire ("Nom :", nom)
# print("Prénom :", prenom) # Ecrire ("Prénom :", prenom)


# Exercice 3
# Demander à l'utilisateur son âge
# Afficher l'âge de l'utilisateur
# age = input("Entrez votre âge : ")
# print("Vous avez ", age, "ans")


# Exercice 4 !!!!!!! à revoir !!!!!!!
# Demander à l'utilisateur son âge
# Afficher l'age que le personne aura dans 10 ans
# age = input("Entrez votre âge : ")
# input renvoie une chaine de caractère (str)
# print(type(age))
# print("Vous avez ", age, "ans")
# pour convertir une chaine de caractère en entier => int(chaine_de_caractère)
# age = int(age) # Base 10 { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
# print(type(age))
# age_dans_10_ans = age + 10
# print("Dans 10 ans, vous aurez ", age_dans_10_ans, "ans")


# Condition : if, elif, else
# syntaxe:
    # if condition:
    #     instruction
    # elif condition:
    #     instruction
    # else:
    #     instruction
# Exercice 5
"""
Vous êtes gérant d'une boite de nuit, on vous demande de mettre en place
un algorithme qui permet de vérifier si une personne peut entrer dans votre boite de nuit
ou non. Pour entrer dans votre boite de nuit, il faut avoir au moins 18 ans.
Demander à l'utilisateur son âge, si l'utilisateur a au moins 18 ans, afficher
"Vous pouvez entrer dans la boite de nuit", 
sinon afficher 
"Vous ne pouvez pas entrer dans la boite de nuit"
"""
# age = int(input("Veuillez entrer votre âge : "))
# if age >= 18:
#     print("Vous pouvez entrer dans la boite de nuit")
# else:
#     print("Vous ne pouvez pas entrer dans la boite de nuit")


# Exercice 6 (if elif else)
"""
Ecrire un programme qui prend en entrée les notes (3 notes) d'un étudiant,
le programme affiche la mention (Echoué(e), Passable, Assez bien , Bien ou Très bien) 
en fonction
de la moyenne de l'étudiant:
NB : Se baser sur cette condition
moyenne  < 10 : Echoué(e)
moyenne  < 12 : Passable
moyenne  < 14 : Assez bien
moyenne  < 18 : Bien
Sinon : Très bien
"""

# note (/10) (/20)

# a = int(input("Entrer la note 1: "))
# b = int(input("Entrer la note 2: "))
# c = int(input("Entrer la note 3: "))
# moyenne = (a + b + c) / 3
# if moyenne < 10:
#     print("Echoué(e)") 
# elif moyenne < 12:
#         print("Passable")
# elif moyenne < 14:
#     print("Assez bien")
# elif moyenne < 18:
#     print("Bien")
# else:
#     print("Très bien")
#    ====> Plus petit ou plus Grand
#    <==== Plus Grand ou plus Petit
#       Echoué      Passable      Assez Bien            Bien       Très Bien
# 0 >= --------|-------------|----------------|------------|------------- <= 20
#        10            12              14            18



# Les boucles for (pour), while (tant que)
# Une boucle c'est une structure itérative (répétition) qui permet de répéter une 
# action plusieurs fois

# For (syntaxe 1)
"""
for i in range(10):
    print(i)

for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)
"""

# White (syntaxe 1)
"""
white i < 10:
    print(i)
    i+=1
"""

# Exercice 7   
# Ecrire un programme qui permet d'afficher boujour 1, boujour 2, boujour 3
# Sans boucle
# print("SANS BOUCLE")
# print("Boujour 1")
# print("Boujour 2")
# print("Boujour 3")
# print()

# Avec boucle
# print("AVEC BOUCLE")
# 1. for
# La boucle for est utilisé lorsqu'on connait le nombre de
# répétition
# range(start, stop, step)
# range (1,     4,     1)
# pour i <- 0 à n-1:
# FinPour
# range(10) = {0-9}
# for i in range(1,4,1):
#     # print("Bonjour", i)
#     # print("Bonjour {} ".format(i))
#     print(f"Bonjour {i}")
#     # print("Bonjour %s"%i)

# i = 1
# while i <= 10:
#     print(f"Bonjour {i}")
#     i += 1 #i = i + 1


# Fonction
# une portion du code qui réutilisable
# Syntaxe:
# def nom_fonction(argument1, argument2.....):
    # instruction 1
    # instruction 2
    #....
    # instruction n

# Exercice fonction application 1
"""
Ecrire un programme qui prend en entrée le nom d'une personne
Et affiche bonjour + le nom de la personne
"""
# Sans fonction
# name = input("Entrez votre nom : ")
# print(f"Bonjour {name}")

# for i in range(10):
#     name = input("Entrez votre nom : ")
#     print(f"Bonjour {name}")
#     print()


# Définition de la fonction
def greet(nom_personne: str):
    print(f"Bonjour {nom_personne}")


# l'appel de la fonction

# greet("Nelsam")
# greet("Josue")

# Exercice fonction application 2
"""
Ecrire un programme qui permet de faire la somme, le produit, le quotient reel et entier
et donne le reste de la division
"""

# a = int(input("Entrez le premier nombre : "))
# b = int(input("Entrez le deuxième nombre : "))
# somme = a + b
# produit = a * b
# quotient_reel = a / b # 1/3 = 0.333
# quotient_entier = a // b # 0
# reste_de_la_division = a % b
# print(f"la somme est : {somme}")
# print(f"la produit est : {produit}")
# print(f"la quotient_reel est : {quotient_reel}")
# print(f"la quotient_entier est : {quotient_entier}")


# c = int(input("Entrez le premier nombre : "))
# d = int(input("Entrez le deuxième nombre : "))
# somme = c + d
# produit = c * d
# quotient_reel = c / d # 1/3 = 0.333
# quotient_entier = c // d # 0
# reste_de_la_division = c % d


def somme (a : float, b: float) -> float:
    return a + b

def produit(a : float, b: float) -> float:
    return a * b

def quotient_reel(num, denom) -> float|str:
    if denom != 0:
        return num / denom
    else:
        return "Math Error"

def quotient_entier(num, denom) -> int|str:
    if denom != 0:
        return num // denom
    else:
        return "Math Error"
    
def reste_div(num, denom) -> int|str:
    if denom != 0:
        return num % denom
    else:
        return "Math Error"
    
def operation2(a,b,sym):
    if b != 0:
        if sym == '%':
            return a % b
        elif sym == '/':
            return a / b
        else:
            return a // b
    else:
        return "Math Error"
    
# Call back
def operation (a, b, function):
    return function(a,b)

    

# a = int(input("Entrez le premier nombre : "))
# b = int(input("Entrez le deuxième nombre : "))
# print(f"la somme est : {somme(a,b)}")
# print(f"la produit est : {produit(a,b)}")
# print(f"le quotient_reel est : {quotient_reel(a,b)}")
# print(f"le quotient_entier est : {quotient_entier(a,b)}")
# print(f"le reste de la division est : {reste_div(a,b)}")
# print(operation(a,b,reste_div))
# print(operation2(a,b,'/'))

# Exercice 8 !!!! A Faire !!!!

#NB : Controle de saisie (la note doit être comprise entre 0 et 20)
""" 
Ecrire un programme qui prend en entrée les notes (3 notes) d'un étudiant,
le programme affiche la mention (Echoué(e), Passable, Assez bien , Bien ou Très bien) 
en fonction
de la moyenne de l'étudiant:
NB : Se baser sur cette condition
moyenne  < 10 : Echoué(e)
moyenne  < 12 : Passable
moyenne  < 14 : Assez bien
moyenne  < 18 : Bien
Sinon : Très bien
"""

## Crée une fonction qui vérifie si une chaine appartient à la base 10 ou pas
def my_isdigit(number: str) -> bool:
    pass

# print("111".isdigit())