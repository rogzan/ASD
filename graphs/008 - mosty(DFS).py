"""
Proszę zaimplementować algorytm DFS do znajdowania mostów w grafie. Proszę przyjąć reprezentację
przez listy sąsiedztwa.
"""
import sys
def mosty(G):
    n=len(G)
    time=[0]*n
    visited=[False]*n
    t=0
    parent=[None]*n
    low=[sys.maxsize]*n


    def DFS(G,v,visited,time,t,parent,low):
        visited[v]=True
        time[v]=t
        t+=1
        low[v]=min(low[v],time[v])
        for i in G[v]:
            if not visited[i]:
                parent[i]=v
                t=DFS(G,i,visited,time,t,parent,low)
                low[v]=min(low[i],low[v])
            elif parent[v]!=i:
                low[v]=min(low[v],time[i])
        return t

    for i in range(n):
        if not visited[i]:
            t=DFS(G,i,visited,time,t,parent,low)


    for i in range(n):
        if time[i]==low[i] and parent[i]!=None:
            print(parent[i],"->",i)



print("G:")
G=[[1,5],[0,2,5],[1,3,4],[2,4],[2,3],[0,1,6],[5]]
mosty(G)
print("s:")

s=[[1],[0,2],[1,3],[2],[5],[4,6],[5,7],[6]]
mosty(s)

