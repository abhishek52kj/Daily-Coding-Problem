def min_jumps(arr):
  if not arr or len(arr) <= 1:
    return 0

  n = len(arr)
  jumps = [0] * n

  for i in range(n - 2, -1, -1):
    if arr[i] == 0:
      jumps[i] = float('inf')
    elif arr[i] >= n - i - 1:
      jumps[i] = 1
    else:
      min_jump = float('inf')
      for j in range(i + 1, min(i + arr[i] + 1, n)):
        min_jump = min(min_jump, jumps[j])

      if min_jump != float('inf'):
        jumps[i] = min_jump + 1
      else:
        jumps[i] = float('inf')

  return jumps[0] if jumps[0] != float('inf') else -1


# Test the function
arr = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
print(min_jumps(arr))  # Output: 2
