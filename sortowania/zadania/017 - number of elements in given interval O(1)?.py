"""
Zaproponuj klasę reprezentującą strukturę danych, która w konstruktorze dostaje tablicę liczb naturalnych długości n
o zakresie wartości [0,k]. Ma ona posiadać metodę count_num_in_range(a,b) - ma ona zwracać informację o tym, ile liczb
w zakresie [a,b] było w tablicy, ma działać w czasie O(1).
Można założyć, że zawsze a>=1, b<=k


"""

class str:

    def __init__(self,arr,k):
        counter=[0]*k

        for i in range(len(arr)):
            counter[arr[i]]+=1

        for i in range(1,k):
            counter[i]+=counter[i-1]

        self.c=counter

    def count_num_in_range(self,a,b):

        return self.c[b]-self.c[a]+1



    
if __name__=="__main__":

    arr=[5,3,4,2,3,4,2,3,4,5,3,2,3,6,7,3,4,5,6,7,8,9,1,2,3,4,5,6,7,4,3]
    Struktura=str(arr,10)
    k=Struktura.count_num_in_range(1,2)
    print(k)
