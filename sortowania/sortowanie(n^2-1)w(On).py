def countSort(arr, n, exp):
    output = [0] * n
    count = [0] * n

    for i in range(n):
        count[(arr[i] // exp) % n] += 1
    for i in range(1, n):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        output[count[(arr[i] // exp) % n] - 1] = arr[i]
        count[(arr[i] // exp) % n] -= 1
    for i in range(n):
        arr[i] = output[i]

#  size n using Radix Sort
def sort(arr):
    n = len(arr)
    # Do counting sort for first digit in base n.
    # Note that instead of passing digit number,
    # exp (n^0 = 1) is passed.
    countSort(arr, n, 1)
    # Do counting sort for second digit in base n.
    # Note that instead of passing digit number,
    # exp (n^1 = n) is passed.
    countSort(arr, n, n)

arr = [40, 12, 45, 32, 33, 1, 22]
sort(arr)
print(*arr) 

# https://www.geeksforgeeks.org/sort-n-numbers-range-0-n2-1-linear-time/
