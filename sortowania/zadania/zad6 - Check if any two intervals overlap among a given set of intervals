#An interval is represented as a combination of start time and end time. Given a set of intervals,
# check if any two intervals overlap.
def partition(arr,left,right):
    i=left-1
    pivot=arr[right]
    for j in range(left,right):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]

    return i+1


def quickSort(arr,left,right):
    if left<right:
        pi=partition(arr,left,right)
        quickSort(arr,left,pi-1)
        quickSort(arr,pi+1,right)


def overlap(arr):
    quickSort(arr,0,len(arr)-1)
    i=0
    j=1

    while i<len(arr)-1:
        if arr[i][1]>arr[j][0]:
            overlaped=(arr[i],arr[j])
        i+=1
        j+=1

    return overlaped
