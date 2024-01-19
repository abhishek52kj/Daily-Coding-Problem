from collections import deque


def letter_combinations(digits, mapping):
  if not digits:
    return []

  result = []
  queue = deque([""])

  while queue:
    current_combination = queue.popleft()
    if len(current_combination) == len(digits):
      result.append(current_combination)
      continue
    current_digit = digits[len(current_combination)]
    for letter in mapping[current_digit]:
      queue.append(current_combination + letter)

  return result


# Example usage:
digit_mapping = {
  "2": ["a", "b", "c"],
  "3": ["d", "e", "f"],
  "4": ["g", "h", "i"],
  "5": ["j", "k", "l"],
  "6": ["m", "n", "o"],
  "7": ["p", "q", "r", "s"],
  "8": ["t", "u", "v"],
  "9": ["w", "x", "y", "z"],
}

input_digits = "3"
result = letter_combinations(input_digits, digit_mapping)
print(result)
