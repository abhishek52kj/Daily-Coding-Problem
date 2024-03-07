def binary_search(arr, x):
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == x:
      return True
    elif arr[mid] < x:
      left = mid + 1
    else:
      right = mid - 1
  return False


# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
print(binary_search(arr, x))  # Output: True
