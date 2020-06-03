# Dana jest tablica:
# int n = ...int
# m = ...bool
# A[m][n]
# Gracz początkowo znajduje się na (zadanej) pozycji (x, y), dla której zachodziA[y][x] == true.
# Z danej pozycji wolno bezpośrednio przejść jedynie na pozycję, której dokładnie jedna współrzędna różni się o 1,
# oraz której wartość w tablicyAwynositrue. Proszę napisać programobliczający do ilu różnych pozycji
# może dojść gracz startując z zadanej pozycji (x, y).
# kolos 2013 - zad3

def check(tab,k, w,n,m):
    count = 0;
    for y in range(n):
        for x in range(m):
            if x + 1 < m and tab[x + 1][y] and tab[x][y]:
                union(tab[x][y], tab[x+1][y])
            if y+1 < n and tab[x][y+1] and tab[x][y]:
                union(tab[x][y+1],  tab[x][y])

    for y in range(n):
        for x in range(m):
            if find(tab[x][y]) == find(tab[k][w])):
                count++

    return count - 1
