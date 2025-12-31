def findMinIndex(arr):
    if arr is None:
        raise ValueError("Input array cannot be None.")

    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")

    if len(arr) == 0:
        return []

    if len(arr) == 1:
        return 1
    
    if len(arr) <= 1:
        return False

    low = 0
    high = len(arr) - 1
    minIndex = -1

    while low <= high:

        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if arr[mid1] == arr[mid2]:
            low = mid1 + 1
            high = mid2 - 1
            minIndex = mid1
        elif arr[mid1] < arr[mid2]:
            high = mid2 - 1
            minIndex = mid1
        else:
            low = mid1 + 1
            minIndex = mid2

    return minIndex


array = [9, 7, 2, 1, 3, 6, 10]
print("Array:", array)
index = findMinIndex(array)
print("Minimum element fount at :", index)