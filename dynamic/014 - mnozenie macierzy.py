"""
Dany jest ciąg macierzy. Macierze nie są koniecznie kwadratowe (ale oczywiście znamy ich rozmiary). Zależnie
w jakiej kolejności wykonujemy mnożenia, koszt obliczeniowy może być różny - należy podać algorytm znajdujący
koszt mnożenia przy optymalnym doborze kolejności.

"""
import sys
def matrix(M):
    n=len(M)
    a=[None]*n
    for i in range(n):
        a[i]=[0]*n

    for l in range(2,n+1):
        for i in range(0,n-l+1):
            j=i+l-1
            a[i][j]=sys.maxsize
            for k in range(i,j):
                cost=a[i][k]+a[k+1][j]+M[i][0]*M[k][1]*M[j][1]
                if cost<a[i][j]:
                    a[i][j]=cost
    print(a)
    return a[0][n-1]
if __name__=="__main__":
    M=[[5,6],[6,8],[8,3],[3,4],[4,5]]
    print(matrix(M))
    m=[[1,2],[2,3],[3,4]]
    print(matrix(m))
