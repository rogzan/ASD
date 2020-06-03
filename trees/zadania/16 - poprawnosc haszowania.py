# /* Funkcja sprawdza, czy dana tablica haszujaca ma prawidlowo wpisane dane.
# Haszujemy stringi z tablicy *key, tablica haszujaca to *data, zajetosc *data sprawdza *free, a sama *data przechowuje wartosci haszy. */

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


def checkHT (ht, hashtable):
    if hashtable.size==0: return True;
    flag = True;
    i = 0
    while i<ht.size and flag == True:
        hash_value=hash(ht.key[i],ht.size)
        hash_data=hash_value
        n=0
        while ht.free[hash_value] == False and n < ht.size:
            if ht.data[hash_value]==hash_data: break
            hash_value=(hash_value+1)%ht.size
            n+=1
        if n==ht.size or ht.free[hash_value]==True:
            flag=False;
        i+=1
    return flag
