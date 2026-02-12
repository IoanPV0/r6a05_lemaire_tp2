from vaches.exceptions import InvalidVacheException
from vaches.vache import Vache

class VacheALait(Vache):
    RENDEMENT_LAIT = 1.1
    PRODUCTION_LAIT_MAX = 40.0
    def __init__(self, petit_nom:str = None, age:int = None, poids:float = None) -> None:
        super().__init__(petit_nom = petit_nom, age = age, poids = poids)

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
    
    def __str__(self) -> str:
        return f"{super().__str__()} - Lait disponible : {self.lait_disponible:.1f} L, Lait total produit : {self.lait_total_produit:.1f} L, Lait total trait : {self.lait_total_traite:.1f} L"
    
        
    def ruminer(self):
        super().ruminer()
    
    def _calculer_lait(self, panse_avant = None) -> float:
        lait = VacheALait.RENDEMENT_LAIT * panse_avant
        return lait
    
    def _stocker_lait(self, lait: float) -> None:
        self._lait_disponible += lait
        super()._stocker_lait(lait)

    def _post_rumination(self, panse_avant, lait):
        self._lait_total_produit += lait
        return super()._post_rumination(panse_avant, lait)
    
    def _valider_rumination_possible(self):
        if self._lait_disponible + (VacheALait.RENDEMENT_LAIT * self._panse) > VacheALait.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException("La production de lait a dépassé la limite maximale.")
        return super()._valider_rumination_possible()
    
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
        