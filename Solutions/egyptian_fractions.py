def egyptian_fraction(numerator, denominator):
  fractions = []
  while numerator != 0:
    # Find the ceiling of the division
    div = -(-denominator // numerator)
    fractions.append(div)
    numerator = numerator * div - denominator
    denominator = denominator * div
  return fractions


# Example usage
numerator = 4
denominator = 13
result = egyptian_fraction(numerator, denominator)
print(f"Egyptian Fraction representation of {numerator}/{denominator}:",
      result)
