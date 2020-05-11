"""

Dana jest lista zleceń. Każde zlecenie wymaga pewnego kapitału początkowego C, który należy mieć,
żeby zacząć zlecenie oraz zysk P, który doda się do naszego całkowitego kapitału, gdy wykonamy zlecenie.
Mając kapitał początkowy W i liczbę k wybierz co najwyżej k zleceń tak, że skończysz z maksymalnym
możliwym kapitałem.

"""

def quickSort(arr,left,right):
    if left<right:
        pi=partition(arr,left,right)
        quickSort(arr,left,pi-1)
        quickSort(arr,pi+1,right)

def partition(arr,left,right):
    i=left-1
    pivot=arr[right][1]-arr[right][0]
    for j in range(left,right):
        if arr[j][1]-arr[j][0]>=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]
    return i+1


def maxProfit(tasks,w,k):

    taken=[False]*len(tasks)
    #sortujemy po różnicy pomiędzy kapitałem poczatkowym a profitem

    quickSort(tasks,0,len(tasks)-1)
    print(tasks)
    result=[]
    for i in range(k):
        t = True
        for j in range(len(tasks)):

            if taken[j]==False and tasks[j][0]<=w and t:
                taken[j]=True
                result.append(tasks[j])
                w=w-tasks[j][0]+tasks[j][1]
                t=False
    print(result)


if __name__=="__main__":
    tasks=[[0,2],[1,5],[0,1],[2,8],[3,10],[2,3],[0,5],[1,4]]
    maxProfit(tasks,0,3)
