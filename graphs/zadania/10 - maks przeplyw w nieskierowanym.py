"""
Proszę wskazać algorytm, który znajduje maksymalny przepływ między źródłem a ujściem w
grafie nieskierowanym. Proszę użyć algorytmu z wykładu - dla grafów skierowanych, gdzie
między każdą parą wierzchołków jesto najwyżej jedna krawędź - jako czarnej skrzynki.


Dla każdej krawędzi tworzę dodatkowy wierzchołek

"""

import sys

def BFS(g,s,t,parent):
    n=len(g)
    visited=[False]*n
    queue=[]
    queue.append(s)
    visited[s]=True

    while queue:

        s=queue.pop(0)

        for i in range(n):
            if not visited[i] and g[s][i]>0:
                queue.append(i)
                visited[i]=True
                parent[i]=s
    if visited[t]:
        return True
    return False


def convert_to_directed(g):
    #policzyć ile krawędzi, bo trzeba dodać połowę

    e=0
    n=len(g)
    for i in range(n):
        for j in range(n):
            if g[i][j]>0:
                e+=1
    new_n=int(n+e/2)
    ng=[None]*new_n
    for i in range(new_n):
        ng[i]=[0]*new_n

    for i in range(n):
        for j in range(i,n):
            ng[i][j]=g[i][j]
    e=n
    for i in range(n):
        for j in range(i,n):
            if g[j][i]>0:
                ng[j][e]=g[j][i]
                ng[e][i]=g[j][i]
                e+=1
    return ng

def maxflow(g,s,t):

    g=convert_to_directed(g)
    parent=[None]*len(g)
    max_flow=0

    while BFS(g,s,t,parent):
        path_flow=sys.maxsize
        k=t
        while k!=s:
            path_flow=min(path_flow,g[parent[k]][k])
            k=parent[k]
        max_flow+=path_flow

        v=t
        while v!=s:
            u=parent[v]
            g[u][v]-=path_flow
            g[v][u]+=path_flow
            v=parent[v]

    return max_flow


graph = [[0,8,7,5,0],
         [8,0,0,3,0],
         [7,0,0,5,4],
         [5,3,5,0,8],
         [0,0,4,8,0]]
print(maxflow(graph,0,4))
