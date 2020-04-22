
"""
K 2016/2017 Zadanie 2

Proszę zaimplementwoać funkcję sumBetween(arr,from,to,n), której zadaniem jest obliczyć sumę liczb z
n elementwowej tablicy arr, które w posortowanej tablicy znajdowałyby się na pozycjach o indeksach
od from do to (włącznie). Można przyjąć, że liczby w tablicy są parami różne (ale nie można przyjąć
żadnego innego rozkładu danych).

"""

def partition(arr,left,right):
    pi=arr[right]
    i=left-1

    for j in range(left,right):
        if arr[j]<pi:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]

    return i+1

def kthStatistics(arr,left,right,k):
    i=partition(arr,left,right)
    if i==k:
        return

    if i>k:
        kthStatistics(arr,left,i-1,k)
    else:
        kthStatistics(arr,i+1,right,k)

def sumBetween(arr,fr,to,n):
    kthStatistics(arr,0,n-1,fr)
    kthStatistics(arr,0,n-1,to)
    sum=0
    for i in range(fr,to+1):
        sum+=arr[i]

    return sum


if __name__=="__main__":
    arr=[3,6,1,6,9,2,7,10,15,28,2,19,50,34,20,4,7,28,9,30,40,28,4,7,24,7]
    print(sumBetween(arr,5,10,len(arr)))
