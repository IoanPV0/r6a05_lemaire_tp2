from vaches.exceptions import InvalidVacheException

class Vache:
    AGE_MAX = 25
    POIDS_MAX = 1000.0
    PANSE_MAX = 50.0
    POIDS_MIN_PANSE = 2.0
    RENDEMENT_RUMINATION = 0.25
    _compteur = 0
    def __init__(self, petit_nom:str = None, age:int = None, poids:float = None, panse:float = 0.0) -> None:

        Vache._compteur += 1

        if petit_nom is None or petit_nom.strip() == "":
            raise InvalidVacheException("Le petit nom ne peut pas être vide.")
        if age is None or Vache.AGE_MAX < age or age < 0:
            raise InvalidVacheException(f"L'âge doit être entre 0 et {Vache.AGE_MAX} ans.")
        if poids is None or poids <= 0.0:
            raise InvalidVacheException("Le poids doit être un nombre positif.")
        
        self._id: int = Vache._compteur
        self._petit_nom: str = petit_nom
        self._age: int = age
        self._poids: float = poids
        self._panse: float = panse

    @property
    def poids(self) -> float:
        return self._poids
    
    @property
    def panse(self) -> float:
        return self._panse
    
    @property
    def age(self) -> int:
        return self._age
    
    def brouter(self, quantite: float = None, nourriture: str = None) -> None:
        if quantite is None:
            raise InvalidVacheException("La quantité doit être spécifiée.")
        if quantite <= 0.0:
            raise InvalidVacheException("La quantité doit être un nombre positif.")
        if nourriture is not None:
            raise InvalidVacheException("Cette vache ne peut pas manger de nourriture typée.")
        if self._panse is None:
            self._panse = 0.0
        nouvelle_panse = self._panse + quantite
        if nouvelle_panse > Vache.PANSE_MAX:
            raise InvalidVacheException("La panse ne peut pas dépasser la capacité maximale.")
        self._panse = nouvelle_panse
    
    def ruminer(self) -> None:
        self._valider_rumination_possible()
        panse_avant = self._panse
        gain = Vache.RENDEMENT_RUMINATION * panse_avant
        if self.panse > 0.0:
            panse_avant = self.panse
            self._panse = 0.0
        else :
            raise InvalidVacheException("La panse est vide, la vache ne peut pas ruminer.") 
        gain = Vache.RENDEMENT_RUMINATION * panse_avant
        self._poids += gain
        lait = self._calculer_lait(panse_avant)
        self._stocker_lait(lait)
        self._panse = 0.0
        self._post_rumination(panse_avant, lait)

    def vieillir(self) -> None:
        if self.age < Vache.AGE_MAX:
            self._age += 1
        else:
            raise InvalidVacheException("La vache a atteint l'âge maximum et ne peut pas vieillir davantage.")
        
    def _calculer_lait(self, panse_avant : float = None) -> float:
        return None
    
    def _stocker_lait(self, lait : float) -> None:
        pass

    def _post_rumination(self, panse_avant : float, lait: float) -> None:
        pass
    
    def _ajouter_panse(self, quantite: float) -> None:
        pass

    def _valider_rumination_possible(self) -> None:
        pass

    def _valider_etat(self) -> None:
        pass

    def __str__(self):
        pass