def maximum_product_of_three(nums):
  nums.sort()

  # The maximum product can be obtained by either multiplying the three largest numbers
  # or the two smallest numbers (if they are negative) with the largest number.

  # Case 1: All positive numbers
  product_case1 = nums[-1] * nums[-2] * nums[-3]

  # Case 2: Two smallest numbers (negative) and the largest number
  product_case2 = nums[0] * nums[1] * nums[-1]

  # Return the maximum of the two cases
  return max(product_case1, product_case2)


# Example usage:
input_list = [-10, 10, 5, 2]
result = maximum_product_of_three(input_list)
print(result)
