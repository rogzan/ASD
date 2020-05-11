"""
Mówimy, że wierzchołek t w grafie skierowanym jest uniweralnym ujściem, jeśli z każdego innego wierzchołka v istnieje
krawędź z v do t, oraz nie istnieje żadna krawędź wychodząca z t. Proszę napisać algorym znajdujący ujście (jeśli istnieje)
przy macierzowej reprezentacji grafu.
"""

def universalSink(g):
    i=0
    j=0
    n=len(g)
    while i<n and j<n:
        if g[i][j]==1:
            i+=1
        else:
            j+=1

    if j==n-1:
        return -1

    for k in range(n):
        if g[i][k]!=0:
            return -1
        if g[k][i]!=1 and i!=k:
            return -1

    return i




if __name__=="__main__":
    g=[[0,1,0,1,0,1],[0,0,0,1,0,0],[1,0,0,1,0,0],[0,1,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0]]

    print(universalSink(g))
