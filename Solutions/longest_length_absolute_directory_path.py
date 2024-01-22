def lengthLongestPath(input_str):
  lines = input_str.split('\n')
  stack = [(-1, 0)]  # (depth, length)
  max_length = 0

  for line in lines:
    depth = line.count('\t')
    name = line.lstrip('\t')
    while depth <= stack[-1][0]:
      stack.pop()

    if '.' in name:
      max_length = max(max_length, stack[-1][1] + len(name))
    else:
      stack.append((depth, stack[-1][1] + len(name) + 1))

  return max_length


# Example usage:
input_str1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
input_str2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

print(lengthLongestPath(input_str1))  # Output: 20
print(lengthLongestPath(input_str2))  # Output: 32
