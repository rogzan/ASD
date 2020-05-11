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
            for k in range(len(g[j])):
                p=g[j][k][0]
                if dist[p]>dist[j]+g[j][k][1]:
                    dist[p]=dist[j]+g[j][k][1]
                    parent[p]=j

    for j in range(n):
        for k in range(len(g[j])):
            p = g[j][k][0]
            if dist[p] > dist[j] + g[j][k][1]:
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

    G=[[(1,4),(7,8)],
       [(2,8),(7,11),(0,4)],
       [(1,8),(8,2),(5,4),(3,7)],
       [(2,7),(4,9),(5,14)],
       [(3,9),(5,10)],
       [(2,4),(3,14),(4,10),(6,2)],
       [(5,2),(7,1),(8,6)],
       [(0,8),(1,11),(6,1),(8,7)],
       [(2,2),(6,6),(7,7)]]

    BellmanFord(0,G)
