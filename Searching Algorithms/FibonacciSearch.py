def FibonacciSearch(arr, x):
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
    
    n = len(arr)
    a =  0
    b = 1
    c = 1
 
    while c < n:
        a = b
        b = c
        c = a + b
    offset = -1
 
    while c > 1:
        i = min(offset + a, n - 1)
 
        if arr[i] < x:
            c = b
            b = a
            a = c - b
            offset = i
        elif arr[i] > x:
            c = a
            b = b - a
            a = c - b
        else:
            return i
 
    if b and arr[offset + 1] == x:
        return offset + 1
 
    return -1

array = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(array)
target = 33
print("Array:", array)
print("Target:", target)
index = FibonacciSearch(array, target)
print("Target element fount at :", index)