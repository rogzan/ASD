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
        return arr[i]

    if i>k:
        kthStatistics(arr,left,i-1,k)
    else:
        kthStatistics(arr,i+1,right,k)
