"""

BFS using adjacency list

"""

def BFS(g,f):

    visited=[False]*len(g)

    queue=[]
    queue.append(f)
    visited[f]=True

    while queue:

        s=queue.pop(0)
        print(s)

        for i in g[s]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True






if __name__=="__main__":

    g=[[1,3,4],[0,2],[1,3,4],[0,2,5],[0,2],[3]]
    BFS(g,0)
