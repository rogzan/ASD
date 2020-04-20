def quick_sort(t, p, r):
    while p<r:
        q=partition(t,p,r)
        if q-p < r-q:
            quick_sort(t,p,q-1)
            p = q + 1
        else:
            quick_sort(t,q+1,r)
            r = q - 1

def partition(t,p,r):
    x=t[r]
    i=p-1
    for j in range(p,r):
        if t[j] <= x:
            i += 1
            t[i], t[j] = t[j], t[i]
    t[i + 1], t[r]= t[r], t[i + 1]
    return i+1


t=[5, 2, 8, 1, 3, 9, 2, 5, 11, 7]
quick_sort(t, 0, 9)
print(t)
