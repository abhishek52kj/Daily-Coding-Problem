def rabin_karp(text, pattern):
  if len(pattern) == 0:
    return 0
  if len(pattern) > len(text):
    return False

  prime = 101
  base = 256

  pattern_hash = 0
  text_hash = 0
  for i in range(len(pattern)):
    pattern_hash = (pattern_hash * base + ord(pattern[i])) % prime
    text_hash = (text_hash * base + ord(text[i])) % prime

  base_power = 1
  for i in range(len(pattern) - 1):
    base_power = (base_power * base) % prime

  for i in range(len(text) - len(pattern) + 1):
    if pattern_hash == text_hash:
      match = True
      for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
          match = False
          break
      if match:
        return i

    if i < len(text) - len(pattern):
      text_hash = (base * (text_hash - ord(text[i]) * base_power) +
                   ord(text[i + len(pattern)])) % prime
      if text_hash < 0:
        text_hash += prime

  return False


# Example usage:
text = "ABABCABABCDABCABC"
pattern = "ABC"
print(rabin_karp(text, pattern))  # Output: 2
