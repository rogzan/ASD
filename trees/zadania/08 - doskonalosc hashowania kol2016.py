# Kol 2016/zad 2
# Dana jest struktura struct HT{int* table; int size;}, która opisuje tablicę haszującą rozmiaru size,
# przechowującą liczby nieujemne. Tablica korzysta z funkcji haszującej int hash(int x)i liniowego rozwiązywania konfliktów
# (ujemne wartości w tablicy table oznaczają wolne pola). Doskonałością takiej tablicy nazywamy liczbę elementów x takich,
# że pozycja x w tablicy to hash(x) mod size(a więc x jest na ”swojej” pozycji). Proszę napisać funkcję:void enlarge( HT* ht);
# która powiększa tablicę dwukrotnie i wpisuje elementy w takiej kolejności, by doskonałość powstałej tablicy była jak największa.
# Funkcja powinna być możliwie jak najszybsza.

class Node:
    def __init__(self):
        self.key=None
        self.value=None
        self.state=None         #occupied = oc ; keep_looking= kl ; empty = None

def hash(key,n): #zakładam, że mam super extra dobrze liczącą funkcję haszującą, to tylko do testowania
    return key%n

class HashTable:
    def __init__(self,n):
        self.a=[None]*n
        self.n=n
        self.ws=17      #wzlędnie pierwszy w stosunku do n

    def insert(self,key,value):
        idx=hash(key,self.n)
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
        idx=hash(key,n)
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

def enlarge(ht):
    result = HashTable(ht.n*2)
    for i in range(result.n):
        result.a[i]=-1;
    for i in range(ht.n):
        new_index=hash(ht.a[i])%result.n;
        if new_index==ht.a[i]:
            result.a[new_index]=ht.a[i];
            ht.a[i]=-1
    for i in range(ht.n):
        if ht.a[i]!=-1:
            new_index=hash(ht.a[i])%result.n;
            while result.a[new_index]!=-1:
                new_index=(new_index+1)%result.n;
            result.a[new_index]=ht.a[i];
    ht.n=2*(ht.n);
    ht.a=result.a;
#-------------------------#
class HT:
    def __init__(self,n):
        self.table =[None]*n
        self.size = n
def hash (x):
    result=0;
    result^=(x>>2)+x;
    return result;
