#Consider a big party where a log register for guest’s entry and exit times is maintained.
#Find the time at which there are maximum guests in the party. Note that entries in register are not in any order.


def partition(arr,left,right):
    i=left-1
    pivot=arr[right]
    for j in range(left,right):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]

    return i+1


def quickSort(arr,left,right):
    if left<right:
        pi=partition(arr,left,right)
        quickSort(arr,left,pi-1)
        quickSort(arr,pi+1,right)


def maxGuests(arrival,exit):

    quickSort(arrival,0,len(arrival)-1)
    quickSort(exit,0,len(exit)-1)

    time=arrival[0]
    guests=1
    max_guests=1

    n=len(arrival)

    i=1
    j=0

    while i<n and j<n:
        if arrival[i] <= exit[j]:
            guests+=1
            if guests>max_guests:
                max_guests=guests
                time=arrival[i]
            i+=1
        else:
            guests-=1
            j+=1


    return (max_guests,time)
