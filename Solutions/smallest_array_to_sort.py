def find_unsorted_window(arr):
  n = len(arr)
  left_bound = 0
  while left_bound < n - 1 and arr[left_bound] <= arr[left_bound + 1]:
    left_bound += 1

  if left_bound == n - 1:
    return (0, 0)

  right_bound = n - 1
  while right_bound > 0 and arr[right_bound] >= arr[right_bound - 1]:
    right_bound -= 1

  min_val = min(arr[left_bound:right_bound + 1])
  max_val = max(arr[left_bound:right_bound + 1])

  while left_bound > 0 and arr[left_bound - 1] > min_val:
    left_bound -= 1

  while right_bound < n - 1 and arr[right_bound + 1] < max_val:
    right_bound += 1

  return (left_bound, right_bound)


# Example usage:
arr = [3, 7, 5, 8, 6, 10, 9]
print(find_unsorted_window(arr))
