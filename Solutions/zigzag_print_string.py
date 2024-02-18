def print_zigzag(string, k):
  
  if k == 1:
      print(string)
      return

  rows = [""] * k
  row = 0
  down = True

  for i, char in enumerate(string):
      rows[row] += char

      # Calculate spacing
      spacing = 2 * (k - 1)  
      if row > 0 and row < k - 1:
          spaces = spacing - 2 * row if down else 2 * row
          rows[row] += " " * spaces

      if row == 0:
          down = True
      elif row == k - 1:
          down = False

      if down:
          row += 1
      else:
          row -= 1

  print('\n'.join(rows))

# Example usage
string = "thisisazigzag"
k = 4
print_zigzag(string, k)
