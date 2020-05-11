"""

BFS using adjacency matrix

"""


def BFT(g,f):

    visited=[False]*len(g)
    queue=[]

    queue.append(f)
    visited[f]=True

    while queue:
        s=queue.pop(0)
        print(s)

        for i in range(s,len(g)):
            if visited[i]==False and g[s][i]==1:
                queue.append(i)
                visited[i]=True






if __name__=="__main__":

    g=[[0,1,0,1,1,],[1,0,1,0,0,],[0,1,0,1,1],[1,0,1,0,0],[1,0,1,0,0]]
    BFT(g,0)
