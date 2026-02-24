"""
Corpus est un conteneur de texte
"""
from texte import Texte

class Corpus:

    def __init__(self, name: str):
        self._name = name
        self._textes = list[Texte] = []
    
    @property
    def name(self) -> str:
        return self._name