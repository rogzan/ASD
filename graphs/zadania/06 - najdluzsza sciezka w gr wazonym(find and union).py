"""
Dany jest graf ważony. Wagę ścieżki definujemy jako min(z wag krawędzi na tej ścieżce)
znaleźć najdłuższą ścieżkę między wierzchołkami s i t.


Sortujemy po malejąco po wadze i łaczymy w set te wierzchołki, które łączy dana krawędź dopóki w s i t nie będą w 
jednym secie.
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
        if arr[j][2]>=pivot:
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

def maxPath(g,n,s,t):
    vertices=[None]*n
    ans=[]
    for i in range(n):
        vertices[i]=make_set(i)
    quickSort(g,0,len(g)-1)

    for u,v,w in g:

        union(vertices[u],vertices[v])
        ans.append((u,v))
        if vertices[s].parent==vertices[t].parent:
            print(ans)
            print(w)
            return


g=[[0,1,5],[0,3,2],[1,0,5],[1,4,1],[1,3,7],[2,3,3],[3,2,3],[3,0,2],[3,4,2],[4,1,1],[4,3,2],[3,1,7]]


maxPath(g,5,1,4)


G=[[0,1,5],[0,3,1],[0,5,2],[1,4,7],[2,3,4],[2,5,8],[3,5,3]]
maxPath(G,6,3,5)
