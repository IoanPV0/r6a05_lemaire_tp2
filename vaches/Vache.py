from vaches.exceptions import InvalidVacheException


class Vache:
    AGE_MAX = 25
    POIDS_MAX = 1000.0
    PANSE_MAX = 50.0
    POIDS_MIN_PANSE = 2.0
    def __init__(self, petit_nom:str = None, age:int = None, poids:float = None, panse:float = None):
        if petit_nom is None or petit_nom.strip() == "":
            raise InvalidVacheException("Le petit nom ne peut pas être vide.")
        if age is None or Vache.AGE_MAX < age or age < 0:
            raise InvalidVacheException(f"L'âge doit être entre 0 et {Vache.AGE_MAX} ans.")
        self._petit_nom = petit_nom
        self._age = age
        self._poids = poids
        self._panse = panse

    @property
    def poids(self) -> float:
        return self._poids
    

    