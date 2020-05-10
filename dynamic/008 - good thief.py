"""
Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n − 1]. Złodziej
chce wybrać przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu
ukraść dwa przedmioty leżące obok siebie. Proszę zaimplementować funkcję:
int goodThief( int A[], int n );
która zwraca maksymalną wartość przedmiotów, które złodziej może ukraść zgodnie ze swoim
kodeksem moralnym oraz wypisuje numery przemiotów które powinien wybrać. Proszę uzasadnić
poprawność algorytmu oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie
jak najszybszy (ale przede wszystkim poprawny).


"""


def goodThief(arr):
    n=len(arr)
    f=[0]*(n+2)

    f[0]=0
    f[1]=0

    for i in range(2,n+2):
        if f[i-2]+arr[i-2]>f[i-1]:
            f[i]=f[i-2]+arr[i-2]
        else:
            f[i]=f[i-1]

    return f[n+1]

arr=[5,7,8,2,4,3,1,10,6]
print(goodThief(arr))
print("A:")
A=[5,8,9,10,3,5,38,8,10,23,43,20,7,8,9]
print(goodThief(A))

# https://www.geeksforgeeks.org/find-maximum-possible-stolen-value-houses/
