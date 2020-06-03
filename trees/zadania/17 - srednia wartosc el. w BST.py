# /* Funkcja oblicza srednia wartosc elementow w drzewie BST */

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

def get_numbers (T, sum, counter):
    if T == None: return
    sum+=T.value
    counter+=1
    if  T.left!=None: get_numbers(T.left,sum,counter)
    if T.right!=None: get_numbers(T.right,sum,counter)

def average (T):
    if T==None: return 0;
    sum=0
    counter=0
    get_numbers(T,sum,counter)
    return sum / counter
