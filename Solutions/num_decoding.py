def num_decoding(message):
  n = len(message)
  if n == 0:
    return 0

  dp = [0] * (n + 1)
  dp[0] = 1
  dp[1] = 1 if message[0] != '0' else 0

  for i in range(2, n + 1):
    if message[i - 1] != '0':
      dp[i] += dp[i - 1]

    two_digits = int(message[i - 2:i])
    if 10 <= two_digits <= 26:
      dp[i] += dp[i - 2]

  return dp[n]


if __name__ == "__main__":
  encoded_message = '1234'
  print(num_decoding(encoded_message))
