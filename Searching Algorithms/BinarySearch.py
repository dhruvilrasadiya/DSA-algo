def binary_search(arr, target):

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

    length = len(arr)


    left, right = 0, length - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


    return -1


array = [11, 12, 22, 25, 64]
target = 25
print("Array:", array)
print("Target:", target)
index = binary_search(array, target)
print("Target element fount at :", index)