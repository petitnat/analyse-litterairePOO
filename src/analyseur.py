"" 
from abc import ABC, abstractmethod

class AnalyseurTexte(ABC):
    @abstractmethod
    def analyser(self, texte: "Document") -> dict: ...
    def analyser_corpus(self, docs: list["Document"]) -> list[dict]:
        return [self.analyser(d) for d in docs]

# a = AnalyseurTexte()  # TypeError !
class CompteurMots(AnalyseurTexte):
    def analyser(self, texte: "Document") -> dict:
        mots = texte.resume().lower().split()
        return {"total": len(mots), "uniques": len(set(mots))}