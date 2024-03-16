def dfs(node, adj_list, visited, group):
  visited[node] = True
  group.add(node)
  for neighbor in adj_list[node]:
    if not visited[neighbor]:
      dfs(neighbor, adj_list, visited, group)


def count_friend_groups(adj_list):
  visited = {node: False for node in adj_list}
  groups = []
  for node in adj_list:
    if not visited[node]:
      group = set()
      dfs(node, adj_list, visited, group)
      groups.append(group)
  return len(groups)


# Example adjacency list representing friendships
adj_list = {0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]}

# Count friend groups
num_groups = count_friend_groups(adj_list)
print("Number of friend groups in the class:", num_groups)
