# Dana  jest  lista  identyfikatorów n wagonów  (każdy  numer  to  liczba  32  bitowa). Oprócz tego mamy też listę
# połączeń wagonów, gdzie każde pole zawiera identyfikatory dwóch połączonych wagonów  (wiadomo,  że  lista  jest  poprawna;
# w  szczególności  dany  wagon  może  być  połączony  najwyżej  zdwoma innymi wagonami i żaden skład nie tworzy cyklu).
# Proszę zaproponować algorytm obliczający długośćnajdłuższego ciągu wagonów.

class Zestaw:
    def __init__(self):
        self.len = 1
        self.end = self

def trains(links):
    zajezdnia = {}
    for wagon in set([wagon for link in links for wagon in link]):
        zajezdnia[wagon] = Zestaw()

    result = 0
    for link in links:
        zestawA = zajezdnia[link[0]]
        zestawB = zajezdnia[link[1]]

        newLen = zestawA.len + zestawB.len

        if newLen > result:
            result = newLen

        tmp = zestawA.end
        zestawA.end.end = zestawB.end
        zestawB.end.end = tmp

        zestawA.len = newLen
        zestawB.len = newLen
        zestawA.end.len = newLen
        zestawB.end.len = newLen

    return result

links = [(1, 2), (2, 3), (5, 6), (6, 7), (4, 5)]
print(trains(links))
