class TreeNode:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def find_second_largest(root):
  if root is None or (root.left is None and root.right is None):
    return None

  def reverse_in_order(node):
    nonlocal second_largest, count

    if node is None or count >= 2:
      return

    reverse_in_order(node.right)

    count += 1
    if count == 2:
      second_largest = node.value
      return

    reverse_in_order(node.left)

  second_largest = None
  count = 0

  reverse_in_order(root)

  return second_largest


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(17)
root.right.right.right = TreeNode(20)

result = find_second_largest(root)
print(f"The second largest node in the BST is: {result}")
