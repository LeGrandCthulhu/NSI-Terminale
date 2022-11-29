"""
Calcule des aires de différentes figures.

---

triangle(int ou float > 0, int ou float > 0)
    Description: Calcule l'aire d"un triangle
    Entrées: base (int ou float > 0) longueur de la base du triangle.
             hauteur (int ou float > 0) longueur de la hauteur du triangle.
    Sortie: aire (int ou float) aire du triangle.

---

disque(int ou float > 0)
"""

def triangle(base, hauteur):
    """
    Description: Calcule l'aire d"un triangle
    Entrées: base (int ou float > 0) longueur de la base du triangle.
             hauteur (int ou float > 0) longueur de la hauteur du triangle.
    Sortie: aire (int ou float) aire du triangle.
    """
    try:
        if base <= 0 or hauteur <= 0:
            raise ValueError("Les paramètres doivent être strictements supérieurs à 0")
        aire = (base * hauteur) / 2
        return aire
    except TypeError:
        raise TypeError("Les paramètre doivent êtres des nombres.")

def disque(rayon):
    """
    Description: Calcule l'aire d'un disque
    Entrée: rayon (int ou float > 0) longueur du rayon.
    Sortie: aire (int ou float > 0) aire du disque
    """
