def two_sum(nums, k):

  seen = {}
  for i, num in enumerate(nums):
    if k - num in seen:
      return True
    seen[num] = i
  return False


if __name__ == "__main__":
  nums = [10, 15, 3, 7]
  k = 17
  print(two_sum(nums, k))
