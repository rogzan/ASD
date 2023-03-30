def mergeTwoSortedArrays(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    result=[0]*(n1+n2)
    i=0
    i1=0
    i2=0

    while i1<n1 and i2<n2:
        if arr1[i1]<arr2[i2]:
            result[i]=arr1[i1]
            i1+=1
        else:
            result[i]=arr2[i2]
            i2+=1
        i+=1

    while i1<n1:
        result[i]=arr1[i1]
        i+=1
        i1+=1

    while i2<n2:
        result[i]=arr2[i2]
        i+=1
        i2+=1

    return result
