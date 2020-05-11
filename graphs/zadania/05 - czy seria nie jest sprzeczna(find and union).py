"""
Dane jest n zmiennych x1, …, xn, o nieznanych wartościach. Mamy jednak podaną serię równości i różności,
postaci: xi=xj, xi!=xj.
Podaj jak najszybszy algorytm, który sprawdzi, czy podana tak seria nie jest sprzeczna.
"""

#najpierw dodaję wszyskie do setów, które mają równości; później sprawdzam różność elementóœ


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

def series(n,r):
    arr=[None]*n

    for i in range(n):
        arr[i]=make_set(i+1)

    for i,j,w in r:

        if w=="=":
            if arr[i-1].parent!=arr[j-1].parent:
                union(arr[i-1],arr[j-1])

    for i,j,w in r:
        if w=="!":
            if arr[i-1].parent==arr[j-1].parent:
                return False

    return True


r=[[1,3,"="],[4,3,"!"],[2,4,"="],[2,3,"="]]
if(series(4,r)):
    print("true")
else:
    print("false")
