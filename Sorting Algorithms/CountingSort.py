def counting_sort(arr):
    if arr is None:
        raise ValueError("Input array cannot be None.")

    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")

    if len(arr) == 0:
        return []

    if len(arr) == 1:
        return arr
    
    if len(arr) <= 1:
        return arr

    for element in arr:
        if not (isinstance(element, int) or isinstance(element, float)):
            raise TypeError("Array must contain only numbers (int or float).")

    n = len(arr)
    maxval = max(arr)

    cntArr = [0] * (maxval + 1)

    for v in arr:
        cntArr[v] += 1

    for i in range(1, maxval + 1):
        cntArr[i] += cntArr[i - 1]

    ans = [0] * n
    for i in range(n - 1, -1, -1):
        v = arr[i]
        ans[cntArr[v] - 1] = v
        cntArr[v] -= 1

    return ans

unsorted_array = [64, 25, 12, 22, 11]
print("Unsorted array:", unsorted_array)
sorted_array = counting_sort(unsorted_array)
print("Sorted array:", sorted_array)