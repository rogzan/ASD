"""
Rozważmy drzewa BST, które dodatkowo w każdym węźle zawierają pole z liczbą węzłów w danym poddrzewie. Proszę opisać
jak w takim drzewie wykonać następujące operacje:
    1. znalezienie i-tego co do wielkości elementu
    2. wyznaczenie, którym co do wielkości w drzewie jest zadany węzeł

Proszę zaimplementować obie opreacje.

"""
class BSTNode:
    def __init__(self):
        self.key=None
        self.value=None
        self.parent=None
        self.left=None
        self.right=None
        self.leftnodes=0
        self.rightnodes=0

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
            prev.rightnodes+=1
            root=root.right
        else:
            prev=root
            prev.leftnodes+=1
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


def findith(root,i):
    if i==root.leftnodes+1:
        return root.key
    if i<=root.leftnodes:
        return findith(root.left,i)
    else:
        return findith(root.right,i-root.leftnodes-1)

def w(root,k):

    if root.parent == None:
        return k
    else:
        if root.parent.right == root:
            k += root.parent.leftnodes + 1
        return w(root.parent, k)

def whichith(root):
    k=root.leftnodes+1
    return w(root,k)




root=BSTNode()
root.key=9
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

print(whichith(root))
print(whichith(root.left))
print(whichith(root.right))
print(whichith(root.left.right.right))
