def throw_dice(N, faces, total):

  dp = [[0] * (total + 1) for _ in range(N + 1)]

  dp[0][0] = 1

  for i in range(1, N + 1):
    for j in range(1, total + 1):
      for k in range(1, min(faces, j) + 1):
        dp[i][j] += dp[i - 1][j - k]

  return dp[N][total]


# Example usage
print(throw_dice(2, 6, 11))  # Output: 15
