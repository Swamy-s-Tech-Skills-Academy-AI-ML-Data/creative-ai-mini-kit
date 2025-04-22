# Generated on: 2025-04-21 12:47:27

Here's a sample implementation of binary search in Python:

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
```

You can use this function to find the index of a target element in a sorted array by calling `binary_search(arr, target)`. If the target is found, it returns the index; otherwise, it returns -1.