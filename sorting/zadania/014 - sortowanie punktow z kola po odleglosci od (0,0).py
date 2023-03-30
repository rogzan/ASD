"""
Mamy dane n punktów (x, y) w okręgu o promieniu k (liczba naturalna), tzn. 0 <= x^2 + y^2 <= k, które są
w nim równomiernie rozłożone, tzn. prawdopodobieństwo znalezienia punktu na danym obszarze jest
proporcjonalne do pola tego obszaru.
Napisz algorytm, który w czasie Θ(n) posortuje punkty po ich odległości do punktu (0, 0), tzn.
d = sqrt(x^2 + y^2 ).

"""

import math

def bubbleSort(arr):
    n=len(arr)
    if n==0 or n==1:
        return

    for i in range(n):
        for j in range(n-i-1):
            d1=arr[j][0]*arr[j][0]+arr[j][1]*arr[j][1]
            d2=arr[j+1][0]*arr[j+1][0]+arr[j+1][1]*arr[j+1][1]
            if math.sqrt(d1)>math.sqrt(d2):
                arr[j],arr[j+1]=arr[j+1],arr[j]



def Sort(arr,k):

    buckets=[]
    i=1
    r=0
    first=k/(len(arr)/5)
    while(r<k):
        r=first*math.sqrt(i)
        buckets.append([])
        i+=1

    n=len(buckets)
    for i in range(len(arr)):
        p=arr[i][0]*arr[i][0]+arr[i][1]*arr[i][1]
        d=math.sqrt(p)
        norm_num=d/k
        bidx=int(n*norm_num)-1
        buckets[bidx].append(arr[i])


    for i in range(len(buckets)):
        bubbleSort(buckets[i])

    output=[]

    for i in range(len(buckets)):
        j=0
        while(j<len(buckets[i])):
            output.append(buckets[i][j])
            j+=1

    return output

    
    
if __name__=="__main__":
    arr=[[4,3],[2,1],[-1,4],[-4,3],[1,2],[-2,-1],[-0.56,3],[-3.45,2.11],[-1,2.67],[3.76,2.13],[-2.85,-3.67],[0.23,0.89],[3.98,0.45],[0,3.4],[2,2.89],[1.45,-4],[-3.56,-0.43]]
    result=Sort(arr,5)
    print(arr)
    print(result)
