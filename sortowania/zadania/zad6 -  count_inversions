def countMerge(arr,left,middle,right):
    counter=0
    n1=middle-left+1
    n2=right-middle

    L=[0]*n1
    R=[0]*n2
    i=0
    k=left
    while i<n1:
        L[i]=arr[k]
        i+=1
        k+=1
    i=0
    while i<n2:
        R[i]=arr[k]
        i+=1
        k+=1

    i=0
    j=0
    k=left
    while i<n1 and j<n2:
        if L[i]>R[j]:
            counter+=(middle-left-i+1)
            arr[k]=R[j]
            k+=1
            j+=1
        else:
            arr[k]=L[i]
            k+=1
            i+=1

    while i<n1:
        arr[k]=L[i]
        k+=1
        i+=1

    while j<n2:
        arr[k]=R[j]
        k+=1
        j+=1


    return counter



def countInversions(arr,left,right):
    counter=0
    if left < right:
        middle=(right+left)//2
        counter+=countInversions(arr,left,middle)
        counter+=countInversions(arr,middle+1,right)
        counter+=countMerge(arr,left,middle,right)
    return counter
