
"""
Proszę zaimplementować funkcję, która na podstawie drzewa najkrótszych ścieżek (informacje w polach parent)
wypisuje najkrótszą ścieżkę ze źródła do zadanego wierzchołka.
"""



def printPath(v,parent):
    if parent[v]==None:
        print(v)
        return
    printPath(parent[v],parent)
    print(v)
