# Given N machines. Each machine contains some numbers in sorted form. But the amount of numbers, 
# each machine has is not fixed. Output the numbers from all the machine in sorted non-decreasing form.
# Representation of stream of numbers on each machine is considered as linked list. 


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def addNode(head,val):
    if head==None:
        head.val=val
        head.next=None
        return head

    add=Node(val)
    add.next=head
    head=add
    return head

def printList(head):
    curr=head
    while curr:
        print(curr.val)
        curr=curr.next

def leftChild(i):
    return i*2

def rightChild(i):
    return i*2+1


def heapify(heap,i):

    l=leftChild(i)
    r=rightChild(i)

    m=i
    size=heap[0][0]

    if l<=size and heap[l][0]<heap[m][0]:
        m=l
    if r<=size and heap[r][0]<heap[m][0]:
        m=r

    if m != i:
        heap[i],heap[m]=heap[m],heap[i]
        heapify(heap,m)


def buildHeap(h):
    for i in range(h[0][0]//2,0,-1):
        heapify(h,i)


def sortMachines(heads):
    minheap=[]
    for i in range(len(heads)+1):
        minheap.append([0,0])

    minheap[0][0]=len(heads)
    for i in range(1,len(heads)+1):
        minheap[i][0]=heads[i-1].val
        minheap[i][1]=i

    buildHeap(minheap)

    result=[]

    while minheap[0][0]>0:

        result.append(minheap[1][0])
        h=heads[minheap[1][1]-1]
        h=h.next
        if h:
            heads[minheap[1][1]-1]=h
            minheap[1][0]=h.val
        else:
            minheap[1],minheap[minheap[0][0]]=minheap[minheap[0][0]],minheap[1]
            minheap[0][0]-=1

        buildHeap(minheap)

    return result



if __name__=="__main__":
    head1=Node(17)
    head1=addNode(head1,5)
    head1=addNode(head1,2)
    head1=addNode(head1,1)

    head2=Node(24)
    head2=addNode(head2,20)
    head2 = addNode(head2, 17)
    head2 = addNode(head2, 10)
    head2 = addNode(head2, 8)
    head2 = addNode(head2, 3)

    head3=Node(14)
    head3 = addNode(head3, 14)
    head3 = addNode(head3, 12)


    head4=Node(40)
    head4 = addNode(head4, 20)
    head4 = addNode(head4, 18)
    head4 = addNode(head4, 12)
    head4 = addNode(head4, 10)
    head4 = addNode(head4, 2)

    heads=[head1,head2,head3,head4]


    result=sortMachines(heads)
    print(result)
