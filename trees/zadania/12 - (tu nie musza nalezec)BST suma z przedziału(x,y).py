# suma w bst miedzy [x,y] wartosciami x i y nie musza nalezec do drzewska

class BNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.val = None
        self.left_sum = None
        self.right_sum = None

def insert(root,val):
    while root!=None:
        if root.val < val:
            prev=root
            root=root.right
        else:
            prev=root
            root=root.left
    new = BNode()
    new.val = val
    if prev.val < val:
        prev.right=new
        new.parent=prev
    else:
        prev.left=new
        new.parent = prev

def add_sums(root):
    if (root==None): return
    if (root.left==None): root.left_sum=0
    if (root.right==None): root.right_sum=0;
    if (root.left!=None):
        add_sums(root.left)
        root.left_sum = root.left.left_sum + root.left.val + root.left.right_sum
    if (root.right!=None):
        add_sums(root.right)
        root.right_sum = root.right.left_sum + root.right.val + root.right.right_sum

def sum(root, x, y):
    sum = root.left_sum + root.right_sum + root.val
    idx = root
    while idx!= None:
        if x < idx.val:
            idx = idx.left
        elif x > idx.val:
            sum -= idx.val + idx.left_sum
            idx = idx.right
        else:
            sum -= idx.left_sum
            break
    idx = root
    while idx!= None:
        if y < idx.val:
            sum -= idx.val + idx.right_sum
            idx = idx.left
        elif y > idx.val:
            idx = idx.right
        else:
            sum -= idx.right_sum
            break
    return sum

root = BNode()
root.val = 10
insert(root,4);
insert(root,1);
insert(root,7);
insert(root,15);
insert(root,12);
insert(root,20);

add_sums(root);

print(sum(root,3,12), "chuj dupa i kamieni kupa")
