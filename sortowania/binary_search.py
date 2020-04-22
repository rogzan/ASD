def binarySearch(arr,val):
    n=len(arr)
    l=0
    r=n-1
    while l<=r:
        s=(l+r)//2
        if arr[s]==val:
            return s
        elif arr[s]<val:
            l=s+1
        else:
            r=s-1

    return -1
