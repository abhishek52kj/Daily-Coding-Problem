class Graph:

  def __init__(self, vertices):
    self.V = vertices
    self.graph = []

  def add_edge(self, u, v, w):
    self.graph.append([u, v, w])

  def find(self, parent, i):
    if parent[i] == i:
      return i
    return self.find(parent, parent[i])

  def union(self, parent, rank, x, y):
    x_root = self.find(parent, x)
    y_root = self.find(parent, y)

    if rank[x_root] < rank[y_root]:
      parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
      parent[y_root] = x_root
    else:
      parent[y_root] = x_root
      rank[x_root] += 1

  def max_spanning_tree(self):
    result = []

    self.graph = sorted(self.graph, key=lambda item: item[2], reverse=True)

    parent = []
    rank = []

    for node in range(self.V):
      parent.append(node)
      rank.append(0)

    i = 0
    e = 0

    while e < self.V - 1:
      u, v, w = self.graph[i]
      i = i + 1
      x = self.find(parent, u)
      y = self.find(parent, v)

      if x != y:
        e = e + 1
        result.append([u, v, w])
        self.union(parent, rank, x, y)

    max_spanning_tree = Graph(self.V)
    for u, v, weight in result:
      max_spanning_tree.add_edge(u, v, weight)

    return max_spanning_tree


if __name__ == "__main__":
  g = Graph(4)
  g.add_edge(0, 1, 10)
  g.add_edge(0, 2, 6)
  g.add_edge(0, 3, 5)
  g.add_edge(1, 3, 15)
  g.add_edge(2, 3, 4)

  max_spanning_tree = g.max_spanning_tree()
  print("Edges in the Maximum Spanning Tree:")
  for u, v, weight in max_spanning_tree.graph:
    print(f"{u} -- {v} == {weight}")
