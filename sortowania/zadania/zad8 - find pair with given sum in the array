def quickSort(arr,left,right):
    if left<right:
        pi=partition(arr,left,right)
        quickSort(arr,left,pi-1)
        quickSort(arr,pi+1,right)

def partition(arr,left,right):
    i=left-1
    pivot=arr[right]
    for j in range(left,right):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]
    return i+1

def pairWithGivenSum(arr,val):
    quickSort(arr,0,len(arr)-1)

    l=0
    r=len(arr)-1
    results=[]
    while l<r:
        sum=arr[l]+arr[r]
        if sum==val:
            return (l,r)
        elif sum<val:
            l+=1
        else:
            r-=1



if __name__=="__main__":
    arr=[2,45,2,4,6,6,3,45,6,3,6,26,26,75,74,24,63,88,57,35,63,63,98,65,24,56,4,74,24,6]
    res=pairWithGivenSum(arr,6)
    print(arr)
    print(res)
