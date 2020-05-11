#Domknięciem przechodnim skierowanego grafuG= (V, E) nazywamy taki grafG′= (V, E′), że dla każdychdwóch wierzchołków
#v∈VgrafG′ma krawędź zu do v wtedy i tylko wtedy, gdy wG jest skierowana ścieżka z u do v. Proszę zaimplementować funkcję
#tclosure( G ), która na wejście otrzymuje graf skierowanyw reprezentacji macierzowej (bez wag);
#G[i][j] to wartość logiczna mówiąca czy istnieje krawędź zidoj) izwraca graf będący domknięciem przechodnim G(w tej samej reprezentacji).

def tclosure( G ):     # korzystam ze zmodyfikowanego algorytmu Floyda Warshalla
    n = len(G)
    s = [i[:] for i in G]      # macierz wynikowa
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if s[i][j] == False:
                    s[i][j] = (s[i][k] and s[k][j])    #jeśli wierzchołek k jest na ścieżce z i do j i isteją krawędzie(i,k) i (k,j)
    return s

G = [ [False, True , False],[False, False, True ],[False, False, False] ]
print( tclosure( G ) )
