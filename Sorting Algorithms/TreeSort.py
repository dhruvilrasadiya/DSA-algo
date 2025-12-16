class TreeNode:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    else:
        root.count += 1
    
    return root


def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.extend([root.value] * root.count)
        inorder_traversal(root.right, result)


def tree_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    
    if len(arr) <= 1:
        return arr
    
    for x in arr:
        if x is None:
            raise ValueError("List contains None.")
        if not isinstance(x, (int, float, str)):
            raise TypeError("Unsupported data type in list.")

    root = None

    for value in arr:
        root = insert(root, value)

    sorted_arr = []
    inorder_traversal(root, sorted_arr)

    return sorted_arr


unsorted_array = [64, 25, 12, 22, 11]
print("Unsorted array:", unsorted_array)
sorted_array = tree_sort(unsorted_array)
print("Sorted array:", sorted_array)
