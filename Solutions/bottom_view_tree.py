class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def bottom_view(root):
  if not root:
    return []

  # Dictionary to store the horizontal distance and corresponding node value
  horizontal_distance = {}

  # Stack to perform DFS traversal
  stack = [(root, 0)]  # (node, horizontal distance)

  # Traverse the tree
  while stack:
    node, hd = stack.pop()

    # Update horizontal distance and value for the current node
    horizontal_distance[hd] = node.val

    # Traverse left child
    if node.left:
      stack.append((node.left, hd - 1))

    # Traverse right child
    if node.right:
      stack.append((node.right, hd + 1))

  # Sort the keys (horizontal distances)
  sorted_hds = sorted(horizontal_distance.keys())

  # Retrieve the bottom view nodes in the sorted order of horizontal distance
  bottom_view_nodes = [horizontal_distance[hd] for hd in sorted_hds]

  return bottom_view_nodes


# Example usage:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(0)
root.right.right.left = TreeNode(8)

print(bottom_view(root))  # Output: [0, 1, 3, 6, 8, 9]
