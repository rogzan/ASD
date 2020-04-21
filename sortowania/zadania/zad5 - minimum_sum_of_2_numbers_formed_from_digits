#Given an array of digits (from 0 to 9), find the minimum possible sum of two numbers formed from digits
#of the array. All digits of given array must be used to form the two numbers.

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

def minSum(arr):
    quickSort(arr,0,len(arr)-1)
    a=0
    b=0

    for i in range(len(arr)):
        if i%2==0:
            a=a*10+arr[i]
        else:
            b=b*10+arr[i]

    return a+b
