"""
There was a list of length m * n, which had unique values and was sorted.
It was cut into n parts of same length, and then those parts were randomly
shuffled. Elements inside each part were then also shuffled.
Implement function fix_unsorted(arr, n) which will sort such array.
"""


def merge(arr,left,middle,right):

    n1=middle-left+1
    n2=right-middle

    L=[0]*n1
    R=[0]*n2

    l=0
    i=left
    while l<n1:
        L[l]=arr[i]
        l+=1
        i+=1
    r=0
    while r<n2:
        R[r]=arr[i]
        r+=1
        i+=1

    l=0
    r=0
    i=left
    while l<n1 and r<n2:
        if L[l]<R[r]:
            arr[i]=L[l]
            l+=1
        else:
            arr[i]=R[r]
            r+=1
        i+=1
    while l<n1:
        arr[i]=L[l]
        i+=1
        l+=1
    while r<n2:
        arr[i]=R[r]
        i+=1
        r+=1



def mergeSort(arr,left,right):
    if left<right:
        middle=(left+right)//2
        mergeSort(arr,left,middle)
        mergeSort(arr,middle+1,right)
        merge(arr,left,middle,right)



def fix_unsorted(arr,n):


    m=len(arr)//n
    first=[]
    for i in range(n):
        first.append([0,i])

    j=0
    for i in range(0,len(arr),m):
        mergeSort(arr,i,i+m-1)
        first[j][0]=arr[i]
        j+=1

    mergeSort(first,0,len(first)-1)

    result=[]

    for i in range(n):
        k=first[i][1]
        result+=arr[k*m:k*m+m]

    arr=result





if __name__=="__main__":
    arr=[4,2,8,1,35,38,31,34,15,20,12,17,23,29,30,21]
    fix_unsorted(arr,4)
    print(arr)
