def edit_distance(str1, str2):
  m = len(str1)
  n = len(str2)

  # Create a matrix to store the edit distances
  dp = [[0] * (n + 1) for _ in range(m + 1)]

  # Initialize the matrix
  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0:
        dp[i][
          j] = j  # If the first string is empty, insert all characters of the second string
      elif j == 0:
        dp[i][
          j] = i  # If the second string is empty, insert all characters of the first string
      elif str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1]  # Characters match, no operation needed
      else:
        dp[i][j] = 1 + min(
          dp[i - 1][j],  # Deletion
          dp[i][j - 1],  # Insertion
          dp[i - 1][j - 1])  # Substitution

  return dp[m][n]


# Example usage
str1 = "kitten"
str2 = "sitting"
result = edit_distance(str1, str2)
print(f"The edit distance between '{str1}' and '{str2}' is {result}")
