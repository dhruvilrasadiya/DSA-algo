def insertion_sort(arr):
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
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        try:
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
        except Exception:
            raise TypeError(f"Elements {arr[j]} and {key} cannot be compared.")
        
        arr[j + 1] = key

    return arr


unsorted_array = [64, 25, 12, 22, 11]
print("Unsorted array:", unsorted_array)
sorted_array = insertion_sort(unsorted_array)
print("Sorted array:", sorted_array)
