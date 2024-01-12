def nth_perfect_number(n):
  current_number = 19
  count = 0

  while True:
    digit_sum = sum(int(digit) for digit in str(current_number))

    if digit_sum == 10:
      count += 1

    if count == n:
      return current_number

    current_number += 9


print(nth_perfect_number(1))
print(nth_perfect_number(10))
