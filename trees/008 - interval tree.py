class ITNode:
    def __init__(self):
        self.max=0
        self.left=None
        self.right=None
        self.low=None
        self.high=None
        self.intervals=[]

def insert(root,i): # do budowania

    n=ITNode()
    n.intervals=i
    n.low=i[0]
    n.high=i[1]
    n.max=i[1]
    return n



def insert_new(root,i): #wstawianie pojedynczego przedziału do IT
    if root==None:
        n=ITNode()
        n.intervals=i
        n.low=i[0]
        n.high=i[1]
        n.max=i[1]
        return n

    l=root.low
    if i[0]<l:
        root.left=insert(root.left,i)
    else:
        root.right=insert(root.right,i)

    if root.max<i[1]:
        root.max=i[1]

    return root

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.intervals)
    inorder(root.right)

def overlap(i1,i2):
    if i1[0]<=i2[1] and i2[0]<=i1[1]:
        return True
    return False

def overlapSearch(root,i): #z czym się nakłada; wypisuje wszystkie
    if root==None:
        return None
    if overlap(root.intervals,i):
        print(root.intervals)
    if root.left!=None and root.left.max>=i[0]:
        return overlapSearch(root.left,i)
    return overlapSearch(root.right,i)

def f(root,intervals,p,k):
    if p<=k:
        m=(p+k)//2
        root=insert(root,intervals[m])
        root.left=f(root.left,intervals,p,m-1)
        root.right=f(root.right,intervals,m+1,k)
    return root
def build(intervals):
    root=None
    intervals=sorted(intervals)
    m=len(intervals)-1
    root=f(root,intervals,0,m)
    return root



intervals=[(3,4),(2,5),(4,7),(2,7),(5,9),(1,4),(1,6),(3,6)]
IT=build(intervals)
print("left:")
print(IT.left.intervals)
print("right:")
print(IT.right.intervals)
print(IT.right.right.intervals)
print("")
inorder(IT)
print("")
overlapSearch(IT,(2,3))
