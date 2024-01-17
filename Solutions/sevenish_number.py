def find_sevenish_number(n):
  result = 0
  power_of_seven = 1
  powers_of_seven = [1]

  while n > 0:
    if n & 1:
      result += powers_of_seven[-1]

    power_of_seven *= 7
    powers_of_seven.append(power_of_seven)
    n >>= 1

  return result


n = 5
sevenish_number = find_sevenish_number(n)
print(f"The {n}th sevenish number is: {sevenish_number}")
