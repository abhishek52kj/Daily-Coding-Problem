class TreeNode:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class Solution:

  def maxPathSum(self, root):
    self.max_sum = float('-inf')

    def max_path_sum_helper(node):
      if not node:
        return 0

      # Calculate the maximum path sum starting from the left and right subtrees
      left_max = max(0, max_path_sum_helper(node.left))
      right_max = max(0, max_path_sum_helper(node.right))

      # Update the maximum path sum considering the current node
      self.max_sum = max(self.max_sum, left_max + right_max + node.value)

      # Return the maximum path sum that can be extended from the current node
      return max(left_max, right_max) + node.value

    max_path_sum_helper(root)
    return self.max_sum


#       10
#      / \
#     2   10
#    / \    \
#   20  1   -25
#            / \
#           3   4

tree = TreeNode(10)
tree.left = TreeNode(2)
tree.right = TreeNode(10)
tree.left.left = TreeNode(20)
tree.left.right = TreeNode(1)
tree.right.right = TreeNode(-25)
tree.right.right.left = TreeNode(3)
tree.right.right.right = TreeNode(4)

solution = Solution()
result = solution.maxPathSum(tree)
print("Maximum Path Sum:", result)
