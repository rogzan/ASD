"""
Proszę zaimplementować algorytm znajdujący silnie spójne składowe w grafie.
"""


def DFSprint(g,v,visited):
    visited[v]=True
    print(v,end=" ")
    for i in range(len(g)):
        if visited[i]==False and g[v][i]==2:
            DFSprint(g,i,visited)


def DFSr(g,v,visited,stack):
    visited[v]=True

    for i in range(len(g)):
        if visited[i]==False and g[v][i]==1:
            DFSr(g,i,visited,stack)
    stack.append(v)
def ssp(g):
    n=len(g)
    stack=[]
    visited=[False]*n
    for i in range(n):
        if not visited[i]:
            DFSr(g,i,visited,stack)
    for i in range(n):
        for j in range(n):
            if i!=j and g[i][j]==1:
                g[i][j]=0
                g[j][i]=2

    for i in range(n):
        visited[i]=False

    idx=[0]*n
    for i in range(n):
        idx[i]=i


    for i in range(n-1,-1,-1):
        if not visited[stack[i]]:
            DFSprint(g,stack[i],visited)
            print("")

print("g:")
g=[[0,1,0,1,0],
   [0,0,0,1,0],
   [1,0,0,0,0],
   [0,0,0,0,0],
   [0,1,1,0,0]]

ssp(g)

print("G:")
G=[[0,1,0,0,0,0],
   [0,0,1,1,0,0],
   [1,0,0,0,0,0],
   [0,0,0,0,0,1],
   [0,0,0,1,0,0],
   [0,0,0,0,1,0]]
ssp(G)
