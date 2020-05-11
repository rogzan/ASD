from queue import PriorityQueue
import sys

class MyPriorityQueue(PriorityQueue): #aby możliwe było ustalanie priorytetu wzgledem drugiej wartosci
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item


def dijkstra(G, s):
    Q = MyPriorityQueue()
    n=len(g)
    dist=[sys.maxsize]*n
    for i in range(n):
        if(i!=s):
            Q.put(i, dist[i])
    parent=[None]*n
    dist[s]=0
    Q.put(s,0)
    while Q.empty() ==  False:
        for i in range(n):
            u = Q.get()
            for k in range(len(g[i])):
                p = g[i][k][0]
                if dist[p] > dist[u] + g[u][k][1]:
                    dist[p] = dist[u] + g[u][k][1]
                    parent[p] = u
    return parent


G = [[(1,0), (2,1)],[(3,1), (2,0)],[(3,0)],[]]
print(dijkstra(G, 0))
