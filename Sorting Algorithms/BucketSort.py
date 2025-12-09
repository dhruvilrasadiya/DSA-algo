def bucket_sort(arr):
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

    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val

    if range_val == 0:
        return arr

    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        normalized = (num - min_val) / range_val
        index = int(normalized * n)
        if index == n:
            index -= 1
        buckets[index].append(num)

    for i in range(n):
        if len(buckets[i]) > 1:
            buckets[i] = insertion_sort(buckets[i])

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket


unsorted_array = [64, 25, 12, 22, 11]
print("Unsorted array:", unsorted_array)
sorted_array = bucket_sort(unsorted_array)
print("Sorted array:", sorted_array)
