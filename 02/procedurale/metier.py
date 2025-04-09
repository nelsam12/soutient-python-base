from db import livres
from tabulate import tabulate
def add_book(title :str, gender, author:str, year) -> None:
    livre = {
        "titre" : title,
        "auteur" : author.capitalize(),
        "annee" : year,
        "genre" : gender
    }
    # livre["titre"] => ERROR | livre.get("titre") => None
    livres.append(
        livre
    )
    print(f"Vous avez au total {len(livres)} livres")

def get_book_by_title(title : str) -> list:
    founded_books = []
    title = title.upper() #Majuscule
    for livre in livres:
        title_found = livre.get("titre").upper() #Majuscule
        if title_found == title or title_found.startswith(title):
            founded_books.append(livre)
    return founded_books


def delete_book(title : str) -> None:
    book = get_book_by_title(title)[0] if len(get_book_by_title(title)) > 0 else None
    # operateur ternaire condition ? true : false
    if not book:
        print("Livre introuvable")
        return
    if book:
        print(f"Livre {book.get('titre')} supprimé")
        livres.remove(book)
      


def display_items(items : list , header : dict):
    if len(items) == 0:
        print("Liste vide")
    else:
        print(tabulate(items, 
                       tablefmt="rounded_grid", 
                       headers=header
    ))

def display_book(books : list[dict] = livres):
    display_items(books, {"Titre" : "", "Auteur" : "", "Année" : "", "Genre" : ""})