def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def tim_sort(arr):

    if arr is None:
        raise ValueError("Input array cannot be None.")

    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")

    if len(arr) == 0:
        return []

    if len(arr) == 1:
        return arr

    for element in arr:
        if not (isinstance(element, int) or isinstance(element, float)):
            raise TypeError("Array must contain only numbers (int or float).")
        
    n = len(arr)

    minrun = 32
    for i in range(0, n, minrun):
        insertion_sort(arr, i, min(i + minrun - 1, n - 1))

    size = minrun
    while size < n:
        for l in range(0, n, 2 * size):
            m = l + size - 1
            r = min((l + 2 * size - 1), (n - 1))

            if m < r:
                merge(arr, l, m, r)

        size *= 2

    return arr



unsorted_array = [64, 25, 12, 22, 11]
print("Unsorted array:", unsorted_array)
sorted_array = tim_sort(unsorted_array)
print("Sorted array:", sorted_array)

