def find_min_max(arr):
  n = len(arr)
  if n == 0:
    return None, None
  elif n == 1:
    return arr[0], arr[0]

  if arr[0] < arr[1]:
    min_val = arr[0]
    max_val = arr[1]
  else:
    min_val = arr[1]
    max_val = arr[0]

  for i in range(2, n - 1, 2):
    if arr[i] < arr[i + 1]:
      if arr[i] < min_val:
        min_val = arr[i]
      if arr[i + 1] > max_val:
        max_val = arr[i + 1]
    else:
      if arr[i + 1] < min_val:
        min_val = arr[i + 1]
      if arr[i] > max_val:
        max_val = arr[i]

  if n % 2 == 1:
    if arr[-1] < min_val:
      min_val = arr[-1]
    elif arr[-1] > max_val:
      max_val = arr[-1]

  return min_val, max_val


if __name__ == "__main__":
  arr = [3, 6, 1, 8, 2, 4, 10, 5, 7, 9]
  min_val, max_val = find_min_max(arr)
  print("Minimum:", min_val)
  print("Maximum:", max_val)
