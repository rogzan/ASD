"""

Dany jest zbiór przedziałów otwartych. Zaproponuj algorytm, który znajdzie podzbiór tego zbioru taki, że
1. jego rozmiar wynosi dokładnie k
2. przedziały są rozłącznie
3. różnca między najwcześniejszym początkiem a najdalszym końcem jest minimalna.

Jeśli rozwiązanie nie istnieje, to algorytm powinien to stwierdzić.

"""
def quickSort(arr,left,right):
    if left<right:
        pi=partition(arr,left,right)
        quickSort(arr,left,pi-1)
        quickSort(arr,pi+1,right)

def partition(arr,left,right):
    i=left-1
    pivot=arr[right][1]
    for j in range(left,right):
        if arr[j][1]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]
    return i+1


def subset(p,k):
    quickSort(p,0,len(p)-1)
    best=1000

    for i in range(len(p)-k):
        temp=[]
        temp.append(p[i])
        l=1
        j=i+1
        while l<k and j<len(p):

            if temp[l-1][1]<=p[j][0]:
                temp.append(p[j])
                l+=1
            j+=1

        d=temp[l-1][1]-temp[0][0]

        if d<best and l==k:
            best=d
            result=temp[:]

    print(result)


if __name__=="__main__":

    p=[[0,3],[4,5],[6,8],[7,9],[5,10],[1,3]]
    subset(p,3)
