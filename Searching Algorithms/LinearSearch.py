def linear_search(arr, target):
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

    for index in range(length):
        if arr[index] == target:
            return index
    return -1


array = ["64", "25", "12", "22", "11"]
target = "11"
print("Array:", array)
print("Target:", target)
index = linear_search(array, target)
print("Target element fount at :", index)