"""

DFS using adjacency list

"""

def DFSr(g,v,visited):
    visited[v]=True
    print(v)
    for i in g[v]:
        if visited[i]==False:
            DFSr(g,i,visited)

def DFS(g,v):
    
    visited=[False]*len(g)
    DFSr(g,v,visited)
    


if __name__=="__main__":

    g=[[1,3,4],[0,2],[1,3,4],[0,2,5],[0,2],[3]]
    DFS(g,0)
