class TreeNode:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def evaluate_expression_tree(root):
  if root is None:
    return 0

  # If the node is a leaf, return its value
  if root.left is None and root.right is None:
    return root.value

  # Recursively evaluate left and right subtrees
  left_value = evaluate_expression_tree(root.left)
  right_value = evaluate_expression_tree(root.right)

  # Perform the corresponding arithmetic operation
  if root.value == '+':
    return left_value + right_value
  elif root.value == '-':
    return left_value - right_value
  elif root.value == '*':
    return left_value * right_value
  elif root.value == '/':
    # Check for division by zero
    if right_value == 0:
      raise ValueError("Division by zero")
    return left_value / right_value
  else:
    raise ValueError("Invalid operator")


# Example usage:
# Construct the given tree
root = TreeNode('*')
root.left = TreeNode('-')
root.right = TreeNode('+')
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# Evaluate the expression tree
result = evaluate_expression_tree(root)
print(result)
