"""

Chceck whether a given graph is bipartite

"""

def bipartite(g,v):

    colours=[-1]*len(g)

    colours[v]=1
    queue=[]
    queue.append(v)

    while queue:
        u=queue.pop(0)

        if g[u][u]==1: #if loop
            return False

        for i in range(len(g)):
            if g[i][u]==1 and colours[i]==-1:
                colours[i]=1-colours[u]
                queue.append(i)

            elif g[i][u]==1 and colours[i]==colours[u]:
                return False

    return True



if __name__=="__main__":

    g=[[0,1,0,1,1,0],[1,0,1,0,0,0],[0,1,0,1,1,0],[1,0,1,0,0,1],[1,0,1,0,0,0],[0,0,0,1,0,0]]
    if(bipartite(g,0)):
        print("yes")
    else:
        print("no")
