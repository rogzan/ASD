def Select(A, k):   
    return _Select(A, 0, len(A) - 1, k)

def partition(t,p,r):
    x=t[r]
    i=p-1
    for j in range(p,r):
        if t[j] <= x:
            i += 1
            t[i], t[j] = t[j], t[i]
    t[i + 1], t[r]= t[r], t[i + 1]
    return i+1
    
def _Select(arr, left, right, k):   
    if left == right:
        return arr[left]
    q = partition(arr, left, right)
    size = q - left + 1

    if size == k:     
        return arr[q]
    if k < size:
         return _Select(arr, left, q - 1, k)   
    else:
        return _Select(arr, q + 1, right, k - size)
