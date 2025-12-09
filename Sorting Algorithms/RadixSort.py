def radix_sort(arr):
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
    
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


def counting_sort_by_digit(arr, exp, base=10):
    n = len(arr)
    output = [0] * n
    count = [0] * base
    
    for num in arr:
        index = (num // exp) % base
        count[index] += 1
    
    for i in range(1, base):
        count[i] += count[i - 1]
    
    for num in reversed(arr):
        index = (num // exp) % base
        count[index] -= 1
        output[count[index]] = num
    
    return output


unsorted_array = [64, 25, 12, 22, 11]
print("Unsorted array:", unsorted_array)
sorted_array = radix_sort(unsorted_array)
print("Sorted array:", sorted_array)