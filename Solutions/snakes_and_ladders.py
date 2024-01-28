from heapq import heappop, heappush


def min_turns_snakes_and_ladders(snakes, ladders):
  board_size = 100
  min_turns = [float('inf')] * (board_size + 1)
  min_turns[1] = 0

  pq = [(0, 1)]

  while pq:
    turns, square = heappop(pq)
    if square == board_size:
      return turns
    for dice_roll in range(1, 7):
      next_square = square + dice_roll
      next_turns = turns + 1
      if next_square in snakes:
        next_square = snakes[next_square]
      elif next_square in ladders:
        next_square = ladders[next_square]
      if next_square <= board_size:
        if next_turns < min_turns[next_square]:
          min_turns[next_square] = next_turns
          heappush(pq, (next_turns, next_square))

  return -1


snakes = {
  16: 6,
  48: 26,
  49: 11,
  56: 53,
  62: 19,
  64: 60,
  87: 24,
  93: 73,
  95: 75,
  98: 78
}
ladders = {
  1: 38,
  4: 14,
  9: 31,
  21: 42,
  28: 84,
  36: 44,
  51: 67,
  71: 91,
  80: 100
}

min_turns = min_turns_snakes_and_ladders(snakes, ladders)
print("Smallest number of turns:", min_turns)
