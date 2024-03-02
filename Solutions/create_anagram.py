import string


def step_words(words, input_word):
  valid = []
  for word in words:
    if len(input_word) - len(word) != 1:
      continue
    freq_input = letter_frequency(input_word)
    freq_cur = letter_frequency(word)
    diff = 0
    for c in freq_input.keys():
      diff += abs(freq_input[c] - freq_cur[c])
    if diff == 1:
      valid.append(word)
  print(valid)


def letter_frequency(word):
  freq_letter = {c: 0 for c in string.ascii_lowercase}
  for c in word:
    if c not in freq_letter.keys():
      freq_letter[c] = 1
    else:
      freq_letter[c] += 1
  return freq_letter


# Example usage:
if __name__ == "__main__":
  words = ['apple', 'pear', 'lemon', 'paple']
  input_word = 'appeal'
  step_words(words, input_word)

  words = ['a', 'ab', 'abc', 'abcd', 'abcde']
  input_word = 'abcd'
  step_words(words, input_word)
