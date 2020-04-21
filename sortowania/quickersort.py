def QuickerSort(l):
    if len(l) == 0:
        return l
    x = l[0]
    lt = []
    eq = []
    gt = []
    while len(l) > 0:
        y = l.pop(0)
        if y < x:
            lt.append(y)
        elif y > x:
            gt.append(y)  
        else:
            eq.append(y)
    return QuickerSort(lt) + eq + QuickerSort(gt)


l = [2, 7, 3, 17, 13, 19, 2, 5, 11, 7]
l2 = QuickerSort(l)
print(l2)
