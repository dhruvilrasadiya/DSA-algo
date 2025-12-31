import math

def jump_search(arr, target):

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

    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0


    while prev < n:
        try:
            if arr[min(step, n) - 1] >= target:
                break
        except Exception:
            return -1
        prev = step
        step += int(math.sqrt(n))

        if prev >= n:
            return -1
        
    for i in range(prev, min(step, n)):
        try:
            if arr[i] == target:
                return i
        except Exception:
            return -1

    return -1

array = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
target = 55
print("Array:", array)
print("Target:", target)
index = jump_search(array, target)
print("Target element fount at :", index)