"""

Dana jest tablica z n liczbami całkowitymi. Zawiera ona bardzo dużo powtórzeń - co więcej, zaledwie log(n) liczb jest
unikatowe (reszzta to powtórzenia). Napisz algorytm, który w czasie O(n*log(log(n))) posortuje taką tablicę.


"""



def binarySearch(arr,val):
    n=len(arr)
    l=0
    r=n-1
    while l<=r:
        s=(l+r)//2
        if arr[s][0]==val:
            return s
        elif arr[s][0]<val:
            l=s+1
        else:
            r=s-1

    return -1


def Sort(arr,n):

    aux=[]

    for i in range(n):
        k=binarySearch(aux,arr[i])

        if k==-1:
            aux.append([arr[i],1])
            aux=sorted(aux)
        else:
            aux[k][1]+=1

    i=0
    for j in range(len(aux)):
        for k in range(aux[j][1]):
            arr[i]=aux[j][0]
            i+=1





if __name__=="__main__":
    arr=[2,3,1,4,5,1,2,3,4,5,5,4,3,2,1,3,3,3,3,3,5,5,5,5,5,1,1,1,1,1,2,2]
    print(arr)
    Sort(arr,len(arr))
    print(arr)
