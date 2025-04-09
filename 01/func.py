# Les fonctions concernant notre application
import consts
import functions
import os

def display_menu(items: list = consts.MENU, sym :str = ")") -> int:
    for index,item in enumerate(items, start=1):
        print(f"{index}{sym} {item}")
    return len(items)

def get_choice() -> int:
    while True:
        size = display_menu()
        choice = input("Entrez votre choix : ")
        if not functions.my_isdigit(choice):
            clear()
            print("ERROR : Entrez un nombre")
            continue
        if int(choice) > size or int(choice)<=0:
            clear()
            print(f"Entrez un nombre entre 1 et {size}")
            continue
        return int(choice)
    
import db
def save_student(etudiant: dict) -> int:
    db.students.append(etudiant)
    return len(db.students)


def input_student() -> dict:
    return {
        "matricule" : generate_matricule(),
        "nom" : input("Nom : "),
        "prenom" : input("Prénom : "),
        "age" : input("Age : ") + " ans",
        "notes" : [18, 20, 7, 5] 
    }
from tabulate import tabulate
def display_students(students : list = db.students):
    if len(students) == 0:
        print("Pas d'étudiant actuellement")
    else:
        print(tabulate(students, 
                       tablefmt="rounded_grid", 
                       headers={
        "MAT" : "",
        "NOM" : "",
        "PRENOMS" : "",
        "AGE" : ""
    }
    ))


def generate_matricule():
    return f"MAT-{len(db.students) + 1}"

# LAMBDA
clear = lambda : os.system("clear")

# A FAIRE
def get_student_by_matricule():
    pass

def get_mark_of_student(student : dict):
    pass

def get_average_of_student(student : dict):
    pass


if __name__ == "__main__":
    pass