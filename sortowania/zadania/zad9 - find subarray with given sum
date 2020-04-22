def findSum(arr,sum):
    n=len(arr)
    curr=arr[0]
    start=0

    for i in range(1,n):

        while curr+arr[i]>sum:
            curr -= arr[start]
            start+=1

        if curr+arr[i]==sum:
            return (start,i)
        else:
            curr+=arr[i]

    return -1
