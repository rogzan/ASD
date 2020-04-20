def heapify(numbers, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and numbers[i] < numbers[l]:  largest = l
    if r < n and numbers[largest] < numbers[r]:  largest = r
    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]
        heapify(numbers, n, largest)

def heap_sort(numbers):
    n = len(numbers)
    for i in range(n//2, -1, -1):
        heapify(numbers, n, i)
    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)

p = [12, 11, 13, 5, 6, 7, -3, 12, 6, 8, 4]
print("Given array is", end="\n")
print(p)
heap_sort(p)
print("Sorted array is: ", end="\n")
print(p)
