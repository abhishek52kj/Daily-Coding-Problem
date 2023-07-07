class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def count_unival_subtrees(root):
  count = 0

  def is_unival(node):
    nonlocal count

    if node is None:
      return True

    left_unival = is_unival(node.left)
    right_unival = is_unival(node.right)

    if (left_unival and right_unival
        and (node.left is None or node.left.val == node.val)
        and (node.right is None or node.right.val == node.val)):
      count += 1
      return True
    else:
      return False

  is_unival(root)
  return count


if __name__ == "__main__":
  node0 = TreeNode(0)
  node1 = TreeNode(1)
  node2 = TreeNode(0)
  node3 = TreeNode(1)
  node4 = TreeNode(0)
  node5 = TreeNode(1)
  node6 = TreeNode(1)

  node0.left = node1
  node0.right = node2
  node2.left = node3
  node2.right = node4
  node3.left = node5
  node3.right = node6

  unival_count = count_unival_subtrees(node0)
  print("Number of unival subtrees:", unival_count)
