def greet(nom_personne: str):
    print(f"Bonjour {nom_personne}")

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


## Crée une fonction qui vérifie si une chaine appartient à la base 10 ou pas
def my_isdigit(number: str) -> bool:
    return number.isdigit()

# print("111".isdigit())

def validate_note(note: str) -> float:
    if my_isdigit(note) :
        print("Is a number")
    else:
        print("Is not a number")
    return 0.0