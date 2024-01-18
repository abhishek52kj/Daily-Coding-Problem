class TreeNode:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def find_deepest_node(root):
  if not root:
    return None

  queue = [root]

  while queue:
    node = queue.pop(0)

    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)

  return node.value


# Example usage:
# Construct the tree
root = TreeNode('a')
root.left = TreeNode('b')
root.right = TreeNode('c')
root.left.left = TreeNode('d')
root.right.right = TreeNode('e')
root.right.right.left = TreeNode('f')

# Find the deepest node
deepest_node = find_deepest_node(root)
print("Deepest Node:", deepest_node)
