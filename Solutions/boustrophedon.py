class Node:

  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def print_boustrophedon(root):
  if root is None:
    return []  # Handle empty tree case

  result = []
  queue = [root]  # Use a queue for level-order traversal
  left_to_right = True

  while queue:
    level_size = len(queue)
    current_level = []

    for _ in range(level_size):
      node = queue.pop(0)
      current_level.append(node.val)

      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

    if not left_to_right:
      current_level.reverse()  # Reverse if right-to-left

    result += current_level
    left_to_right = not left_to_right  # Alternate directions

  return result


# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

print(print_boustrophedon(root))
