"""
Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n. Napisz algorytm, który posortuje tę
tablicę w czasie O(n).
Można założyć, że stringi składają sie wyłącznie z małych liter alfabetu łacińskiego.
W sortowaniu pierwszeństwo ma długość stringa, kolejność alfabetyczna w drugiej kolejności.

"""
def countingSort(arr,i):

    count=[0]*26
    n=len(arr)
    for j in range(n):
        ind=(ord(arr[j][i])-97)%26
        count[ind]+=1

    for j in range(1,len(count)):
        count[j]+=count[j-1]

    output=[0]*n

    for j in range(n-1,-1,-1):
        ind = (ord(arr[j][i])-97) % 26
        output[count[ind]-1]=arr[j]
        count[ind]-=1

    return output

def radixSort(arr):

    d=len(arr[0])

    for i in range(d-1,-1,-1):
        arr=countingSort(arr,i)


    return arr


def Sort(arr):

    best=0
    for i in range(len(arr)):
        if len(arr[i])>best:
            best=len(arr[i])

    buckets=[]
    for i in range(best):
        buckets.append([])

    for i in range(len(arr)):
        idx=len(arr[i])-1
        buckets[idx].append(arr[i])

    output=[]
    for i in range(len(buckets)):
        buckets[i]=radixSort(buckets[i])

    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            output.append(buckets[i][j])

    return output



    
if __name__=="__main__":
    arr=["koiaf","a","ptatea", "dai", "adfa", "awei", "bekadfy", "srmry", "wyra", "z", "ta", "mtka", "fadka", "ana", "anset", "mvaa", "tloa", "kyta",
         "sytsch", "pat", "rrt", "izyr", "fikr", "ari", "madva", "zytka", "ma", "ka"]
    result=Sort(arr)
    print(result)
