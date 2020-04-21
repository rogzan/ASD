def ternarySearch(arr,val):
    n=len(arr)
    l=0
    r=n-1

    while l<=r:
        p=(r-l)//3  #przeskok
        s1=l+p
        s2=l+2*p
        
        if arr[s1]==val:
            return s1
        elif arr[s1]>val:
            r=s1-1
        elif arr[s2]==val:
            return s2
        elif arr[s2]<val:
            l=s2+1
        else:
            l=s1+1
            r=s2-1
    return -1
