# Kol 2013/zad2
# Proszę opisać jak zmodyfikować drzewa czerwono-czarne (przechowujące elementy typuint) tak,by operacja
# int sum(T, x, y)obliczająca sumę elementów z drzewa o wartościach z przedziału [x, y] działała w czasieO(logn)
# (gdziento rozmiar drzewaT). Pozostałe operacjena powstałym drzewie powinny mieć złożoność taką samą jak w standardowym
# BST. (Podpowiedź: Warto w każdym węźle drzewa przechowywać pewną dodatkową informację, która
# upraszcza wykonanie operacjisumi którą można łatwo aktualizować).
# Program sumuje elementy w drzewie BST z przedzialu [x,y], korzystajac z zapisania w kazdym node'dzie informacji o sumach lewego i prawego poddrzewa. */
# uwaga x i y musza byc w drzewie dokladnie

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

def sum_x (root, x):
    sum=0
    ptr=root
    while ptr.val != x:
        if x < ptr.val:
            if ptr.right != None:
                sum += ptr.right.left_sum+ptr.right.val+ptr.right.right_sum
            sum += ptr.val
            ptr = ptr.left
        else:
            ptr = ptr.right
    if ptr.right!=None:
        sum += ptr.right.left_sum + ptr.right.val + ptr.right.right_sum
    sum += x;
    return sum
def sum_y (root, y):
    sum=0
    ptr=root
    while ptr.val != y:
        if y > ptr.val:
            if ptr.left != None:
                sum += ptr.left.left_sum+ptr.left.val+ptr.left.right_sum
            sum += ptr.val
            ptr = ptr.right
        else:
            ptr = ptr.left
    if ptr.left!=None:
        sum += ptr.left.left_sum + ptr.left.val + ptr.left.right_sum
    sum += y;
    return sum

def sum_between(root, x, y):
    if x==y: return x
    ptr=root
    while (ptr.val > x and ptr.val > y) or (ptr.val < x and ptr.val < y ):
        if ptr.val > x:
            ptr = ptr.left
        else:
            ptr = ptr.right
    result = 0
    if ptr.val != x:
        result += sum_x(ptr.left, x)
    else:
        result += x;
    if ptr.val != y:
        result += sum_y(ptr.right, y)
    else:
        result += y

    if ptr.val !=x and ptr.val != y:
        result += ptr.val
    return result

root = BNode()
root.val = 10
insert(root,4);
insert(root,1);
insert(root,7);
insert(root,15);
insert(root,12);
insert(root,20);

add_sums(root);

print(sum_between(root,7,20))  # włacznie i nie dawaj kurwa 0 bo jebnie
