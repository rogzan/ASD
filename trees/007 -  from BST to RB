"""
Podaj algorytm, który mając na wejściu niezrównoważone drzewo BST
przekształca je w drzewa dające się pokolorować jako czerwono-czarne.


Wpisujemy do tablicy zawartość drzewa, w porządku inorder. Otrzymujemy posortowaną tablicę.
Teraz mamy rekurencyjną funkcję, która tworzy BST. Bierzemy medianę z tablicy,
robimy z niej korzeń i teraz rekurencyjne wywołanie na lewo i prawo od mediany.
Otrzymane drzewo jest idealnie zrównoważone, więc na pewno jest i RB i AVL.

"""
class BSTNode:
    def __init__(self):
        self.key=None
        self.value=None
        self.parent=None
        self.left=None
        self.right=None


    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def find(root,key):
    while root!=None:
        if root.key==key:
            return root
        elif root.key<key:
            root=root.right
        else:
            root=root.left
    return None

def insert(root,key,value):
    while root!=None:
        if root.key<key:
            prev=root
            root=root.right
        else:
            prev=root
            root=root.left
    new = BSTNode()
    new.key = key
    new.value = value
    if prev.key<key:
        prev.right=new
        new.parent=prev
    else:
        prev.left=new
        new.parent = prev

def inorder(root,arr):
    if root.left:
        inorder(root.left,arr)
    arr.append([root.key, root.value])
    if root.right:
        inorder(root.right,arr)
        
def RB(arr,p,k):
    if p<k:
        a=(k+p)//2
        nroot = BSTNode()
        nroot.value = arr[a][1]
        nroot.key = arr[a][0]
        nroot.left=RB(arr,p,a-1)
        nroot.right=RB(arr,a+1,k)
        return nroot
    if p==k:
        a = p
        nroot = BSTNode()
        nroot.value = arr[a][1]
        nroot.key = arr[a][0]
        nroot.left = RB(arr, p, a - 1)
        return nroot
    return None



def toRB(root):
    arr=[]
    inorder(root,arr)
    nroot=RB(arr,0,len(arr)-1)
    return nroot

root=BSTNode()
root.key=9
root.value=11
insert(root,15,11)
insert(root,6,11)
insert(root,10,11)
insert(root,3,11)
insert(root,7,11)
insert(root,8,11)
insert(root,2,11)
insert(root,4,11)
insert(root,1,11)
insert(root,20,11)

root.display()
print("")
toRB(root).display()
