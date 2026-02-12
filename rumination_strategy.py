from typing import Protocol
from vaches.vache import Vache

class RuminationStrategy(Protocol):

    def calculer_lait(self, vache:"Vache", panse_avant_rumination:float) -> float:
        """Calcule le volume de lait produit pendant une rumination, 0 pour Vache"""
        ...

    def stocker_lait(self, vache:"Vache", volume_lait:float) -> None:
        """Stocke le lait produit pendant une rumination et met à jour le lait dispo"""
        ...

    def post_rumination(self, vache:"Vache") -> None:
        """Reset les rations"""
        ...