# kolos 2015/zad3
# W ramach obchodów międzynarodowego święta cyklistów organizatorzy przewidzieli górskąwycieczkę rowerową.
# Będzie się ona odbywać po bardzo wąskiej ścieżce, na której rowery mogąjechać tylko jeden za drugim.
# W ramach zapewnienia bezpieczeństwa każdy rowerzysta będziemiał numer identyfikacyjny oraz małe urządzenie,
# przez które będzie mógł przekazaćidentyfikator rowerzysty przed nim (lub -1 jeśli nie widzi przed sobą nikogo).
# Należy napisaćfunkcję, która na wejściu otrzymuje informacje wysłane przez rowerzystów i oblicza rozmiarnajmniejszej grupy
# (organizatorzy obawiają się, że na małe grupy mogłyby napadać dzikiezwierzęta). Dane są następujące struktury danych:
# struct Cyclist{int id, nid;) // identyfikator rowerzysty oraz tego, którego widzi};
# Funkcja powinna mieć prototypint smallestGroup( Cyclist cyclist[], int n ), gdziecyclistto tablicanrowerzystów.
#     Funkcja powinna być możliwie jak najszybsza. Można założyć,że identyfikatory rowerzystów to liczby z zakresu 0 do 108
# (osiem cyfr napisanych w dwóchrzędach na koszulce rowerzysty) i że pamięć nie jest ograniczona. Rowerzystów jest jednak dużo
# mniej niż identyfikatorów (nie bez powodu boją się dzikich zwierząt). Należy zaimplementować wszystkie potrzebne struktury danych.

class Cyclist:
    def __init__(self):
        self.id = None
        self.nid = None
class Bettercyclist:
    def __init__(self):
        self.id = None
        self.nid = None
        self.pid = None

def hash_function (id):
    hash=0
    hash^=(id>>2)+id
    return hash

def add_to_hashtable (bettercyclists, cyclists, bettern, n, index):
    hash = hash_function(cyclists[index].id) % bettern
    i=0
    while bettercyclists[hash].id != -1 and i<bettern:
        hash=(hash+1) % bettern
        i += 1
    if i == bettern: return
    bettercyclists[hash].id = cyclists[index].id
    bettercyclists[hash].nid = cyclists[index].nid
    bettercyclists[hash].pid = -1

def smallestGroup(cyclists,n):
    bettercyclists = [2*n]
    for i in range(2*n):
        bettercyclists[i] = Bettercyclist()
        bettercyclists[i].id = -1
    for i in range(n):
        add_to_hashtable(bettercyclists,cyclists,2*n,n,i)

    for i in range(n):
        index=hash_function(cyclists[i].id)
        bettercyclists[bettercyclists[index].nid].pid=bettercyclists[index].id

    smallestGroup = float("inf")
    for i in range(2*n):
        if bettercyclists[i].id != -1 and bettercyclists[i].pid == -1:    # pierwszy typ
            counter=1
            iter=i
            while bettercyclists[iter].nid != -1:
                iter = hash_function(bettercyclists[iter].nid)
                counter += 1
            if counter < smallestGroup:
                smallestGroup = counter
    return smallestGroup
