"""
Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie wierzchołki w grafie, przez każdy dokładnie raz.
W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym. Proszę podać  algorytm, który stwierdzi
czy istnieje ścieżka Hamiltona w acyklicznym grafie skierowanym

Postortować topologicznie i sprawdzić czy pomiędzy każdymi dwoma istnieje krawędź
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

def Hamilton(g):
    a=top(g)
    for i in range(1,len(a)):
        if g[i-1][i]==0:
            return False
    return True

g=[[0,1,0,1,0],
   [0,0,0,1,0],
   [1,0,0,0,0],
   [0,0,0,0,0],
   [0,1,1,0,0]]

print(Hamilton(g))

G=[[0,1,1,1,0,0],
   [0,0,1,0,0,0],
   [0,0,0,1,1,0],
   [0,0,0,0,1,0],
   [1,0,0,0,0,1],
   [0,0,0,0,0,0]]
print(Hamilton(G))
