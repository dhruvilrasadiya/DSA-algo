def interpolationSearch(arr, lo, hi, x):
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

    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                       hi, x)

        if arr[pos] > x:
            return interpolationSearch(arr, lo,
                                       pos - 1, x)
    return -1


array = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(array)
target = 23
print("Array:", array)
print("Target:", target)
index = interpolationSearch(array, 0, n-1,  target)
print("Target element fount at :", index)