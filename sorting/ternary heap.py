def parent(i):
    return (i+1)//3

def leftChild(i):
    return i*3-1

def middleChild(i):
    return i*3

def rightChild(i):
    return i*3+1

def heapify3(heap,i):
    l=leftChild(i)
    m=middleChild(i)
    r=rightChild(i)
    size=heap[0]
    mx=i
    if l<=size and heap[l]>heap[mx]:
        mx=l
    if m<=size and heap[m]>heap[mx]:
        mx=m
    if r<=size and heap[r]>heap[mx]:
        mx=r

    if mx != i:
        heap[i],heap[mx]=heap[mx],heap[i]
        heapify3(heap,mx)


def buildHeap(heap):
    for i in range((len(heap)*2)//3,0,-1):
        heapify3(heap,i)

def insert(heap,key):

    heap[0]+=1
    heap[heap[0]]=key
    i=heap[0]

    while i>1 and heap[i]>heap[parent(i)]:
        heap[i],heap[parent(i)]=heap[parent(i)],heap[i]
        i=parent(i)
