def find_word(matrix, word):
  # Check rows
  for row in matrix:
    row_str = ''.join(row)
    if word in row_str:
      return True

  # Check columns
  for col in range(len(matrix[0])):
    col_str = ''.join(row[col] for row in matrix)
    if word in col_str:
      return True

  return False


# Example usage
matrix = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S']]

word1 = 'FOAM'
word2 = 'MASS'
word3 = 'FBOS'

result1 = find_word(matrix, word1)
result2 = find_word(matrix, word2)
result3 = find_word(matrix, word3)

print(f"Can find '{word1}' in the matrix: {result1}")
print(f"Can find '{word2}' in the matrix: {result2}")
print(f"Can find '{word3}' in the matrix: {result3}")