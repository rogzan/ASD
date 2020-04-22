"""
Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności O(n), który stwierdza, czy w tablicy
ponad połowa elementów ma jednakową wartość.

"""

def half(arr):
    mx=max(arr)+1

    n=len(arr)
    buckets=[]
    for i in range(n):
        buckets.append([])

    for i in range(len(arr)):
        norm_num=arr[i]/mx
        idx=int(n*norm_num)
        buckets[idx].append(arr[i])

    for i in range(len(buckets)):
        if len(buckets[i])>len(arr)//2:
            buckets[i]=sorted(buckets[i])
            s=mx
            counter=1
            best=1
            s=buckets[i][0]
            for k in range(1,len(buckets[i])):
                if buckets[i][k]==s:
                    counter+=1
                else:
                    if counter>best:
                        best=counter
                        counter=1
                s=buckets[i][k]
            if best>len(arr)//2:
                return True
            else:
                return False

    return False


    
if __name__=="__main__":
    arr=[4,5,4,7,4,2,4,4,4,8,2,4,5,7,5,6,3,4,5,6,7,78,8,8,8,8,86,7,6,7,8,9,3,2,8,6,13,15,80,4,34,4,4,7,8,9,9,8,8,5,9,8,9,4,44,4,4,4,4,4,14,14,6,4,4,4,2,34,5,4,4,4,4,8,4,2,3,4,4,4]
    if half(arr):
        print("Yes")
    else:
        print("No")
