import re


def is_valid_sentence(sentence):
  # Check if the sentence starts with a capital letter followed by a lowercase letter or a space
  if not sentence or not sentence[0].isupper():
    return False

  # Check for single space between each word
  words = sentence.split()
  if len(words) < 2 or any(word == '' for word in words) or '  ' in sentence:
    return False

  # Check for valid characters
  if not re.match(r'^[A-Z][a-z ,;:.!?‽]+$', sentence):
    return False

  # Check if the sentence ends with a terminal mark immediately following a word
  if len(sentence) > 1:
    second_last_char = sentence[-2]
    last_char = sentence[-1]
    if not second_last_char.isalnum() or last_char not in (".", "?", "!", "‽"):
      return False

  return True


# Example usage:
sentences = [
  "Valid sentence.", "Invalid sentence", " invalid sentence",
  "A valid sentence.", "ANOTHER Valid sentence.", "Another invalid one.", "A",
  "This  sentence has  multiple    spaces  between words.",
  "This sentence has an @invalid character.",
  "This sentence ends with a terminal mark!"
]

for sentence in sentences:
  if is_valid_sentence(sentence):
    print(f"'{sentence}' meets the requirements.")
  else:
    print(f"'{sentence}' does not meet the requirements.")
