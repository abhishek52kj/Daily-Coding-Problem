def run_length_encode(s):
  if not s:
    return ""

  encoded = ""
  count = 1
  for i in range(1, len(s)):
    if s[i] == s[i - 1]:
      count += 1
    else:
      encoded += str(count) + s[i - 1]
      count = 1

  encoded += str(count) + s[-1]
  return encoded


def run_length_decode(encoded):
  decoded = ""
  i = 0
  while i < len(encoded):
    count = int(encoded[i])
    char = encoded[i + 1]
    decoded += char * count
    i += 2

  return decoded


# Example
original_string = "AAAABBBCCDAA"
encoded_string = run_length_encode(original_string)
decoded_string = run_length_decode(encoded_string)

print("Original string:", original_string)
print("Encoded string:", encoded_string)
print("Decoded string:", decoded_string)
