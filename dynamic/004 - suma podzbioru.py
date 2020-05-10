"""
Dana jest tablica n liczb A. Proszę podać i zaimplementować algorytm, który sprawdza, czy da sie wybrać podciąg
liczb z A, które sumują się do zadanej wartości T.

"""

def sub(A,t):
    n=len(A)
    f=[None]*n
    for i in range(n):
        f[i]=[0]*(t+1)
    for i in range(n):
        if A[i]<=t:
            f[i][A[i]]=1
    for j in range(1,t+1):
        for i in range(1,n):
            if j-A[i]>=0:
                f[i][j]=max(f[i][j],f[i-1][j],f[i-1][j-A[i]])
            else:
                f[i][j]=max(f[i][j],f[i-1][j])
    for i in range(n):
        print(f[i])
    return f[n-1][t]==1,f

def printSub(A,f,t):
    n=len(A)
    for i in range(n):
        if f[i][t] == 1:
            if A[i] == t:
                print(A[i])
                return
            else:
                print(A[i])
                printSub(A,f,t-A[i])
                return

def wrapSub(A,t):
    b,f=sub(A,t)
    if b:
        printSub(A,f,t)
    else:
        print("not possible")



A=[3,4,6,1,2,8,10]
wrapSub(A,13)
