""
from texte import Texte

class Roman(Texte) :

    def __init__(self, titre: str, auteur: str, contenu: str, annee: int, genre: str) -> None:
        super().__init__(titre, auteur, contenu, annee)
        self.genre = genre

    def resume (self) -> None:
        print (f"{self.titre}, {self.genre}")

