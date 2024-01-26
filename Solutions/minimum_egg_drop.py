import math


def eggDrop(eggs, floors):
  eggFloor = [[0] * (floors + 1) for _ in range(eggs + 1)]

  for floor in range(1, floors + 1):
    eggFloor[1][floor] = floor

  for egg in range(2, eggs + 1):
    for floor in range(1, floors + 1):
      eggFloor[egg][floor] = float('inf')
      low, high = 1, floor
      while low <= high:
        mid = (low + high) // 2
        res = 1 + max(eggFloor[egg - 1][mid - 1], eggFloor[egg][floor - mid])
        if res < eggFloor[egg][floor]:
          eggFloor[egg][floor] = res
        if eggFloor[egg - 1][mid - 1] < eggFloor[egg][floor - mid]:
          low = mid + 1
        else:
          high = mid - 1

  return eggFloor[eggs][floors]


N = 2
k = 7
print("Minimum number of trials:", eggDrop(N, k))
