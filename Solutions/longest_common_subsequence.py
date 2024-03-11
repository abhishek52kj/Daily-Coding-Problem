def longest_common_subsequence_length(str1, str2, str3):
  m = len(str1)
  n = len(str2)
  o = len(str3)

  # Initialize a 3D table to store lengths of LCS
  # dp[i][j][k] will store the length of LCS of str1[0..i-1], str2[0..j-1], str3[0..k-1]
  dp = [[[0] * (o + 1) for _ in range(n + 1)] for _ in range(m + 1)]

  # Fill the dp table in a bottom-up manner
  for i in range(m + 1):
    for j in range(n + 1):
      for k in range(o + 1):
        if i == 0 or j == 0 or k == 0:
          dp[i][j][k] = 0
        elif str1[i - 1] == str2[j - 1] == str3[k - 1]:
          dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
        else:
          dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

  return dp[m][n][o]


# Example usage
str1 = "epidemiologist"
str2 = "refrigeration"
str3 = "supercalifragilisticexpialodocious"
print("Length of longest common subsequence:",
      longest_common_subsequence_length(str1, str2, str3))
