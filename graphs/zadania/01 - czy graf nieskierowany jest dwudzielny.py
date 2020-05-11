"""
Sprawdzanie czy graf nieskierowany jest dwudzielny (czy da się podzielić jego wierzchołki na dwa zbiory, takie że
krawędzie łączą jedynie wierzchołki z różnych zbiorów).

"""


def dwudzielny(g,v):
    queue=[]
    n=len(g)
    colours=[-1]*n
    colours[v]=True
    queue.append(v)
    visited=[False]*n
    visited[v]=True

    while queue:
        u=queue.pop(0)
        visited[u]=True

        for i in range(n):
            if g[u][i]==1:
                if not visited[i]:
                    colours[i]=not colours[u]
                    queue.append(i)
                elif colours[i]==colours[u]:
                    return False
    return True



if __name__=="__main__":
    g=[[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]

    if dwudzielny(g,0):
        print("yes")
    else:
        print("no")

