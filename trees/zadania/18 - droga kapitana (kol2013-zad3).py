# Kapitan pewnego statku zastanawia się, czy może wpłynąć do portu mimo tego, że nastąpił odpływ.
# Do dyspozycji ma mapę zatoki w postaci tablicy:
# int n = ...
# int m = ...
# int A[m][n];
# gdzie wartośćA[y][x] to głębokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna
# wartość int T to statek może się tam znaleźć. Początkowo statek jest na pozycji (0,0) a port
# znajduje się na pozycji (n−1, m−1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie
# na pozycję bezpośrednio obok (to znaczy, na pozycję, której dokładnie jedna zewspółrzędnych różni się o jeden).
# Proszę napisać funkcję rozwiązującą problem kapitana
# kolos 2013 zad 3
class Node:
    def __init__(self):
        self.parent = None
        self.rank = None
        self.val = None

def make_set(val):
    x=Node()
    x.parent=x
    x.rank=0
    x.val=val # bool
    return x

def findSet(x):
    if x.parent!=x:
        y=findSet(x.parent)
        x.parent=y
        return y
    else:
        return x

def unionSet(x,y):
    Px = findSet(x)
    Py = findSet(y)
    if Py.rank < Px.rank:
        Py.parent = Px
        Px.rank+=Py.rank
    else:
        Px.parent = Py
        Py.rank+=Px.rank
        if Px.rank == Py.rank and Px.rank==0 and Py.rank==0:
            Px.rank=2

def pathCount(A, n, m, x, y):
    S = [[ None for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for i in range(m):
            S[i][j]=make_set(A[i][j])

    for i in range(n):
        for j in range(m):
            if A[i][j]==True:
                if i+1<m and A[i+1][j]==True:
                    unionSet(S[i][j],S[i+1][j])
                if j+1<n and A[i][j+1]==True:
                    unionSet(S[i][j],S[i][j+1])
    res=findSet(S[x][y])
    return res.rank
