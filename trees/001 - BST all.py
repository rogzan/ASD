class BSTNode:
    def __init__(self):
        self.key=None
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

def insert(root,key):

    while root!=None:
        if root.key<key:
            prev=root
            root=root.right
        else:
            prev=root
            root=root.left
    new = BSTNode()
    new.key = key
    if prev.key<key:
        prev.right=new
        new.parent=prev
    else:
        prev.left=new
        new.parent = prev

def mx(root): #max
    while root.right:
        root=root.right
    return root.key

def mn(root): #min
    while root.left:
        root=root.left
    return root.key

def succ(root): #następnik
    f=root.key
    if root.right:
        return mn(root.right)
    else:
        while root.parent and root.parent.key<root.key:
            root=root.parent
        if root.parent:
            if root.parent.key < f:
                return None
            return root.parent.key
        if root.key < f:
            return None
        return root.key


def pred(root): #poprzednik
    f=root.key
    if root.left:
        return mx(root.left)
    else:
        while root.parent and root.parent.key > root.key:
            root = root.parent

        if root.parent:
            if root.parent.key>f:
                return None
            return root.parent.key
        if root.key>f:
            return None
        return root.key


def delete(root, key):
    if not root:
        return root
    if root.key > key:
        root.left = delete(root.left, key)
    elif root.key < key:
        root.right= delete(root.right, key)
    else:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        temp = root.right
        mini = temp.key
        while temp.left:
            temp = temp.left
            mini = temp.key
        root.key = mini
        root.right = delete(root.right,root.key)
    return root


def kth_largest(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.right
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.key
        root = root.left

root=BSTNode()
root.key=9
insert(root,15,)
insert(root,6)
insert(root,10)
insert(root,3)
insert(root,7)
insert(root,8)
insert(root,2)
insert(root,4)
insert(root,1)
insert(root,20)

root.display()
delete(root,15)
root.display()
