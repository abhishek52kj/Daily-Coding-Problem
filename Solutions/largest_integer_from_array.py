def largest_number(arr):
  # Convert numbers to strings for custom sorting
  arr = list(map(str, arr))

  # Define a custom comparison function
  def custom_compare(x, y):
    return int(x + y) - int(y + x)

  # Sort the array using the custom comparison function
  arr.sort(key=lambda x: (x, int(x)), reverse=True)

  # Concatenate the sorted strings to form the largest number
  result = ''.join(arr)

  return int(result)


# Example usage:
numbers = [10, 7, 76, 415, 9]
result = largest_number(numbers)
print(result)
