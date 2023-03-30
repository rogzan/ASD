def partition(arr,left,right):
    i=left-1
    pivot=arr[right]
    for j in range(left,right):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]
    return i+1

def quickSortIterative(arr,left,right):

    size=right-left+1
    stack=[0]*size

    top=0
    stack[top]=left
    top+=1
    stack[top]=right

    while top>=0:

        r=stack[top]
        top-=1
        l=stack[top]
        top-=1

        pi=partition(arr,l,r)

        if pi-1>l:
            top+=1
            stack[top]=l
            top+=1
            stack[top]=pi-1
        if pi+1<r:
            top+=1
            stack[top]=pi+1
            top+=1
            stack[top]=r
