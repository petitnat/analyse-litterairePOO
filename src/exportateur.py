from abc import ABC, abstractmethod

from texte import Texte

class Exportateur(ABC) :
    @abstractmethod
    def exporter (self, texte: Texte) -> str : ...

class ExportateurHTML(Exportateur) :

    def exporter (self, texte: Texte) -> str :
        return f"<h1>{texte.titre}<h1><p>{texte.contenu}</p></h1>"

class ExportateurCSV(Exportateur) :
    def exporter (self, texte: Texte) -> str :
        return f'"{texte.titre}";"{texte.contenu.replace('"', "''").replace("\n",r"\n")}"'