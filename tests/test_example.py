
from corpus import Corpus
from texte import Texte
from adaptateurs import LecteurCSV, AdaptateurCSV



# def test_version():
#     assert __version__ == "0.1.0"


def test_ajout_au_corpus_fonctionne():
    t1 = Texte("Germinal", "Émile Zola", "La mine était noire et profonde", 1885)
    t2 = Texte(
        "Madame Bovary", "Gustave Flaubert", "Elle rêvait de voyages lointains", 1857
    )

    corpus = Corpus("Romans du XIXe")
    corpus.ajouter_texte(t1)
    corpus.ajouter_texte(t2)
    assert len(corpus._textes) == 2

def test_adaptateurs_fonctionne():
    csv_lu = LecteurCSV().lire_lignes("./tests/donnees.csv")
    adaptateur = AdaptateurCSV()
    textes = adaptateur.charger(csv_lu)
    assert len(textes) == 1

# def test_rechercher_mot():
#     roman = Corpus("Romans")
#
#     roman.ajouter_texte(Texte("Droit de la femme", "eMILE", """A LA REINE.
#
#
#         MADAME,
#
#         Peu faite au langage que l'on tient aux Rois, je n'emploierai point
#         l'adulation des Courtisans pour vous faire hommage de cette singulière
#         production. Mon but, Madame, est de vous parler franchement; je n'ai
#         pas attendu, pour m'exprimer ainsi, l'époque de la Liberté: je me
#         suis montrée avec la même énergie dans un temps où l'aveuglement des
#         Despotes punissait une si noble audace.
#
#
#         """, 1200))
#
#     assert roman.rechercher_mot("courtisans") == "courtisans"

test_adaptateurs_fonctionne()
test_ajout_au_corpus_fonctionne()