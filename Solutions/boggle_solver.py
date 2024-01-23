class TrieNode:

  def __init__(self):
    self.children = {}
    self.is_end_of_word = False


class BoggleSolver:

  def __init__(self, board, dictionary):
    self.board = board
    self.rows = len(board)
    self.cols = len(board[0])
    self.words_found = set()

    self.root = TrieNode()
    for word in dictionary:
      node = self.root
      for char in word:
        node = node.children.setdefault(char, TrieNode())
      node.is_end_of_word = True

  def is_valid_position(self, row, col, visited):
    return 0 <= row < self.rows and 0 <= col < self.cols and not visited[row][
      col]

  def dfs(self, row, col, node, current_word, visited):
    if node.is_end_of_word:
      self.words_found.add(current_word)

    visited[row][col] = True

    for i in range(max(0, row - 1), min(self.rows, row + 2)):
      for j in range(max(0, col - 1), min(self.cols, col + 2)):
        if self.is_valid_position(i, j, visited):
          next_char = self.board[i][j]
          next_node = node.children.get(next_char)
          if next_node:
            self.dfs(i, j, next_node, current_word + next_char, visited)

    visited[row][col] = False

  def solve(self):
    visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

    for i in range(self.rows):
      for j in range(self.cols):
        start_char = self.board[i][j]
        start_node = self.root.children.get(start_char)
        if start_node:
          self.dfs(i, j, start_node, start_char, visited)

    return self.words_found


boggle_board = [['c', 'a', 't', 's'], ['r', 'r', 'e', 't'],
                ['a', 'o', 'o', 'a'], ['b', 'n', 'n', 'e']]

word_dictionary = [
  "cat", "rat", "bat", "roar", "tone", "none", "toe", "not", "notate"
]

solver = BoggleSolver(boggle_board, word_dictionary)
result = solver.solve()

print("Words found:", result)
