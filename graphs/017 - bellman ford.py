"""
Single source shortest path - Bellman Ford algorithm

"""

import sys


def BellmanFord(edges, v, src):

    dist=[sys.maxsize]*v
    dist[src]=0

    for i in range(v-1):

        for e in range(len(edges)):

            if dist[edges[e][1]]>dist[edges[e][0]]+edges[e][2]:
                dist[edges[e][1]]=dist[edges[e][0]]+edges[e][2]

    for e in range(len(edges)):

        if dist[edges[e][1]] > dist[edges[e][0]] + edges[e][2]:
            print("Graph contain negative weight cycle")
            return

    return dist




if __name__=="__main__":
    edges=[[0,1,2],[0,4,3],[1,4,-4],[2,1,5],[0,3,-1],[3,2,2],[3,4,3],[4,2,1]]
    print(BellmanFord(edges,5,0))
