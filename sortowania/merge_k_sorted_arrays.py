def mergeTwoSortedArrays(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    i1=0
    i2=0
    result=[0]*(n1+n2)
    r=0

    while i1<n1 and i2<n2:
        if arr1[i1]<arr2[i2]:
            result[r]=arr1[i1]
            i1+=1
        else:
            result[r]=arr2[i2]
            i2+=1
        r+=1
    while i1<n1:
        result[r]=arr1[i1]
        r+=1
        i1+=1
    while i2<n2:
        result[r]=arr2[i2]
        r+=1
        i2+=1

    return result



def mergeArrays(arr):

    while len(arr)!=1:
        result=[]
        for i in range(0,len(arr),2):
            if i==len(arr)-1:
                result.append(arr[i])
            else:
                result.append(mergeTwoSortedArrays(arr[i],arr[i+1]))
        arr=result
    return arr





if __name__=="__main__":
    arr=[[1,2,3], [3,4,7,7], [6,8,19], [1,3,5,7,8,9]]
    arr=mergeArrays(arr)
    print(arr)
