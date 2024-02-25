def list_order(L):
  K = [0]
  max_last = 0  # Keeps track of the biggest number we have seen
  min_last = 0  # Keeps track of the smallest number we have seen

  for i in range(1, len(L)):
    if L[i] == '+':
      K.append(max_last + 1)
      max_last += 1
    elif L[i] == '-':
      K.append(min_last - 1)
      min_last -= 1
  return [k - min_last for k in K]


# Example usage:
hints = [None, "+", "+", "-", "+"]
result = list_order(hints)
print(result)  # Output: [1, 2, 3, 0, 4]
