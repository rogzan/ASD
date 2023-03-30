"""
K 2015/2016 Zadanie 3

Dana jest klasa Node opisująca listę jednokierunkową. Proszę zaimplementwoać funckję fixSortedList(head), która
otrzymuje na wejściu listę jednokierunkową bez wartownika. Lista ta jest prawie posortowana w tym sensie, że
powstała z listy posortowanej przez zmianę jednego losowo wybranego elementu na losową wartość. Fukcja powinna
przepiąć elementy tak, by lista stała się posortowana i zwrócić wskaźnik do głowy tej listy. Można założyć, że wszystkie
liczby na liście są różne i że ta lista ma co najmniej dwa elementy. Funckja powinna  działać w czasie liniowym
względem długości listy wejściowej.


"""

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def addNode(head,val):
    add=Node(val)
    add.next=head
    head=add
    return head

def createAlmostSortedList():
    head=Node(30)
    head=addNode(head,28)
    head = addNode(head, 25)
    head = addNode(head, 22)
    head = addNode(head, 20)
    head = addNode(head, 19)
    head = addNode(head, 18)
    head = addNode(head, 16)
    head = addNode(head, 14)
    head = addNode(head, 12)
    head = addNode(head, 40)
    head = addNode(head, 8)
    head = addNode(head, 7)
    head = addNode(head, 6)
    head = addNode(head, 5)
    head = addNode(head, 4)
    head = addNode(head, 3)
    head = addNode(head, 2)
    head = addNode(head, 1)

    return head

def printList(head):
    pom=head
    while pom:
        print(pom.val)
        pom=pom.next
        
def fixSortedList(head):
    prev=head.next
    curr=head.next.next
    nfound = True
    diff=None
    while curr.next.next and nfound :
        if (curr.val>curr.next.val and curr.val>prev.val) or (curr.val<curr.next.val and curr.val<prev.val):
            diff=curr
            prev.next=curr.next
            nfound = False
        prev=curr
        curr=curr.next
    if not diff:
        if head.val>head.next.val:
            diff=head
            head=head.next
        elif curr.val>curr.next.val:
            diff=curr.next
            curr.next=None

    value=diff.val
    prev=None
    curr=head
    if head.val>value:
        diff.next=head
        head=diff
        return head
    while curr and curr.val < value:
        prev=curr
        curr=curr.next

    prev.next=diff
    diff.next=curr

    return head



if __name__=="__main__":
    head=createAlmostSortedList()
    head=fixSortedList(head)
    printList(head)
