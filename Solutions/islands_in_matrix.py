def numIslands(matrix):
  if not matrix:
    return 0

  def dfs(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(
        matrix[0]) or matrix[i][j] != 1:
      return
    matrix[i][j] = "#"
    dfs(matrix, i + 1, j)
    dfs(matrix, i - 1, j)
    dfs(matrix, i, j + 1)
    dfs(matrix, i, j - 1)

  count = 0
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 1:
        dfs(matrix, i, j)
        count += 1

  return count


# Example usage:
matrix = [[1, 0, 0, 0, 0], 
          [0, 0, 1, 1, 0], 
          [0, 1, 1, 0, 0], 
          [0, 0, 0, 0, 0],
          [1, 1, 0, 0, 1], 
          [1, 1, 0, 0, 1]]

print(numIslands(matrix))  # Output should be 4
