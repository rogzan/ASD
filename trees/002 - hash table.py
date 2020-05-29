class Node:
    def __init__(self):
        self.key=None
        self.value=None
        self.state=None         #occupied = oc ; keep_looking= kl ; empty = None

def hashFunction(key,n): #zakładam, że mam super extra dobrze liczącą funkcję haszującą, to tylko do testowania
    return key%n

class HashTable:
    def __init__(self,n):
        self.a=[None]*n
        self.n=n
        self.ws=17      #wzlędnie pierwszy w stosunku do n

    def insert(self,key,value):
        idx=hashFunction(key,self.n)
        i=0
        ws=self.ws
        n=self.n
        while self.a[idx] and self.a[idx].state=="oc" and i<n:
            idx=(idx+ws*i)%n
            i+=1
        new=Node()
        new.key=key
        new.value=value
        new.state="oc"
        self.a[idx]=new


    def find(self,key):
        n=self.n
        ws = self.ws
        idx=hashFunction(key,n)
        i=0
        while self.a[idx] and i<n:
            if self.a[idx].key==key and self.a[idx].state!="kl":
                return idx
            idx=(idx+ws*i)%n
            i+=1
        return None

    def remove(self,key):
        i=self.find(key)
        self.a[i].state="kl"


h=HashTable(100)

h.insert(17,1)
h.insert(135,2)
h.insert(17,3)
h.insert(19,4)
h.insert(16,5)
h.insert(118,6)
h.insert(56,7)
h.insert(78,8)
h.insert(90,9)
h.insert(89,10)
h.insert(189,11)
h.insert(170,12)
h.insert(617,13)
h.insert(8763,14)
h.insert(12325,15)
h.insert(121,16)
h.insert(16,17)
h.remove(16)
h.remove(118)
print(h.find(16))
print(h.find(118))
