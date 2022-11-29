"""
Calcule des aires de différentes figures.

---

triangle(int ou float > 0, int ou float > 0)
    Description: Calcule l'aire d'un triangle.
    Entrées: base (int ou float > 0) longueur de la base du triangle.
             hauteur (int ou float > 0) longueur de la hauteur du triangle.
    Sortie: aire (int ou float) aire du triangle.

---

disque(int ou float > 0)
    Description: Calcule l'aire d'un disque.
    Entrée: rayon (int ou float > 0) longueur du rayon.
    Sortie: aire (int ou float > 0) aire du disque

---

carre(int ou float > 0)
    Description: Calcule l'aire d'un carré.
    Entrée: coté (int ou float > 0) longueur du côté.
    Sortie: aire (int ou float > 0) aire du carré.

---

parallélogramme(int ou float > 0)
    Description: Calcule l'aire d'un parallélogramme.
    Entrées: longueur (int ou float > 0) longueur d'un côté du parallélogramme.
             largeur (int ou float > 0) longueur de la largeur du parallélogramme.
    Sortie: aire (int ou float) aire du parallélogramme.

---

losange(int ou float > 0)
    Description: Calcule l'aire d'un losange.
    Entrées: grandeDiagonale (int ou float > 0) longueur de la grande diagonale du losange.
             petiteDiagonale (int ou float > 0) longueur de la petite diagonale du losange.
    Sortie: aire (int ou float) aire du losange.

---

trapeze(int ou float > 0)
    Description: Calcule l'aire d'un trapèze.
    Entrées: grandeBase (int ou float > 0) longueur de la grande base du trapèze.
             petiteBase (int ou float > 0) longueur de la petite base du trapèze.
             hauteur (int ou float > 0) hauteur du trapèze.
    Sortie: aire (int ou float) aire du trapèze.
"""

from math import *

def triangle(base, hauteur):
    """
    Description: Calcule l'aire d'un triangle.
    Entrées: base (int ou float > 0) longueur de la base du triangle.
             hauteur (int ou float > 0) longueur de la hauteur du triangle.
    Sortie: aire (int ou float) aire du triangle.
    """
    try:
        if base <= 0 or hauteur <= 0:
            raise ValueError
        aire = (base * hauteur) / 2
        return aire
    except TypeError:
        print("Les paramètres doivent être des nombres.")
    except ValueError:
        print("Les paramètres doivent être strictements positifs.")

def disque(rayon):
    """
    Description: Calcule l'aire d'un disque.
    Entrée: rayon (int ou float > 0) longueur du rayon.
    Sortie: aire (int ou float > 0) aire du disque
    """
    try:
        if rayon <= 0:
            raise ValueError
        aire = pi * rayon**2
        return aire
    except TypeError:
        print("Le rayon doit être un nombre.")
    except ValueError:
        print("Le rayon doit être strictement supérieur à 0.")

def carre(cote):
    """
    Description: Calcule l'aire d'un carré.
    Entrée: coté (int ou float > 0) longueur du côté.
    Sortie: aire (int ou float > 0) aire du carré.
    """
    try:
        if cote <= 0:
            raise ValueError
        aire = cote**2
        return aire
    except TypeError:
        print("Le côté doit être un nombre.")
    except ValueError:
        print("Le côté doit être strictement supérieur à 0.")

def parallelogramme(longueur, largeur):
    """
    Description: Calcule l'aire d'un parallélogramme.
    Entrées: longueur (int ou float > 0) longueur d'un côté du parallélogramme.
             largeur (int ou float > 0) longueur de la largeur du parallélogramme.
    Sortie: aire (int ou float) aire du parallélogramme.
    """
    try:
        if longueur <= 0 or largeur <= 0:
            raise ValueError
        aire = longueur * largeur
        return aire
    except TypeError:
        print("Les paramètres doivent être des nombres.")
    except ValueError:
        print("Les paramètres doivent être strictements positifs.")

def losange(grandeDiagonale, petiteDiagonale):
    """
    Description: Calcule l'aire d'un losange.
    Entrées: grandeDiagonale (int ou float > 0) longueur de la grande diagonale du losange.
             petiteDiagonale (int ou float > 0) longueur de la petite diagonale du losange.
    Sortie: aire (int ou float) aire du losange.
    """
    try:
        if grandeDiagonale <= 0 or petiteDiagonale <= 0:
            raise ValueError
        aire = (grandeDiagonale * petiteDiagonale) / 2
        return aire
    except TypeError:
        print("Les paramètres doivent être des nombres.")
    except ValueError:
        print("Les paramètres doivent être strictements positifs.")

def trapeze(grandeBase, petiteBase, hauteur):
    """
    Description: Calcule l'aire d'un trapèze.
    Entrées: grandeBase (int ou float > 0) longueur de la grande base du trapèze.
             petiteBase (int ou float > 0) longueur de la petite base du trapèze.
             hauteur (int ou float > 0) hauteur du trapèze.
    Sortie: aire (int ou float) aire du trapèze.
    """
    try:
        if grandeBase <= 0 or petiteBase <= 0 or hauteur <= 0:
            raise ValueError
        aire = (grandeBase * petiteBase) / (hauteur * 2)
        return aire
    except TypeError:
        print("Les paramètres doivent être des nombres.")
    except ValueError:
        print("Les paramètres doivent être strictements positifs.")


# A tester en profondeur.