
class AnalyseurError(Exception):
    """Exception de base pour les operations sur un corpus."""

class TexteVideError(AnalyseurError):
    def __init__(self, titre: str):
        super().__init__(f"Le document {titre} est vide")

class FormatInconnuError(AnalyseurError):
    pass


# Utilisation
if __name__ == "__main__":
    from corpus import Corpus
    corpus = Corpus("Mon corpus")
    try:
        doc = corpus.rechercher_mot("Bovary")
        print(doc)
    except TexteVideError as e:
        print(f"Erreur : {e}")
        print(f"Titre cherche : {e.titre}")
    except AnalyseurError:
        print("Autre erreur de corpus")