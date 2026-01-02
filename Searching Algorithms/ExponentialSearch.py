def binarySearch( arr, l, r, x):
    if r >= l:
        mid = l + ( r-l ) // 2
        
        if arr[mid] == x:
            return mid
        
        if arr[mid] > x:
            return binarySearch(arr, l, 
                                mid - 1, x)
        return binarySearch(arr, mid + 1, r, x)
        
    return -1

def exponentialSearch(arr, n, x):
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
    
    if arr[0] == x:
        return 0
        
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    
    return binarySearch( arr, i // 2, 
                         min(i, n-1), x)


array = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(array)
target = 42
print("Array:", array)
print("Target:", target)
index = exponentialSearch(array, n, target)
print("Target element fount at :", index)
