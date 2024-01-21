def last_survivor_general(N, k):
  prisoners = list(range(1, N + 1))
  index = 0

  while len(prisoners) > 1:
    index = (index + k - 1) % len(prisoners)
    prisoners.pop(index)

  return prisoners[0]


def last_survivor_bonus(N):
  if N == 1:
    return 1
  if N % 2 == 0:
    return 2 * last_survivor_bonus(N // 2) - 1
  else:
    return 2 * last_survivor_bonus(N // 2) + 1


N = 5
k = 3
result_general = last_survivor_general(N, k)
print(
  f"For N = {N} and k = {k}, the last survivor is at position: {result_general}"
)

N = 5
result_bonus = last_survivor_bonus(N)
print(
  f"For N = {N} and k = 2, the last survivor is at position: {result_bonus}")
