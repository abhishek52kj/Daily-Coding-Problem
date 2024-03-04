def is_power_of_four(n):
  # A number is a power of four if it is greater than 0 and only has one bit set in its binary representation,
  # and this bit appears at an even position (0-based index).
  return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0


# Example usage:
N = 32
print(is_power_of_four(N))  # Output: True
