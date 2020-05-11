"""
Proszę zaimplementować algorytm znajdujący cykl Eulera.
"""

def DFSr(g,v,cycle):


    for i in range(len(g)):
        if g[i][v]==1:
            g[i][v]=0
            g[v][i]=0
            DFSr(g,i,cycle)
    cycle.append(v)



def Euler(G):
    cycle=[]
    DFSr(G, 0,cycle)

    ans=[0]*len(cycle)
    j=0
    for i in range(len(cycle)-1,-1,-1):
        ans[j]=cycle[i]
        j+=1
    return ans


G=[[0,1,1,1,1,0],
   [1,0,1,0,0,0],
   [1,1,0,1,0,1],
   [1,0,1,0,0,0],
   [1,0,0,0,0,1],
   [0,0,1,0,1,0]]
print(Euler(G))
