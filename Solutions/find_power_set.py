def generate_power_set(input_set):

  def backtrack(start, current_set, result):
    result.append(current_set.copy())

    for i in range(start, len(input_set)):
      current_set.append(input_set[i])
      backtrack(i + 1, current_set, result)
      current_set.pop()

  result = []
  backtrack(0, [], result)
  return result


input_set = {1, 2, 3}
power_set = generate_power_set(list(input_set))
print(power_set)
