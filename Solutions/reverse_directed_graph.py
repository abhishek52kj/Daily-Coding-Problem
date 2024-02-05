from collections import defaultdict


class Graph:

  def __init__(self):
    self.graph = defaultdict(list)

  def add_edge(self, u, v):
    self.graph[u].append(v)

  def reverse_graph(self):
    reversed_graph = Graph()

    for node in self.graph:
      for neighbor in self.graph[node]:
        reversed_graph.add_edge(neighbor, node)

    return reversed_graph

  def print_graph(self):
    for node in self.graph:
      for neighbor in self.graph[node]:
        print(f"{node} -> {neighbor}")


def main():
  # Create a directed graph
  graph = Graph()
  graph.add_edge('A', 'B')
  graph.add_edge('B', 'C')

  print("Original Graph:")
  graph.print_graph()

  # Compute the reversal of the graph
  reversed_graph = graph.reverse_graph()

  print("\nReversed Graph:")
  reversed_graph.print_graph()


if __name__ == "__main__":
  main()
