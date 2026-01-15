"""
Module: Data Structures & Algorithms
Focus: Efficient searching and sorting for large-scale datasets.
"""

def binary_search(arr, target):
    """O(log n) implementation for fast data retrieval."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example: Sorting a large list of User IDs
user_ids = sorted([452, 102, 993, 204, 550])
print(f"Target found at index: {binary_search(user_ids, 204)}")
