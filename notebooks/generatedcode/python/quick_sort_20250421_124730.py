# Generated on: 2025-04-21 12:47:30

Certainly! Below is an implementation of the quick sort algorithm in Python:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage
array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quick_sort(array)
print(sorted_array)
```

In this code, the `quick_sort` function is defined, which takes an array `arr` as input and recursively sorts it using the quick sort algorithm. The base case is when the array has only one element, in which case it returns the array as is. Otherwise, a pivot element is selected and the array is partitioned into two sub-arrays, one containing elements less than or equal to the pivot, and the other containing elements greater than the pivot. The function then recursively applies quick sort to each sub-array and combines them along with the pivot element to produce the sorted array.