from vaches.exceptions import InvalidVacheException
from vaches.vache import Vache

class VacheALait(Vache):
    RENDEMENT_LAIT = 1.1
    PRODUCTION_LAIT_MAX = 40.0
    def __init__(self, petit_nom:str = None, age:int = None, poids:float = None) -> None:
        super().__init__(petit_nom = petit_nom, age = age, poids = poids, panse = 0.0)
        self._lait_disponible: float = 0.0
        self._lait_total_produit: float = 0.0
        self._lait_total_traite: float = 0.0

    @property
    def lait_disponible(self) -> float:
        return self._lait_disponible
    
    @property
    def lait_total_produit(self) -> float:
        return self._lait_total_produit
    
    @property
    def lait_total_traite(self) -> float:
        return self._lait_total_traite
    
    @property
    def __str__(self):
        return super().__str__()
    
    def ruminer(self):
        super().ruminer()
    
    def _calculer_lait(self, panse_avant = None):
        lait = VacheALait.RENDEMENT_LAIT * panse_avant
        self._lait_disponible += lait
        self._lait_total_produit += lait
        return lait
    
    def traire(self, litres: float = None) -> float:
        if litres is None:
            raise InvalidVacheException("La quantité de lait à traire doit être spécifiée.")
        if litres <= 0.0:
            raise InvalidVacheException("La quantité de lait à traire doit être un nombre positif.")
        if litres > self._lait_disponible:
            raise InvalidVacheException("La quantité de lait à traire ne peut pas dépasser la quantité disponible.")
        self._lait_disponible -= litres
        self._lait_total_traite += litres
        return litres
        