def max_sum_non_adjacent(nums):
  prev_max = 0
  curr_max = 0

  for num in nums:
    temp = curr_max
    curr_max = max(prev_max + num, curr_max)
    prev_max = temp
    print(prev_max, curr_max)

  return curr_max


if __name__ == "__main__":
  nums = [5, 1, 1, 1, 5]
  print(max_sum_non_adjacent(nums))