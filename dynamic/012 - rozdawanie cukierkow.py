"""
Alice is a kindergarten teacher. She wants to give some candies to the children in her class. 
All the children sit in a line and each of them has a rating score according to his or her performance in the class. 
Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the 
higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.

For example, assume her students' ratings are [4, 6, 4, 5, 6, 2]. She gives the students candy in the following minimal
 amounts: [1, 2, 1, 2, 3, 1]. She must buy a minimum of 10 candies. 

"""


def candies(n, arr):
    counter=[1]*n
    for i in range(1,n):
        if arr[i-1]<arr[i]:
            counter[i]=counter[i-1]+1
    for i in range(n-1,0,-1):
        if arr[i]<arr[i-1]:
            counter[i-1]=max(counter[i-1],counter[i]+1)

    s=0
    for i in range(n):
       s+=counter[i]

    return s




arr=[2,4,2,6,1,7,8,9,2,1]
print(candies(len(arr),arr))
