"" 
from abc import ABC, abstractmethod
from collections import Counter
from texte import Texte

class AnalyseurTexte(ABC):

    @abstractmethod
    def analyser(self, texte: "Texte") -> dict: ...

    def analyser_corpus(self, docs: list["Texte"]) -> list[dict]:
        return [self.analyser(d) for d in docs]

# a = AnalyseurTexte()  # TypeError !
class CompteurMots(AnalyseurTexte):

    def analyser(self, texte: "Texte") -> dict:
        mots = texte.resume().lower().split()
        return {"total": len(mots), "uniques": len(set(mots))}

class AnalyseurFrequence(AnalyseurTexte):

    def analyser(self, texte: "Texte"):
        return (texte.frequences().most_common(10))

class AnalyseurLongueur(AnalyseurTexte):
    """analyseur de longueur"""
    def analyser(self, texte: "Texte") -> dict:
        return f"""nombre de mots : {texte.nombre_mots()}, nombre de phrases : {texte.nombre_phrases()}, """
    def analyser_corpus(self, docs: list["Texte"]) -> list[dict]:
        """analyseur de corpus"""
        effectif = 0
        result =""
        for d in docs :
            effectif += d.nombre_phrases()
            result += self.analyser(d) +"\n"
        return f"{result}moyenne de phrases : {effectif/len(docs)}"

if __name__ == "__main__":



    texte1 = Texte("Droit de la femme", "eMILE", """A LA REINE.


    MADAME,

    Peu faite au langage que l'on tient aux Rois, je n'emploierai point
    l'adulation des Courtisans pour vous faire hommage de cette singulière
    production. Mon but, Madame, est de vous parler franchement; je n'ai
    pas attendu, pour m'exprimer ainsi, l'époque de la Liberté: je me
    suis montrée avec la même énergie dans un temps où l'aveuglement des
    Despotes punissait une si noble audace.

    Lorsque tout l'Empire vous accusait et vous rendait responsable de ses
    calamités, moi seule, dans un temps de trouble et d'orage, j'ai eu la
    force de prendre votre défense. Je n'ai jamais pu me persuader qu'une
    Princesse, élevée au sein des grandeurs, eût tous les vices de la
    bassesse.

    Oui, Madame, lorsque j'ai vu le glaive levé sur vous, j'ai jeté mes
    observations entre ce glaive et la victime; mais aujourd'hui que je
    vois qu'on observe de près la foule de mutins soudoyée, & qu'elle est
    retenue par la crainte des loix, je vous dirai, Madame, ce que je ne
    vous aurois pas dit alors.
    """, 1200)

    cm = CompteurMots()
    print(cm.analyser(texte1))
    dixplus = AnalyseurFrequence()
    print(dixplus.analyser(texte1))
    stats = AnalyseurLongueur()
    print(stats.analyser(texte1))