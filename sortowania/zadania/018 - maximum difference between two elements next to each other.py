"""
Dana jest tablica A liczb wymiernych (wszystkie liczby są różne). Proszę podać algorytm,
który znajdzie takie dwie liczby A[i] i A[j], które po posortowaniu tablicy występują bezpośrednio koło siebie
i których różnica jest maksymalna.
"""


def adjacentMax(arr):


    mi = min(arr)
    mx = max(arr)
    n = len(arr)//2
    buckets = []

    for i in range(n):
        buckets.append([])

    for i in range(len(arr)):
        norm_num=(arr[i]-mi)/mx
        idx=int(norm_num*n)
        buckets[idx].append(arr[i])

    print(buckets)

    T=[0]*3


    for i in range(1,len(buckets)):
        if len(buckets[i])==0:
            j=i
            while(len(buckets[i+1])==0):
                i+=1
            while(len(buckets[j-1])==0):
                j-=1
            a=min(buckets[i+1])
            b=max(buckets[j-1])
            if a-b>T[0]:
                T[0]=a-b
                T[1]=b
                T[2]=a
        else:
            if buckets[i] and buckets[i-1]:
                a=min(buckets[i])
                b=max(buckets[i-1])
                if a-b>T[0]:
                    T[0]=a-b
                    T[1]=b
                    T[2]=a
    print(T)


if __name__=="__main__":
    arr=[1,2,3,24,85,89,46,61,67,25,89,67,45,46,21,8,80]
    adjacentMax(arr)
