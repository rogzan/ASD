"""

W jednej z chińskich prowincji postanowiono wybudować serię maszyn chroniących ludzkość przed koronawirusem.
Prowincję można zobrazować jako tablicę wartości 1 i 0, gdzie arr[i]=1 oznacza, że w mieście i można zbudować maszynę,
a wartość 0, że nie można. Dana jest również liczba k, która oznacza, że jeśli postawimy maszynę w mieście i, to miasta
o indeksach j takich, że abs(i-j)<k są przez nią chronione.
Należy zaproponować algorytm, który stwierdzi ile minimalnie maszyn potrzeba aby zapewnić ochronę w każdym mieście, lub
-1 jeśli jest to niemożliwe.
"""


def mach(cities, k):

    protected=[False]*len(cities)
    i=0
    counter=0
    while i<len(cities):
        if protected[i]:
            i+=1
        else:
            j=k
            while i+j>=len(cities):
                j-=1

            while cities[i+j]!=1 and j>0:
                j-=1
            if j==i and cities[i]==0:
                return -1
            p=k
            while p>=0:
                if i+j+p<len(cities):
                    protected[i+j+p]=True
                if i+j-p>=0:
                    protected[i+j-p]=True
                p-=1
            if i+j<len(cities):
                i+=j
            else:
                i+=1
            counter+=1


    return counter

if __name__=="__main__":

    cities=[1,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0]
    print(mach(cities,3))
