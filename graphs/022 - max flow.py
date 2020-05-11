"""
Maximum Flow Problem
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


def maxflow(g,s,t):
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


graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

print(maxflow(graph,0,5))
