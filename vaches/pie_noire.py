from vaches.exceptions import InvalidVacheException
from vaches.vache import Vache, VacheALait
from nourriture.type_nourriture import TypeNourriture

class PieNoire(VacheALait):
    COEFFICIENT_LAIT_PAR_NOURRITURE = dict[type_nourriture, float]
    def __init__(self, petit_nom:str = None, age:int = None, poids:float = None, nombre_tache_blanche:int = None, nombre_tache_noire:int = None) -> None:
        super().__init__(petit_nom = petit_nom, age = age, poids = poids)

        self._nombre_tache_noire: int = nombre_tache_noire
        self._nombre_tache_blanche: int = nombre_tache_blanche

    @property
    def nombre_tache_noire(self) -> int:
        return self._nombre_tache_noire
    
    @property
    def nombre_tache_blanche(self) -> int:
        return self._nombre_tache_blanche
    
    @property
    def __str__(self):
        return super().__str__()