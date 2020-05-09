"""
Longest Increasing Subsequence - O(n^2)

"""

def LIS(arr):
    n=len(arr)
    f=[1]*n
    p=[-1]*n

    for i in range(1,n):
        for j in range(i):
            if arr[j]<arr[i] and f[i]<f[j]+1:
                f[i]=f[j]+1
                p[i]=j

    return f,p




def printLIS(arr,p,i):
    if p[i]>=0:
        printLIS(arr,p,p[i])
    print(arr[i])


def wrapLIS(arr):
    f,p=LIS(arr)
    l=max(f)

    i=0
    while f[i]!=l:
        i+=1

    printLIS(arr,p,i)



if __name__=="__main__":
    arr=[2,3,1,6,15,23,7,10,12,5,16,18,1,3,5,12,4,2,3,6,2,14,23,35,24,90,2,3,1,95,4,2]
    wrapLIS(arr)
