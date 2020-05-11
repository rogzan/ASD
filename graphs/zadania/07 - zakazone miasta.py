
"""
Królestwo Syjonu składa się z miast połączonych dwukierunkowymi drogami. Między dowolną parą miast istnieje jedna
i tylko jedna ścieżka. Część miast została zainfekowana przez maszyny. Do eskalacji ataku dojdzie,
jeśli znajdą się przynajmniej dwa miasta, zainfekowane przez maszyny, między którymi będzie istniała ścieżka.
Dlatego Mofreusz postanowił zniszczyć część dróg między miastami, tak aby żadne zainfekowane miasta nie były połączone.
Niemniej jednak każda droga ma przypisany czas potrzebny na zniszczenie. Pomóż Morefuszowi tak dobrać niszczone
drogi, aby nie instniała ścieżka między dowolnymi zainfekowanymi miastami i czas potrzebny na niszczenie był
minimalny. Niszczymy jedną drogę na raz.

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

def infection(g,n,inf):
    destroy=[]
    quickSort(g,0,len(g)-1)

    vertices=[None]*n
    for i in range(n):
        vertices[i]=make_set(i)
    for u,v,w in g:
        pu=vertices[u].parent
        pv=vertices[v].parent
        if pu!=pv:
            if inf[u] and inf[v]:
                destroy.append((u,v))
            elif inf[u] or inf[v]:
                union(vertices[u],vertices[v])
                inf[u]=True
                inf[v]=True
    print(destroy)


g=[[0,1,8],[1,2,4],[0,2,5],[2,3,7],[0,3,2]]
i=[True,False,True,True]
infection(g,4,i)


G=[[0,1,5],[0,3,1],[0,5,2],[1,4,7],[2,3,4],[2,5,8],[3,5,3]]
i=[True,False,False,True,True,False] #infected
infection(G,6,i)
