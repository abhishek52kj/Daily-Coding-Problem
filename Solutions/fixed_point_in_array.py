def find_fixed_point(arr):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == mid:
      return mid
    elif arr[mid] < mid:
      left = mid + 1
    else:
      right = mid - 1

  return False


# Example usage:
arr1 = [-6, 0, 2, 40]
arr2 = [1, 5, 7, 8]

print(find_fixed_point(arr1))  # Output: 2
print(find_fixed_point(arr2))  # Output: False
