"""
Mamy dwie tablice, A[n] i B[n]. Należy znaleźć długość ich najdłuższego wspólnego podciągu. (Klasyczny O(n^2))

"""

def subsequence(A,B):
    n=len(A)

    f=[None]*n
    for i in range(n):
        f[i]=[0]*n

    i=0
    while B[i]!=A[0] and i<n:
        i+=1
    while i<n:
        f[i][0]=1
        i+=1

    i=0
    while B[0]!=A[i] and i<n:
        i+=1
    while i<n:
        f[0][i]=1
        i+=1

    for i in range(1,n):
        for j in range(1,n):
            if A[j]==B[i]:
                f[i][j]=max(f[i][j-1],f[i-1][j])+1

            else:
                f[i][j]=max(f[i-1][j],f[i][j-1])

    return f[n-1][n-1]


if __name__=="__main__":
    A=[3,5,2,7,1,3]
    B=[5,8,2,5,7,3]
    print(subsequence(A,B))
