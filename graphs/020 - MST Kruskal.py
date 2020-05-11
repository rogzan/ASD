"""
Proszę zaimplementować algorytm Kruskala
"""


def quickSort(arr,left,right):
    if left<right:
        pi=partition(arr,left,right)
        quickSort(arr,left,pi-1)
        quickSort(arr,pi+1,right)

def partition(arr,left,right):
    i=left-1
    pivot=arr[right][2]
    for j in range(left,right):
        if arr[j][2]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]
    return i+1


class Node:
    def __init__(self,id):
        self.id=id
        self.parent=self
        self.rank=0

def find_set(x):
    if x!=x.parent:
        x.parent=find_set(x.parent)
    return x.parent

def union(x,y):
    x=find_set(x)
    y=find_set(y)
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1

def make_set(v):
    return Node(v)

def Kruskal(g,v):       #v to liczba wierzchołków
    n=len(g)
    quickSort(g,0,n-1)
    A=[]
    V=[]
    for i in range(v):
        V.append(make_set(i))

    for i in range(n):
        u=g[i][0]
        v=g[i][1]
        if find_set(V[u])!=find_set(V[v]):
            A.append(g[i])
            union(V[u],V[v])

    print(A)





g=[[0,1,5],[0,3,2],[1,0,5],[1,4,1],[1,3,7],[2,3,3],[3,2,3],[3,0,2],[3,4,2],[4,1,1],[4,3,2],[3,1,7]]


Kruskal(g,5)


G=[[0,1,5],[0,3,1],[0,5,2],[1,4,7],[2,3,4],[2,5,8],[3,5,3]]
Kruskal(G,6)
