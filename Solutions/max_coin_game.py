def max_money(coins):
  n = len(coins)
  dp = [[0] * n for _ in range(n)]

  for i in range(n):
    dp[i][i] = coins[i]

  for length in range(2, n + 1):
    for i in range(n - length + 1):
      j = i + length - 1
      dp[i][j] = max(coins[i] - dp[i + 1][j], coins[j] - dp[i][j - 1])

  return dp[0][n - 1]


if __name__ == "__main__":
  coins = [5, 1, 2, 10, 6, 2]
  print("Maximum amount of money you can win:", max_money(coins))
