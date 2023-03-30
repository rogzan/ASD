def partition(arr,left,right):
    pivot=arr[right]
    i=left-1

    for j in range(left,right):
        if arr[j]<pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    i+=1
    arr[i],arr[right]=arr[right],arr[i]
    return i


def quickSort(arr,left,right):

    if left<right:
        pi=partition(arr,left,right)
        quickSort(arr,left,pi-1)
        quickSort(arr,pi+1,right)

def binarySearchFirst(arr,left,right,x):

    while left<=right:
        middle=(left+right)//2
        if arr[middle]==x:
            while arr[middle-1]==x:
                middle-=1
            return middle
        elif arr[middle]<x:
            left=middle+1
        else:
            right=middle-1

    return -1

def SortAccording(arr1,arr2):

    
    temp=arr1[:]
    quickSort(temp,0,len(temp)-1)
    visited=[0]*len(arr1)
    j=0

    for i in range(len(arr2)):

        p=binarySearchFirst(temp,0,len(temp)-1,arr2[i])
        arr1[j]=arr2[i]
        visited[p]=1
        j+=1
        while temp[p+1]==arr2[i]:
            arr1[j] = arr2[i]
            j+=1
            p+=1
            visited[p] = 1


    for i in range(len(visited)):
        if visited[i]==0:
            arr1[j]=temp[i]
            j+=1
