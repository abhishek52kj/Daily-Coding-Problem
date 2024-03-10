def evaluate_expression(expression: str) -> int:
  result = 0
  add = True
  sub_eval_string = ""
  number_of_parentheses = 0
  for char in expression:
    if number_of_parentheses > 0:
      # inside a set of parentheses
      if char == "(":
        number_of_parentheses += 1
      elif char == ")":
        number_of_parentheses -= 1
      if number_of_parentheses == 0:
        if add:
          result += evaluate_expression(sub_eval_string)
        else:
          result -= evaluate_expression(sub_eval_string)
        sub_eval_string = ""
      else:
        sub_eval_string += char
    else:
      if char == "-":
        add = False
      elif char == "+":
        add = True
      elif char == "(":
        number_of_parentheses = 1
      elif char.isdigit():
        if add:
          result += int(char)
        else:
          result -= int(char)
  return result


if __name__ == "__main__":
  print(evaluate_expression("-1 + (2 + 3)"))
  print(evaluate_expression("-1 + (2 + 3) + (2 - 3)"))
  print(evaluate_expression("-1 + (2 + 3) + ((2 - 3) + 1)"))
