from vaches.exceptions import InvalidVacheException
from vaches.vache import Vache
from vaches.vache_a_lait import VacheALait
from vaches.nourriture.type_nourriture import TypeNourriture

class PieNoire(VacheALait):
    COEFFICIENT_LAIT_PAR_NOURRITURE: dict[TypeNourriture, float] = {
        TypeNourriture.MARGUERITE: 1.1,
        TypeNourriture.HERBE: 1.0,
        TypeNourriture.FOIN: 0.9,
        TypeNourriture.PAILLE: 0.4,
        TypeNourriture.CEREALES: 1.3,
    }
    def __init__(self, petit_nom:str = None, age:int = None, poids:float = None, nombre_taches_blanches:int = None, nombre_taches_noires:int = None) -> None:
        super().__init__(petit_nom = petit_nom, age = age, poids = poids)

        if nombre_taches_blanches is None or nombre_taches_blanches <= 0:
            raise InvalidVacheException("Le nombre de taches blanches doit être un entier positif.")
        if nombre_taches_noires is None or nombre_taches_noires <= 0:
            raise InvalidVacheException("Le nombre de taches noires doit être un entier positif.")

        self._nombre_taches_noires: int = nombre_taches_noires
        self._nombre_taches_blanches: int = nombre_taches_blanches
        self._ration: dict[TypeNourriture, float] = dict()

    @property
    def nombre_taches_noires(self) -> int:
        return self._nombre_taches_noires
    
    @property
    def nombre_taches_blanches(self) -> int:
        return self._nombre_taches_blanches
    
    @property
    def ration(self) -> dict[TypeNourriture, float]:
        return self._ration.copy() #objet mutable, on retourne une copie pour éviter les modifications externes
    
    def __str__(self):
        return f"{super().__str__()} - Taches blanches: {self.nombre_taches_blanches}, Taches noires: {self.nombre_taches_noires}"
    
    def brouter(self, quantite: float = None, nourriture: TypeNourriture = None) -> None:
        if quantite is None:
            raise InvalidVacheException("La quantité doit être spécifiée.")
        if quantite <= 0.0:
            raise InvalidVacheException("La quantité doit être un nombre positif.")
        if self._panse is None:
            self._panse = 0.0
        nouvelle_panse = self._panse + quantite
        if nouvelle_panse > Vache.PANSE_MAX:
            raise InvalidVacheException("La panse ne peut pas dépasser la capacité maximale.")
        self._panse = nouvelle_panse
        if nourriture not in self._ration:
            self._ration[nourriture] = 0.0
        self._ration[nourriture] += quantite
