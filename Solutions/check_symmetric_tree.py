class TreeNode:

  def __init__(self, val=0, children=None):
    self.val = val
    self.children = children if children is not None else []


def is_symmetric(root):
  if root is None:
    return True
  return is_mirror(root, root)


def is_mirror(node1, node2):
  if node1 is None and node2 is None:
    return True
  if node1 is None or node2 is None:
    return False
  if node1.val != node2.val:
    return False
  if len(node1.children) != len(node2.children):
    return False
  for c1, c2 in zip(node1.children, reversed(node2.children)):
    if not is_mirror(c1, c2):
      return False
  return True


# Example usage
if __name__ == "__main__":
  root = TreeNode(4, [
    TreeNode(3, [TreeNode(9)]),
    TreeNode(5),
    TreeNode(3, [TreeNode(9), TreeNode(1)])
  ])

  print(is_symmetric(root))  # Output: True
