def reverse(arr,left,right):
    i=left
    j=right
    while i<=j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

def moveElements(arr,k):
    reverse(arr,0,len(arr)-1)
    reverse(arr,0,k-1)
    reverse(arr,k,len(arr)-1)


if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9]
    print(arr)
    moveElements(arr,3)
    print(arr)
