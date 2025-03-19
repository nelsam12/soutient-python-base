### BOUCLE + LIST + TUPLE + Fonction lambda ###
# list
# tuple
# import pprint

# roles = ("Admin", "Admin","Dba", "System") # Sécurisé
# roles2 = ["Admin", "Dba", "System"] # Non Sécurisé

# # Ajouter un role à roles2
# roles2.append("Client")
# roles_= [roles, roles2]
# pprint.pprint(roles_)


"""
On va enregistrer les informations des étudiants (matricule, nom, prenom, age, notes)
Réaliser le menu suivant:
1. Enregistrer un nouvel étudiant
2. Afficher tous les étudiants
3. Rechercher un etudiant par son matricule
4. Afficher les notes d'un étudiant
5. Calculer la moyenne d'un étudiant
6. Exporter les étudiants dans un fichier txt, json, tinydb
7. Récupérer les informations des étudiants depuis un fichier txt, json
8. Faire la même que les questions 6 et 7 avec une base de données mysql, postgres voir oracle (à voir après)
9. Générer un fichier pdf (bulletin de l'étudiant)
10. Quitter
"""



import func

if __name__ == "__main__":
    while True:
        choice = func.get_choice()
        if choice == 1:
            print("Enregistrement de l'étudiant")
            etudiant = func.input_student()
            func.save_student(etudiant)
        elif choice == 2:
            func.display_students()
        elif choice == 10:
            break
        else:
            print("Fonctionalités non disponible")

        # match case

