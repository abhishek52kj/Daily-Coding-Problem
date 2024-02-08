def split_array(nums, k):
  left = max(nums)  # Minimum possible maximum sum
  right = sum(nums)  # Maximum possible maximum sum

  while left < right:
    mid = left + (right - left) // 2
    if can_partition(nums, k, mid):
      right = mid
    else:
      left = mid + 1

  return left


def can_partition(nums, k, target):
  partitions = 0
  current_sum = 0

  for num in nums:
    current_sum += num
    if current_sum > target:
      partitions += 1
      current_sum = num

  partitions += 1  # Count the last partition

  return partitions <= k


# Example usage:
N = [5, 1, 2, 7, 3, 4]
k = 3
print(split_array(N, k))  # Output: 8
