def can_form_circle(words):
  if not words:
    return False

  # Create a dictionary to store first and last characters of each word
  first_char = {}
  last_char = {}

  for word in words:
    first_char[word[0]] = first_char.get(word[0], 0) + 1
    last_char[word[-1]] = last_char.get(word[-1], 0) + 1

  # Check if the number of words starting with a character is equal to the number
  # of words ending with that character, except for one character
  odd_start = odd_end = 0
  for char in first_char:
    if char not in last_char:
      return False
    if first_char[char] != last_char[char]:
      if abs(first_char[char] - last_char[char]) > 1:
        return False
      if first_char[char] > last_char[char]:
        odd_start += 1
      else:
        odd_end += 1

  return odd_start == 1 and odd_end == 1


# Example usage:
words = ['chair', 'height', 'racket', 'touch', 'tunic']
if can_form_circle(words):
  print("The words can form a circle.")
else:
  print("The words cannot form a circle.")
