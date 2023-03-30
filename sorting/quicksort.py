def quick_sort(t, p, r):
    if p<r:
        q=partition(t,p,r)
        quick_sort(t,p,q-1)
        quick_sort(t,q+1,r)

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
