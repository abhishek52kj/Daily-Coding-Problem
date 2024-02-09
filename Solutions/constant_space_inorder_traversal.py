class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def morris_inorder_traversal(root):
  current = root
  while current:
    if not current.left:
      print(current.val, end=" ")
      current = current.right
    else:

      pre = current.left
      while pre.right and pre.right != current:
        pre = pre.right

      if not pre.right:
        pre.right = current
        current = current.left

      else:
        pre.right = None
        print(current.val, end=" ")
        current = current.right


# Example usage:
"""
      1
     / \
    2   3
   / \
  4   5
"""
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Performing in-order traversal
print("In-order traversal:", end=" ")
morris_inorder_traversal(root)
