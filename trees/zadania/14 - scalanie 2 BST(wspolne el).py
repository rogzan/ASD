# Funkcja scala 2 drzewa BST tak, ze drzewo wynikowe zawiera tylko elementy znajdujace sie na wejsciu w obu drzewach. */
class Node:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.parent = None

class Listnode:
    def __init__(self):
        self.node = None
        self.prev= None
        self.next = None

def list_to_tree (list, length):
    root=list.node
    ptr1 = Listnode()
    ptr2 = Listnode()
    counter=0
    while counter<length/2: ptr1 = ptr1.prev
    counter=0
    while counter<length/2: ptr2=ptr2.next
    root.left=list_to_tree(ptr1,length/2)
    root.right=list_to_tree(ptr2,length/2)
    return root
def tree_to_list(root):
    if root.parent==None:
        result = Listnode()
        result.prev=None
        result.next=None
        result.node=root
        previous=tree_to_list(root.left)
        previous.next=result
        result.prev=previous
        next=tree_to_list(root.right);
        next.prev=result
        result.next=next
        return result
    else:
        if root.left != None or root.right != None:
            newNode = Listnode()
            newNode.n=root
            if root.left!=None:
                previous=tree_to_list(root.left)
                previous.next=newNode
                newNode.prev=previous
            if root.right!=None:
                next = tree_to_list(root.right)
                next.prev=newNode
                newNode.next=next
            return newNode
        else:
            newNode = Listnode()
            newNode.node=root
            return newNode

def merge_lists(list1, list2, length):
    ptr1=list1;
    ptr2=list2;
    while ptr1.prev!=None: ptr1=ptr1.prev
    while ptr2.prev!=None: ptr2=ptr2.prev

    result=Listnode()
    ptr3=result
    while ptr1!=None and ptr2!=None:
        if ptr1.node.val==ptr2.node.val:
            ptr3.next=ptr1
            ptr1=ptr1.next
            ptr2=ptr2.next
            ptr3=ptr3.next
            length+=1
        else:
            if ptr1.Node.val < ptr2.Node.val: ptr1=ptr1.next
            else: ptr2=ptr2.next
    ptr3.next=None
    ptr3=result
    iter=0
    while iter<length/2:
        ptr3=ptr3.next
        iter+=1
    return ptr3

def merge_BST (root1, root2):
    list1=tree_to_list(root1);
    list2=tree_to_list(root2);
    length=0;
    list3=merge_lists(list1,list2,length);
    result=list_to_tree(list3,length);
    return result
