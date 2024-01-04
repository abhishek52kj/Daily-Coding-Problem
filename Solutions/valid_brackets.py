def is_balanced(s):
  stack = []
  mapping = {')': '(', '}': '{', ']': '['}

  for char in s:
      if char in mapping.values():
          stack.append(char)
      elif char in mapping.keys():
          if not stack or stack.pop() != mapping[char]:
              return False
      else:
          return False

  return not stack

# Test cases
string1 = "([])[]({})"
string2 = "([)]"
string3 = "((()"

print(is_balanced(string1))  # Output: True
print(is_balanced(string2))  # Output: False
print(is_balanced(string3))  # Output: False
