def transitive_closure(graph):

  n = len(graph)
  M = [[0 for _ in range(n)] for _ in range(n)]

  # Initialize the adjacency matrix with the direct connections
  for i, neighbors in enumerate(graph):
    for neighbor in neighbors:
      M[i][neighbor] = 1

  # Use Floyd-Warshall algorithm to find transitive closure
  for k in range(n):
    for i in range(n):
      for j in range(n):
        M[i][j] |= M[i][k] & M[k][j]

  return M


# Example usage
graph = [[0, 1, 3], [1, 2], [2], [3]]

transitive_closure_matrix = transitive_closure(graph)

print(transitive_closure_matrix)
