"""
Dany jest graf ważony  G, oraz drzewo rozpinające T, które być może jest drzewem najkrótszych ścieżek w G,
od pewnego wierzchołka s z G. Podaj algorytm, który sprawdzi, czy T rzeczywiście jest drzewem najkrótszych ścieżek
od wierzchołka s.

Rozwiązanie:
przejść po wszystkich krawędziach i sprawdzić czy da się zrelaksować
złożoność o(E)
"""
import sys

def check(G,T,src):
    n=len(G)
    dist=[sys.maxsize]*n
    dist[src]=0
    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j] in G[src]:
                dist[T[i][j][0]]=T[i][j][1]
            else:
                dist[T[i][j][0]]=dist[i]+T[i][j][1]
    print(dist)
    for j in range(n):
        for k in range(len(G[j])):
            s=G[j][k][0]
            w=G[j][k][1]
            if dist[s] > dist[j] + w:
                print("T nie jest drzewem najkrótszych ścieżek")
                return

    print("T jest drzewem najkrótszych ścieżek")


G=[[(1,2),(2,3),(4,2)],
   [(3,1),(2,4)],
   [(3,2)],
   [],
   [(3,2)]]

T=[[(1,2),(2,3),(4,2)],
   [(3,1)],[],[],[]]

check(G,T,0)
