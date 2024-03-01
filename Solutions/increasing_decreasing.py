def calculate_bonuses(lines_of_code):
  n = len(lines_of_code)
  bonuses = [1] * n

  # Forward pass to handle increasing sequences
  for i in range(1, n):
    if lines_of_code[i] > lines_of_code[i - 1]:
      bonuses[i] = bonuses[i - 1] + 1

  # Backward pass to handle decreasing sequences
  for i in range(n - 2, -1, -1):
    if lines_of_code[i] > lines_of_code[i + 1]:
      bonuses[i] = max(bonuses[i], bonuses[i + 1] + 1)

  return bonuses


# Example usage:
lines_of_code = [10, 40, 200, 1000, 60, 30]
bonuses = calculate_bonuses(lines_of_code)
print(bonuses)
