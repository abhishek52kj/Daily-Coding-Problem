def smallest_positive_not_sum(arr):
  result = 1  # Initialize the result

  # Traverse the array and update the result
  for num in arr:
    if num <= result:
      result += num
    else:
      break

  return result


# Example usage:
arr = [1, 2, 5, 10]
result = smallest_positive_not_sum(arr)
print(result)
