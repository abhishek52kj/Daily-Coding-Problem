def spiral_order(matrix):
  result = []
  while matrix:
    result += matrix.pop(0)
    if matrix and matrix[0]:
      for row in matrix:
        result.append(row.pop())
    if matrix:
      result += matrix.pop()[::-1]
    if matrix and matrix[0]:
      for row in matrix[::-1]:
        result.append(row.pop(0))
  return result


def print_spiral(matrix):
  spiral_result = spiral_order(matrix)
  for num in spiral_result:
    print(num)


# Example usage:
matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]

print_spiral(matrix)
