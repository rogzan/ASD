"""
Proszę zaimplementować algorytm Bellman'a-Ford'a dla reprezentacji macierzowej grafu.
"""


import sys

def printPath(v,parent):
    if parent[v]==None:
        print(v)
        return
    printPath(parent[v],parent)
    print(v)

def BellmanFord(s,g):
    n=len(g)
    dist=[sys.maxsize]*n
    parent=[None]*n
    dist[s]=0
    for i in range(n-1):
        for j in range(n):
            for k in range(n):
                if g[j][k]!=0 and dist[k]>dist[j]+g[j][k]:
                    dist[k]=dist[j]+g[j][k]
                    parent[k]=j

    for j in range(n):
        for k in range(n):
            if g[j][k]!=0 and dist[k] > dist[j] + g[j][k]:
                print("negative cycle")
                return
    print(dist)
    print(parent)
    printPath(6,parent)

if __name__=="__main__":
    g= [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0] ]

    BellmanFord(0,g)
