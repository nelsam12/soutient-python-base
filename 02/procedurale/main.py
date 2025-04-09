
# 1 Ajouter
# 2 Rechercher (par le titre)
# 3 Supprimer
# 4 Afficher


import os
from metier import *

menus = [
    "Ajouter un livre",
    "Rechercher un livre par son titre",
    "Supprimer un livre",
    "Lister les livres"
]
def display_menu(items: list , sym :str = ")") -> int:
    for index,item in enumerate(items, start=1):
        print(f"{index}{sym} {item}")
    return len(items)


clear = lambda : os.system("clear")

def my_isdigit(number: str) -> bool:
    return number.isdigit()

def get_choice() -> int:
    while True:
        size = display_menu(menus)
        choice = input("Entrez votre choix : ")
        if not my_isdigit(choice):
            clear()
            print("ERROR : Entrez un nombre")
            continue
        if int(choice) > size or int(choice)<=0:
            clear()
            print(f"Entrez un nombre entre 1 et {size}")
            continue
        return int(choice)

# Fonctionnalité ajout d'un livre

if __name__ == "__main__" :
    while True:
        choice = get_choice()
        match choice:
            case 1:
                title = input("Titre du livre : ")
                genre = "Fiction"
                author = "Antoine de St-Exupery"
                year = 1968
                add_book(title, genre, author, year)
            case 2:
                title = input("Titre du livre recherché : ")
                display_book(get_book_by_title(title))
            case 3:
                title = input("Titre du livre à supprimer : ")
                delete_book(title)
            case 4:
                display_book()
            case _:
                print("Fonctionalités non disponible")

        # match case

# listes = [
#     {
#         "id" : 1,
#         "titre" : "1984",
#     },
#     {
#         "id" : 2,
#         "titre" : "Le Petit Prince",
#     },
#     {
#         "id" : 3,
#         "titre" : "Harry Potter à l'école des sorciers",
#     },
#     {
#         "id" : 4,
#         "titre" : "Les Misérables",
#     },
#     {
#         "id" : 5,
#         "titre" : "L'Étranger",
#     },
#     {
#         "id" : 6,
#         "titre" : "Don Quichotte",
#     },
# ]

# item = {
#         "id" : 1,
#         "titre" : "1984",
#     }
# listes.remove(item)
# print(listes)


