class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def remove_single_child_nodes(root):
  if root is None:
    return None

  root.left = remove_single_child_nodes(root.left)
  root.right = remove_single_child_nodes(root.right)

  if root.left is None and root.right is None:
    return root

  if root.left is None:
    return root.right

  if root.right is None:
    return root.left

  return root


def print_tree(root):
  if root:
    print(root.val, end=' ')
    print_tree(root.left)
    print_tree(root.right)


# Example tree construction
root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.left.left.right = TreeNode(5)
root.right = TreeNode(2)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(7)

# Convert tree to full binary tree
root = remove_single_child_nodes(root)

# Print the modified tree
print_tree(root)
