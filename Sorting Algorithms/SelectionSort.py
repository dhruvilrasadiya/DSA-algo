def selection_sort(arr):

    if arr is None:
        raise ValueError("Input array cannot be None.")
    
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    
    if len(arr) == 0:
        return arr

    if len(arr) == 1:
        return arr

    for element in arr:
        if not (isinstance(element, int) or isinstance(element, float)):
            raise TypeError("Array must contain only numbers (int or float).")
    
    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            try:
                if arr[j] < arr[min_idx]:
                    min_idx = j
            except Exception:
                raise TypeError(f"Elements {arr[j]} and {arr[min_idx]} cannot be compared.")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

unsorted_array = [64, 25, 12, 22, 11]
print("Unsorted array:", unsorted_array)
sorted_array = selection_sort(unsorted_array)
print("Sorted array:", sorted_array)