"""
Proszę zaimplementować algorytm Dijkstry dla reprezentacji macierzowej grafu
"""


from queue import PriorityQueue


def relax(cost,parent,infinity,v,u,cvu):
    if infinity[u]:
        cost[u]=cost[v]+cvu
        parent[u]=v
        infinity[u]=False
        return True

    if cost[u]>cost[v]+cvu:
        cost[u]=cost[v]+cvu
        parent[u]=v
        return True
    return False


def dijkstra(G,s):
    q=PriorityQueue()
    n=len(G)
    cost=[-1]*n
    infinity=[True]*n
    parent=[None]*n

    cost[s]=0
    infinity[s]=False
    q.put((0,s))

    while not q.empty():
        c,v=q.get()
        for i in range(n):
            if G[v][i]:
                if relax(cost,parent,infinity,v,i,G[v][i]):
                    q.put((cost[i],i))

    print(cost)
    print(parent)


G = [[0, 4, 7, 2],
     [4, 0, 0, 0],
     [7, 0, 0, 2],
     [2, 0, 2, 0]]

dijkstra(G, 0)
