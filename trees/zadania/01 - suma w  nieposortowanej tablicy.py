"""
Dana jest nieposortowana tablica A[1...n] oraz liczba x. Proszę podać algorytm sprawdzający, czy istnieją
indeksy i oraz j, takie że A[i] + A[j] = x.

"""

def Pair(A,x):
    s=set()
    for i in range(len(A)):
        t=x-A[i]
        if t in s:
            print(t,A[i])
        s.add(A[i])

A=[3,8,2,15,10,5,7,12,-2]
Pair(A,10)
