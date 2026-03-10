""
from texte import Texte

class Roman(Texte) :

    def __init__(self, titre: str, auteur: str, contenu: str, annee: int, genre: str) -> None:
        super().__init__(titre, auteur, contenu, annee)
        self.genre = genre

    def resume (self) -> str:
        print (f"{self.titre}, {self.genre}")

class Poesie(Texte) :

    def __init__(self, titre: str, auteur: str, contenu: str, annee: int, forme: str)-> None:
        super().__init__(titre, auteur, contenu, annee)
        self.vers = contenu.replace("/n/n", "/n").count("/n")

    def resume (self) -> str:
        print (f"{self.titre}, {self.vers}")

class Article(Texte) :
    def __init__(self, titre: str, auteur: str, contenu: str, annee: int, revue : str) -> None:
        super().init(titre, auteur, contenu, annee)
        self.revue = revue

    def 

petitpoeme = Poesie("Le bateau ivre", "Arthur Rimbaud", "Comme je descendais des Fleuves impassibles,"
                                                         "Je ne me sentis plus guidé par les haleurs :"
                                                         "Des Peaux-Rouges criards les avaient pris pour cibles,"
                                                         "Les ayant cloués nus aux poteaux de couleurs."
                                                         "J’étais insoucieux de tous les équipages,"
                                                         "Porteur de blés flamands ou de cotons anglais."
                                                         "Quand avec mes haleurs ont fini ces tapages,"
                                                         "Les Fleuves m’ont laissé descendre où je voulais."
                                                         "Dans les clapotements furieux des marées,"
                                                         "Moi, l’autre hiver, plus sourd que les cerveaux d’enfants,"
                                                         "Je courus ! Et les Péninsules démarrées"
                                                         "N’ont pas subi tohu-bohus plus triomphants."
                                                         "La tempête a béni mes éveils maritimes."
                                                         "Plus léger qu’un bouchon j’ai dansé sur les flots"
                                                         "Qu’on appelle rouleurs éternels de victimes,"
                                                         "Dix nuits, sans regretter l’oeil niais des falots !", 1898, "sonnet")



print (petitpoeme.resume())