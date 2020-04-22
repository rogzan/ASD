"""
Mamy daną tablię zawierającą n (n>=11) liczb naturalnych w zakresie [0,k]. Zamieniono 10 liczb z tej tablicy na losowe
liczby spoza tego zakresu (np. dużo większe lub ujemne). Napisz algorytm, który posortuje tablicę w czasie 0(n).

"""

def insertionSort(arr):

    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key


def Sort(arr,k):
    ch_less=[]
    ch_more=[]

    for i in range(len(arr)):
        if arr[i]<0:
            ch_less.append(arr[i])
            arr[i]=-1
        if arr[i]>k:
            ch_more.append(arr[i])
            arr[i]=-1

    insertionSort(ch_less)
    insertionSort(ch_more)

    buckets=[]
    n=k

    for i in range(n):
        buckets.append([])

    for i in arr:
        if i!=-1:
            norm_num=i/k
            idx=int(norm_num*n)
            buckets[idx].append(i)

    output=[]

    for i in range(len(ch_less)):
        output.append(ch_less[i])

    for i in range(len(buckets)):
        output.extend(buckets[i])

    for i in range(len(ch_more)):
        output.append(ch_more[i])

    return output


    
if __name__=="__main__":
    k=10
    arr=[4,6,100,3,6,45,4,-45,6,2,73,4,9,1,3,6,-37,3,0,6,3,7,2,50,4,1,8,9,7,533,4,3,2,5,7,122,0,4,5,0,1,0,-154,3,6,190,8,4]
    result=Sort(arr,k)
    print(arr)
    print(result)
