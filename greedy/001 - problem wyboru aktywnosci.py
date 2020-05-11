"""
Activity selection problem

"""


def quickSort(arr,left,right):
    if left<right:
        pi=partition(arr,left,right)
        quickSort(arr,left,pi-1)
        quickSort(arr,pi+1,right)

def partition(arr,left,right):
    i=left-1
    pivot=arr[right][1]
    for j in range(left,right):
        if arr[j][1]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]
    return i+1



def activityProblem(time):

    quickSort(time,0,len(time)-1)
    result=[]
    result.append(time[0])

    p=0
    i=1
    while i<len(time):

        if result[p][1]<=time[i][0]:
            result.append(time[i])
            i+=1
            p+=1
        else:
            i+=1

    print(result)



if __name__=="__main__":

    time=[[1,3],[2,4],[1,7],[4,7],[2,5],[6,9],[3,5],[7,9],[9,15],[10,12],[2,10],[4,8]]
    activityProblem(time)
