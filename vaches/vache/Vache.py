class Vache:
    AGE_MAX = 25
    POIDS_MAX = 1000.0
    PANSE_MAX = 50.0
    POIDS_MIN_PANSE = 2.0
    def __init__(self, petit_nom:str = None, age:int = None, poids:float = None, panse:float = None):
        self._petit_nom = petit_nom
        self._age = age
        self._poids = poids
        self._panse = panse

    