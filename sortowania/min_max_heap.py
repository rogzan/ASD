def parent(i):
    return i//2

def leftChild(i):
    return i*2

def rightChild(i):
    return i*2+1

def level(i):
    if i==1:
        return 1
    else:
        return 1+level(parent(i))
#odd level - min values
#even level - max values

def heapify(heap,i):

    if level(i)%2==0:
        heapifyMIN(heap,i)
    else:
        heapifyMAX(heap,i)


def heapifyMIN(heap,i):
    mn1=i
    l=leftChild(i)
    r=rightChild(i)
    size=heap[0]
    if l<=size and heap[l]<heap[mn1]:
        mn1=l
    if r<=size and heap[r]<heap[mn1]:
        mn1=r
    ll=leftChild(leftChild(i))
    lr=leftChild(rightChild(i))
    rr=rightChild(rightChild(i))
    rl=rightChild(rightChild(i))
    grandChildren=[ll,lr,rr,rl]
    mn2=i
    for j in range(len(grandChildren)):
        if grandChildren[j]<=size and heap[grandChildren[j]]<heap[mn2]:
            mn2=grandChildren[j]

    if heap[mn2]<heap[mn1]:
        heap[mn2],heap[i]=heap[i],heap[mn2]
        if heap[mn2]>heap[parent(mn2)]:
            heap[mn2],heap[parent(mn2)]=heap[parent(mn2)],heap[mn2]
        heapifyMIN(heap,mn2)
    else:
        if mn1 != i:
            heap[mn1],heap[i]=heap[i],heap[mn1]

def heapifyMAX(heap,i):
    mx1 = i
    l = leftChild(i)
    r = rightChild(i)
    size = heap[0]
    if l <= size and heap[l] > heap[mx1]:
        mn1 = l
    if r <= size and heap[r] > heap[mx1]:
        mx1 = r
    ll = leftChild(leftChild(i))
    lr = leftChild(rightChild(i))
    rr = rightChild(rightChild(i))
    rl = rightChild(rightChild(i))
    grandChildren = [ll, lr, rr, rl]
    mx2 = i
    for j in range(len(grandChildren)):
        if grandChildren[j] <= size and heap[grandChildren[j]] > heap[mx2]:
            mx2 = grandChildren[j]

    if heap[mx2] > heap[mx1]:
        heap[mx2], heap[i] = heap[i], heap[mx2]
        if heap[mx2] < heap[parent(mx2)]:
            heap[mx2], heap[parent(mx2)] = heap[parent(mx2)], heap[mx2]
        heapifyMAX(heap, mx2)
    else:
        if mx1 != i:
            heap[mx1], heap[i] = heap[i], heap[mx1]


def buildHeap(heap):
    for i in range(len(heap)//2,0,-1):
        heapify(heap,i)
