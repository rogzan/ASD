"""
Proszę zaimplementować algorytm sortowania topologicznego.
"""

def DFSr(g,v,visited,sort):
    visited[v]=True

    for i in range(len(g)):
        if visited[i]==False and g[v][i]==1:
            DFSr(g,i,visited,sort)
    sort.append(v)

def top(g):
    n=len(g)
    sort=[]
    visited=[False]*n
    for i in range(n):
        if not visited[i]:
            DFSr(g,i,visited,sort)
    rev=[0]*len(sort)
    j=n-1

    for i in range(n):
        rev[i]=sort[j]
        j-=1
    return rev

g=[[0,1,0,1,0],
   [0,0,0,1,0],
   [1,0,0,0,0],
   [0,0,0,0,0],
   [0,1,1,0,0]]

print(top(g))
