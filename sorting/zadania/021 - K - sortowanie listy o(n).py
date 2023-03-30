"""
K 2016/2017 Zadanie 1

Dana jest struktura opisująca listę jednokierunkową dla liczb rzeczywistych.
Proszę zaimplementwoać funckję Sort(list), która otrzymuje na wejściu listę liczb rzeczywistych
(z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na przedziale [0,10) i sortuje jej zawartość
w kolejności niemalejącej. Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność.


"""


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insertNode(head,val):
    if head==None:
        head=Node(val)
    else:
        added=Node(val)
        added.next=head
        head=added
    return head

def printList(head):
    current=head
    while current != None:
        print(current.data)
        current=current.next

def insertSort(arr):

    for i in range(1,len(arr)):
        key=arr[i].data
        j=i-1
        while j>=0 and key<arr[j].data:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1].data=key


def Sort(head,n):

    buckets=[None]*n
    for i in range(n):
        buckets[i]=[]
    pom=head.next
    mx=10
    while pom:
        num=pom.data/mx
        b_idx=int(n*num)
        buckets[b_idx].append(Node(pom.data))
        pom=pom.next

    for i in range(n):
        insertSort(buckets[i])

    head=Node(None)
    prev=head
    for i in range(n):
        for j in range(len(buckets[i])):
            add=buckets[i][j]
            prev.next=add
            prev=add

    return head







head=Node(1)
head=insertNode(head,4)
head=insertNode(head,9)
head=insertNode(head,5)
head=insertNode(head,3)
head=insertNode(head,8)
head=insertNode(head,4)
head=insertNode(head,5)
head=insertNode(head,4)
head=insertNode(head,9)
head=insertNode(head,5)
head=insertNode(head,3)
head=insertNode(head,8)
head=insertNode(head,4)
head=insertNode(head,5)
head=insertNode(head,4)
head=insertNode(head,9)
head=insertNode(head,5)
head=insertNode(head,3)
head=insertNode(head,8)
head=insertNode(head,4)
head=insertNode(head,5)
head=insertNode(head,1)
head=insertNode(head,2)
head=insertNode(head,1)
head=insertNode(head,2)
head=insertNode(head,1)
head=insertNode(head,1)
head=insertNode(head,1)
head=insertNode(head,9)
head=insertNode(head,5)
head=insertNode(head,3)
head=insertNode(head,8)
head=insertNode(head,6)
head=insertNode(head,7)
head=insertNode(head,6)
head=insertNode(head,7)
head=insertNode(head,6)
head=insertNode(head,8)
head=insertNode(head,4)
head=insertNode(head,5)


printList(head)
print("NOWA:")
head=Sort(head,10)
printList(head)
