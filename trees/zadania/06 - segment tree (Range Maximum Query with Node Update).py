# Given an array arr[0 . . . n-1]. Find the maximum of elements from index l to r 
# where 0 <= l <= r <= n-1. Also, change the value of a specified element of the array to a new value x.

from math import ceil,log 

def getMid(s, e): 
    return s + (e - s) // 2
 
    # st     -> Pointer to segment tree 
    # node     -> Index of current node in the segment tree . 
    # ss & se -> Starting and ending indexes of the segment represented by current node, i.e., st[node] 
    # l & r -> Starting and ending indexes of range query */ 
    
def MaxUtil(st, ss, se, l,r, node): 
    if (l <= ss and r >= se): 
        return st[node] 
    if (se < l or ss > r): 
        return -1
    mid = getMid(ss, se)   
    return max(MaxUtil(st, ss, mid, l, r,2 * node + 1),MaxUtil(st, mid + 1, se, l, r, 2 * node + 2)) 
  
def updateValue(arr, st, ss, se,index, value, node): 
    if (index < ss or index > se): 
        print("Invalid Input") 
        return
    if (ss == se): 
        arr[index] = value 
        st[node] = value 
    else: 
            mid = getMid(ss, se) 
  
            if (index >= ss and index <= mid): 
                updateValue(arr, st, ss, mid, index, value, 2 * node + 1) 
            else: 
                updateValue(arr, st, mid + 1, se, index, value, 2 * node + 2) 
            st[node] = max(st[2 * node + 1],st[2 * node + 2]) 
    return
  
# index l (query start) to r (query end). 
def getMax(st, n, l, r): 
    if (l < 0 or r > n - 1 or l > r): 
        printf("Invalid Input") 
        return -1
    return MaxUtil(st, 0, n - 1, l, r, 0) 
  
def constructSTUtil(arr, ss, se, st, si): 
    if (ss == se): 
        st[si] = arr[ss] 
        return arr[ss] 
    mid = getMid(ss, se)   
    st[si] = max(constructSTUtil(arr, ss, mid, st, si * 2 + 1), constructSTUtil(arr, mid + 1, se, st, si * 2 + 2)) 
    return st[si] 
    
def constructST(arr, n): 
    x = ceil(log(n,2)) 
    max_size = 2 * pow(2, x) - 1
    st =[0]*max_size 
    constructSTUtil(arr, 0, n - 1, st, 0) 
    return st 
  
if __name__ == '__main__': 
    arr= [1, 3, 5, 7, 9, 11] 
    n = len(arr) 
  
    # Build segment tree from given array 
    st = constructST(arr, n) 
  
    # Prmax of values in array 
    # from index 1 to 3 
    print("Max of values in given range = ",getMax(st, n, 1, 3)) 
  
    # Update: set arr[1] = 8 and update 
    # corresponding segment tree nodes. 
    updateValue(arr, st, 0, n - 1, 1, 8, 0) 
  
    # Find max after the value is updated 
    print("Updated max of values in given range = ",getMax(st, n, 1, 3)) 
    # https://www.geeksforgeeks.org/segment-tree-set-2-range-maximum-query-node-update/?ref=rp
