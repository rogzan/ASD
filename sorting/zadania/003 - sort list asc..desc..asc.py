#Sort a linked list that is sorted alternating ascending and descending orders

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

def reverse(head):

    last=head
    while last.next:
        last=last.next

    curr=head
    prev=None

    while curr!=last:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next

    last.next=prev

    return last


def merge(head1,head2):

    if head1.val<head2.val:
        head=Node(head1.val)
        head1=head1.next
    else:
        head=Node(head2.val)
        head2=head2.next

    curr=head
    while head1 and head2:
        if head1.val<head2.val:
            add=Node(head1.val)
            head1=head1.next
            curr.next=add
            curr=curr.next
        else:
            add=Node(head2.val)
            head2=head2.next
            curr.next=add
            curr=curr.next

    while head1:
        add = Node(head1.val)
        head1 = head1.next
        curr.next = add
        curr = curr.next

    while head2:
        add = Node(head2.val)
        head2 = head2.next
        curr.next = add
        curr = curr.next


    return head





def sort(head):

    head1=head
    head2=head.next

    prev1=head1
    curr1=None
    prev2=head2
    curr2=None
    i=0

    h=head.next.next

    while h:
        if i%2==0:
            curr1=h
            prev1.next=curr1
            prev1=h
        else:
            curr2=h
            prev2.next=curr2
            prev2=h

        h=h.next
        i+=1
    prev1.next=None
    prev2.next=None

    head2=reverse(head2)

    head=merge(head1,head2)

    return head



if __name__=="__main__":
    head = Node(1)
    head = addNode(head,20)
    head = addNode(head, 6)
    head = addNode(head, 15)
    head = addNode(head, 7)
    head = addNode(head, 11)
    head = addNode(head, 8)
    head = addNode(head, 8)
    head = addNode(head, 12)
    head = addNode(head, 6)
    head = addNode(head, 17)
    head = addNode(head, 2)

    printList(head)
    head=sort(head)
    print("sorted")
