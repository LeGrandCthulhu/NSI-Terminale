def somme(liste: list) -> int:
    """
    (Récursive) Somme des entier contenues dans une liste
    """
    try:
        if not liste: # Cas de fin
            return 0

        if type(liste[0]) != int: # Vérifie que c'est bien des entiers
            raise ValueError
        else:
            return liste[0] + somme(liste[1:])

    except TypeError:
        print("La fonction à pour paramètre une liste d'entier")
    except ValueError:
        print("La liste doit être composé exclusivement d'entiers.")

def fact_it(n: int) -> int:
    try:
        if n < 0:
            raise ValueError
        
        fact = 1
        if n == 0:
            return fact

        for i in range(1, n+1):
            fact *= i
        
        return fact
    
    except TypeError:
        print("Le paramètre doit être un entier positif")
    except ValueError:
        print("L'entier fournit doit être positif")

    

