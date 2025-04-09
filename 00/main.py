def tri_bulle():
    is_ranged = False
# Saisie des nombres séparés par des espaces
    ma_liste = input("Entrez une liste de nombres entiers en utilisant l'espace comme séparateur : ")
# Transformation de la chaîne de caractères en liste d'entiers
    liste = [int(x) for x in ma_liste.split()]
# Rangement de la liste
    x = len(liste)
    for i in range(x):
        for j in range(0, x - i - 1):
# Arrangement en ordre croissant
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
# Afficher la liste trié
    print("Liste triée :", liste)

tri_bulle()

