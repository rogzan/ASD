import sys

def parent(i):
    return i//2

def leftChild(i):
    return i*2

def rightChild(i):
    return i*2+1


def heapify(heap,i):

    l=leftChild(i)
    r=rightChild(i)

    m=i
    size=heap[0]

    if l<=size and heap[l]>heap[m]:
        m=l
    if r<=size and heap[r]>heap[m]:
        m=r

    if m != i:
        heap[i],heap[m]=heap[m],heap[i]
        heapify(heap,m)


def buildHeap(h):
    for i in range(h[0]//2,0,-1):
        heapify(h,i)


def extractMax(heap):
    size = heap[0]
    if size<1:
        sys.exit()
    m=heap[1]
    heap[1]=heap[size]
    heap[0]-=1
    heapify(heap,1)
    return m

def increaseKey(heap,i,key):
    if heap[i]>key:
        print("new key is smaller than current key")
        sys.exit()

    heap[i]=key

    while i>1 and heap[parent(i)]<heap[i]:
        heap[i],heap[parent(i)]=heap[parent(i)],heap[i]
        i=parent(i)

def insert(heap,key):

    if heap[0]==len(heap)-1:
        sys.exit()

    heap[0]+=1
    heap[heap[0]]=key
    i=heap[0]

    while i>1 and heap[i]>heap[parent(i)]:
        heap[i],heap[parent(i)]=heap[parent(i)],heap[i]
        i=parent(i)

def delete(heap,i):

    size=heap[0]
    heap[i],heap[size]=heap[size],heap[i]
    heap[0]-=1
    
    while i>1 and heap[i]>heap[parent(i)]:
        heap[i],heap[parent(i)]=heap[parent(i)],heap[i]
        i=parent(i)
