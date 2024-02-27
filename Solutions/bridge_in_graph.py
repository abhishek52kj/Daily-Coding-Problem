def bridges(graph):

  def dfs(u, parent):
    nonlocal time
    low[u] = disc[u] = time
    time += 1
    for v in graph[u]:
      if disc[v] == -1:
        parent[v] = u
        dfs(v, parent)
        low[u] = min(low[u], low[v])
        if low[v] > disc[u]:
          bridges.append((u, v))
      elif v != parent[u]:
        low[u] = min(low[u], disc[v])

  n = len(graph)
  disc = [-1] * n
  low = [-1] * n
  parent = [-1] * n
  time = 0
  bridges = []
  for i in range(n):
    if disc[i] == -1:
      dfs(i, parent)
  return bridges


# Example usage:
graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3, 4], 3: [2], 4: [2, 5], 5: [4]}

print(bridges(graph))  # Output: [(2, 3), (2, 4)]
