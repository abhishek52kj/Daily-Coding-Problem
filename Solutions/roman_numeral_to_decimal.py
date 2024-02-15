roman_numeral_map = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000,
}


def roman_to_int(roman_numeral):

  total = 0
  prev = 0

  for char in roman_numeral:
    current = roman_numeral_map[char]
    total += current

    if prev < current:
      total -= 2 * prev

    prev = current

  return total


# Example usage
roman_numeral = "MCMXCIV"
decimal_value = roman_to_int(roman_numeral)
print(f"{roman_numeral} in decimal is {decimal_value}")
