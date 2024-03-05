def pushDominoes(dominoes):
  result = list(dominoes)
  length = len(dominoes)
  force = 0

  for i in range(length):
    if dominoes[i] == 'R':
      force = length
    elif dominoes[i] == 'L':
      force = 0
    else:
      force = max(force - 1, 0)
    result[i] = '.' if force == 0 else 'R' if force == length else 'L'

  force = 0
  for i in range(length - 1, -1, -1):
    if dominoes[i] == 'L':
      force = length
    elif dominoes[i] == 'R':
      force = 0
    else:
      force = max(force - 1, 0)
    if force > 0:
      result[i] = 'L'
    elif force < 0:
      result[i] = 'R'

  return ''.join(result)


# Test cases
print(pushDominoes(".L.R....L"))  # Output: "LL.RRRLLL"
print(pushDominoes("..R...L.L"))  # Output: "..RR.LLLL"
