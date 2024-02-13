def find_maximum(a, b):
  diff = a - b
  # if a > b, sign will be 1, otherwise 0
  sign = (diff >> 31) & 0x1
  # maximum will be a*sign + b*(1-sign)
  max_number = a * (1 - sign) + b * sign
  return max_number


# Test the function
a = 10
b = 20
print("Maximum of", a, "and", b, "is:", find_maximum(a, b))
