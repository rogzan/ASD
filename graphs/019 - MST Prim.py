
"""
Proszę zaimplementować algorytm Prima
"""

from queue import PriorityQueue
import sys

def Prim(g):
    n=len(g)
    parent=[None]*n
    dist=[sys.maxsize]*n
    dist[0]=0
    q=PriorityQueue()
    q.put((0,0))
    taken=[False]*n
    taken[0]=True

    while not q.empty():
        d,u=q.get()
        taken[u]=True
        if d==dist[u]:
            for i in range(n):
                if g[u][i]!=0 and dist[i]>g[u][i] and taken[i]==False:
                    parent[i]=u
                    dist[i]=g[u][i]
                    q.put((g[u][i],i))
    print(parent)

print("g:")
g=[[0,5,0,2,0],
   [5,0,7,0,1],
   [0,0,0,3,0],
   [2,7,3,0,2],
   [0,1,0,2,0]]

Prim(g)

print("G:")
G=[[0,5,0,1,0,2],
   [5,0,0,0,7,0],
   [0,0,0,4,0,8],
   [1,0,4,0,0,3],
   [0,7,0,0,0,0],
   [2,0,8,3,0,0]]
Prim(G)
