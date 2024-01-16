def cherryPickup(grid):
  if not grid or grid[0][0] == -1 or grid[-1][-1] == -1:
    return -1

  n = len(grid)
  memo = {}

  def dp(r1, c1, r2):
    c2 = r1 + c1 - r2

    if r1 == c1 == r2 == 0:
      return grid[0][0]

    if r1 < 0 or c1 < 0 or r2 < 0 or c2 < 0 or grid[r1][c1] == -1 or grid[r2][
        c2] == -1:
      return float('-inf')

    if (r1, c1, r2) in memo:
      return memo[(r1, c1, r2)]

    cherries = grid[r1][c1]
    if r1 != r2:
      cherries += grid[r2][c2]

    cherries += max(dp(r1 - 1, c1, r2 - 1), dp(r1, c1 - 1, r2),
                    dp(r1 - 1, c1, r2), dp(r1, c1 - 1, r2 - 1))

    memo[(r1, c1, r2)] = cherries
    return cherries

  result = max(0, dp(n - 1, n - 1, n - 1))
  return result if result != float('-inf') else -1


grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
grid2 = [[1, 1, 1, 0, 0], [1, 1, 1, 0, 1], [1, 1, 1, 0, 0], [1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1]]
grid3 = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0],
         [0, 1, 1, 1, 1]]
result = cherryPickup(grid3)
print(result)
