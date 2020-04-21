def countingSort(arr,exp):
    count=[0]*10
    n=len(arr)
    for i in range(n):
        ind=arr[i]//exp
        count[ind%10]+=1
    sum=0

    for i in range(10):
        sum+=count[i]
        count[i]=sum

    output=[0]*n

    for i in range(n-1,-1,-1):
        ind=arr[i]//exp
        output[count[ind % 10] - 1] = arr[i]
        count[ind % 10] -= 1

    return output
    
def radixSort(arr):
    max1=max(arr)
    exp=1
    while (max1//exp) > 0:
        arr=countingSort(arr,exp)
        exp*=10

    return arr
