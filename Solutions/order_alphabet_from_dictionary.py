def find_alien_order(words):
  graph = {}
  for word in words:
    for char in word:
      if char not in graph:
        graph[char] = set()

  for i in range(len(words) - 1):
    word1 = words[i]
    word2 = words[i + 1]
    min_length = min(len(word1), len(word2))

    for j in range(min_length):
      if word1[j] != word2[j]:
        graph[word1[j]].add(word2[j])
        break
      elif j == min_length - 1 and len(word1) > len(word2):
        return []

  stack = []
  visited = set()

  def dfs(node):
    visited.add(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        dfs(neighbor)
    stack.append(node)

  for node in graph:
    if node not in visited:
      dfs(node)

  return stack[::-1]


# Test the function
words = ['xww', 'wxyw', 'wxyz', 'ywx', 'ywz']
print(find_alien_order(words))
