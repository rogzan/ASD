# Kolos 2014/zad1
# Pewna firma przechowuje dużo liczb pierwszych w postaci binarnej jako stringi ”10101...”.
# Zaimplementuj strukturę danychSetdo przechowywania tych danych. Napisz funkcje:Set createSet( string A[], int n ),
# która tworzy Set z n-elementowej tablicy stringów oraz bool contains( Set a, string s ), która sprawdza czy dana liczba jest w Secie.
# Oszacuj złożoność czasową i pamięciową powyższych funkcji.

class Set:
    def __init__(self):
        self.root = None

class BSTNode:
    def __init__(self):
        self.number=None
        self.left=None
        self.right=None
        self.is_end = None

def newnode(number):
    x = BSTNode()
    x.number = number
    return x

def addstring(set, number):
    l = len(number)
    i = 0
    ptr = set.root
    while i < l:
        if number[i] == "0":
            if ptr.left != None: ptr = ptr.left
            else:
                tmp = newnode("0")
                ptr.left = tmp
                ptr = ptr.left
        elif number[i] == "1":
            if ptr.right != None: ptr = ptr.right
            else:
                tmp = newnode("1")
                ptr.right = tmp
                ptr = ptr.right
        i += 1
    ptr.is_end = True

def createset(A, n):
    numbers = Set()
    root = BSTNode()
    numbers.root = root
    for i in range(n):
        addstring(numbers, A[i])
    return numbers

def contains(a, s):
    if a.root == None: return False
    ptr = a.root
    i = 0
    length = len(s)
    while i < length:
        if s[i] == '0':
            if ptr.left != None: ptr = ptr.left;
            else: return False
        elif s[i] == '1':
            if ptr.right != None: ptr = ptr.right
            else: return False
        i += 1
    if ptr.is_end: return True;
    else: return False

tab = ["0001","0010","0011"]
numbers = createset(tab,len(tab))
exists = contains(numbers,"0011")
if exists: print("tak")
else: print("nie")
