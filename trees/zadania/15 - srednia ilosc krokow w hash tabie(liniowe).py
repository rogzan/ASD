# /* Funkcja oblicza srednia ilosc krokow przy liniowym rozwiazywaniu kolizji w danej tablicy haszujacej */


class HT:
    def __init__(self):
        self.key = None #tablica na klucze danych
        self.data = None #tablica na dane
        self.free = None #pole wolne czy zajete
        self.size = None #rozmiar tablicy
        
def hash (key, size):
    hash=0;
    for i in range(len(key)): hash^=(hash<<3)+key[0]
    return hash%size

def take_place (ht, hashtable, index):
    if hashtable.size==0: return 0
    hash_value=hash(ht.key[index],hashtable.size)
    steps=0

    while hashtable.free[hash_value] == False and steps<hashtable.size:
        hash_value=(hash_value+1)%hashtable.size
        steps+=1
    hashtable.free[hash_value]=False
    return steps

def averageAccess (ht):
    hashtable = HT()
    hashtable.size=ht.size
    hashtable.free = [hashtable.size]
    for i in range(hashtable.size): hashtable.free[i]=True;
    steps = 0
    for i in range(hashtable.size): steps+=take_place(ht,hashtable,i)
    result = steps / hashtable.size
    return result
