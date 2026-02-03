from vaches.exceptions import InvalidVacheException
from vaches.Vache import Vache

class VacheALait(Vache):
    RENDEMENT_LAIT = 1.1
    PRODUCTION_LAIT_MAX = 40.0
    def __init__(self, petit_nom:str = None, age:int = None, poids:float = None, panse:float = 0.0) -> None:
        super().__init__(petit_nom=petit_nom, age=age, poids=poids, panse=panse)
        self._lait_disponible = 0.0
        self._lait_total_produit = 0.0
        self._lait_total_traite = 0.0

    