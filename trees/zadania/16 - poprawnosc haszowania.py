# /* Funkcja sprawdza, czy dana tablica haszujaca ma prawidlowo wpisane dane.
# Haszujemy stringi z tablicy *key, tablica haszujaca to *data, zajetosc *data sprawdza *free, a sama *data przechowuje wartosci haszy. */

# Żeby zrobić to wzorcowo, musimy dla każdego elementu w tablicy znaleźć, gdzie powinien być jego hash 
# (O(1) wywołanie hash(x)) i sprawdzić, czy między nim a jego hashem jest -1. Tworzymy sobie dodatkową tablicę P,
# gdzie P[i] oznacza indeks ostatniej napotkanej -1, na lewo od i. Tablicę P uzupełniamy tak, że iterujemy po T 
# i jak nie ma -1 pod T[i], to wpisujemy indeks ostatniej zapamiętanej -1,  a jak T[i] jest -1, to aktualizujemy
# indeks ostatniej napotkanej -1. Dla liczb w T, poprzedzających pierwszą -1, możemy w P[i] wpisać jakieś -1 albo None.
# I teraz jeżeli i < hash(T[i]%N) to sprawdzamy, czy P[hash(i)%N] > i jak tak to jest źle, bo jest -1 między pozycją i hashem.
# No i przypadek symetryczny dla i > hash(T[i]%N).

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
