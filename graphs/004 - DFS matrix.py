"""

DFS using adjacency matrix

"""
def DFSr(g,v,visited):
    visited[v]=True
    print(v)

    for i in range(len(g)):
        if visited[i]==False and g[i][v]==1:
            DFSr(g,i,visited)


def DFS(g,v):
    visited=[False]*len(g)
    DFSr(g,v,visited)





if __name__=="__main__":

    g=[[0,1,0,1,1,0],[1,0,1,0,0,0],[0,1,0,1,1,0],[1,0,1,0,0,1],[1,0,1,0,0,0],[0,0,0,1,0,0]]
    DFS(g,0)
