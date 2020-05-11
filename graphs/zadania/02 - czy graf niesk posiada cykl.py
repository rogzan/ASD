"""
Sprawdzanie czy graf nieskierowany posiada cykl.

"""

def rCycle(g,visited,parent,v):

    visited[v]=True
    for i in range(len(g)):
        if g[v][i]==1:
            if not visited[i]:
                parent[i]=v
                return rCycle(g,visited,parent,i)
            else:
                if i!=parent[v]:
                    return True
    return False


def cycle(g):
    n=len(g)
    visited=[False]*n
    parent=[-1]*n

    return rCycle(g,visited,parent,0)





if __name__=="__main__":
    g=[[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]]

    if cycle(g):
        print("yes")
    else:
        print("no")
