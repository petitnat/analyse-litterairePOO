from texte import Texte


class LecteurCSV:
    def lire_lignes(self, chemin: str) -> list[dict]:
        import csv
        with open(chemin) as f: return list(csv.DictReader(f))

class AdaptateurCSV :

    def charger (self, csvlu: list[dict]) -> list[Texte]:
        fini = []
        for index in csvlu :
            fini.append(Texte(index["titre"], index["auteur"], index["contenu"], index["annee"]))
        return fini



