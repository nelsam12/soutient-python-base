code = [0,8,9,4,4]
# Rechercher le code avec l'algorithme de recherche
import time
count = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                time.sleep(0.0001)
                count +=1
                print(f"Essai n°{count} : {i}{j}{k}{l}")
                # temps de recherche en secondes
                print(f"Temps de recherche : {count} secondes")
                if code[0] == i and code[1] == j and code[2] == k and code[3] == l:
                    print("Code trouvé")
                    print(i,j,k,l)
                    break
# 10x10x10x10