# Définie les erreurs possibles dans les fonctions

class EmptyListError(Exception):
    """Lorsque la liste requise est vide mais ne le devrait pas."""

class ValueOutOfInterval(Exception):
    """Lorsque l'entier saisi est en dehors de l'intervalle définie"""
    pass

class IntervalError(Exception):
    """Lorsque a > b alors que l'intervalle est [a;b]"""
    pass

