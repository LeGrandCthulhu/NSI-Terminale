from math import inf
import errors

# Exercice 3

def min_liste(liste):
    """
    Description: Renvoie la valeur minimale d'une liste.
    Entrée: liste (list) liste avec les nombres.
    Sortie: mini (int ou float) le minimum de la liste.
    """

    try:
        if len(liste) == 0:                                         # Vérifie si la liste n'est pas vide.
            raise errors.EmptyListError
            
        if type(liste[0]) != int and type(liste[0]) != float:       # Vérifie que la première valeur est bien un nombre.
            raise ValueError
            
        mini = liste[0]

        for i in range(1, len(liste)):                              # Parcours la liste pour chercher le mini.
            if type(liste[i]) != int and type(liste[i]) != float:   # Vérifie que les valeurs de la liste sont bien des nombres.
                raise ValueError

            elif liste[i] < mini:                                   # Redéfinie mini si la nouvelle valeur est plus basse.
                mini = liste[i]

            else:
                pass

        # Fatal errors
    except ValueError:
        print("Les valeurs de la listes doivent êtres des nombres.")
        return
        
    except errors.EmptyListError:
        print("La liste est vide.")
        return
        
    except TypeError:
        print("La fonction demande une liste en paramètre.")
        return
    
    return mini

# Tested

# Exercice 4

def saisir_entier(message="Saisir un entier: ", a=-inf, b=inf):
    """
    Description: Renvoie l'entier saisi (oui c'est claqué).
    Entrées: message (str) =  "Saisir un entier: " message de l'input de l'entier.
             a (int ou float) = -inf borne minimale de l'intervalle.
             b (int ou float) = inf borne maximale de l'intervalle.
    Sortie: nb (int) entier saisi.
    """

    while True:
        try:
            if type(a) != int and type(a) != float or type(b) != int and type(b) != float: # Vérifie si a et b sont bien des nombres
                raise TypeError

            if a > b:                           # Vérifie que c'est un intervalle correcte.
                raise errors.IntervalError

            nb = int(input(message))            # Demande la saisie de l'entier.

            if nb > b or nb < a:                # Vérifie que l'entier saisi est bien compris dans l'intervalle.
                raise errors.ValueOutOfInterval
            
            break

        # Erreurs de saisie
        except ValueError:
            print("Mets un entier la con de toi.")
        
        except errors.ValueOutOfInterval:
            print(f"L'entier doit être entre {a} et {b}.") 

        # Erreurs fatales de paramètres
        except errors.IntervalError:
            print("L'intervalle n'est pas correcte, la borne minimale est supérieur à la borne maximale.")
            return
        
        except TypeError:
            print("Les bornes de l'intervalle doivent être des nombres.")
            return
            
    
    return nb

# Tested

