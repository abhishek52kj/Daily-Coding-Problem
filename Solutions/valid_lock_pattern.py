class Solution:

  def numberOfPatterns(self, N: int) -> int:
    self.skip = [[0] * 10 for _ in range(10)]
    self.skip[1][3] = self.skip[3][1] = 2
    self.skip[1][7] = self.skip[7][1] = 4
    self.skip[3][9] = self.skip[9][3] = 6
    self.skip[7][9] = self.skip[9][7] = 8
    self.skip[1][9] = self.skip[9][1] = self.skip[2][8] = self.skip[8][
      2] = self.skip[3][7] = self.skip[7][3] = self.skip[4][6] = self.skip[6][
        4] = 5
    self.visited = [False] * 10
    self.result = 0
    self.dfs(1, 1, N - 1) * 4
    self.result += self.dfs(2, 1, N - 1) * 4
    self.result += self.dfs(5, 1, N - 1)
    return self.result

  def dfs(self, num, length, N):
    if length == N:
      return 1
    self.visited[num] = True
    count = 0
    for next_num in range(1, 10):
      if not self.visited[next_num] and (
          self.skip[num][next_num] == 0
          or self.visited[self.skip[num][next_num]]):
        count += self.dfs(next_num, length + 1, N)
    self.visited[num] = False
    return count


# Example usage:
solution = Solution()
print(solution.numberOfPatterns(9))  # Example usage
