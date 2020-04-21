def reverse(head):
    p=head
    curr=head.next
    prev=head
    while p.next:
        p=p.next
    prev.next=None
    while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return p
