def minSwapsCouples(row):
  min_swaps = 0
  couple_map = {val: idx for idx, val in enumerate(row)}

  for i in range(0, len(row), 2):
    couple = row[i] // 2
    if row[i + 1] != row[i] ^ 1:
      min_swaps += 1
      other_couple_idx = couple_map[couple * 2 + (row[i] ^ 1)]
      row[i + 1], row[other_couple_idx] = row[other_couple_idx], row[i + 1]
      couple_map[row[other_couple_idx]] = other_couple_idx

  return min_swaps


# Example usage:
row = [0, 2, 1, 3]  # Example arrangement of couples
print(minSwapsCouples(row))  # Output: 1
