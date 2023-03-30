def interpolationSearch(arr,val):
    l=0
    r=len(arr)-1

    while l<=r:
        s=(val-arr[l])*(r-l)//(arr[r]-arr[l])
        if arr[s]==val:
            return s
        elif arr[s]<val:
            l=s+1
        else:
            r=s-1
    return -1
