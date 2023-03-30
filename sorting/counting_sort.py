def countingSort(A, k):
    output = [0] * len(A)
    count = [0] * (k+1)

    # Store the count of each elements in count array
    for i in range(len(A)):
        count[A[i]] += 1

    # Store the cummulative count
    for i in range(1, k):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    for i in range(len(A)-1,-1,-1):
        output[count[A[i]] - 1] = A[i]
        count[A[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, len(A)):
        A[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data,10)
print(data)
