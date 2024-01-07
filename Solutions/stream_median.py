import heapq


class RunningMedian:

  def __init__(self):
    self.min_heap = []  # Heap for the larger half of the numbers
    self.max_heap = []  # Heap for the smaller half of the numbers

  def add_number(self, num):
    # Ensure max_heap has smaller numbers
    if not self.max_heap or num <= -self.max_heap[0]:
      heapq.heappush(self.max_heap, -num)
    else:
      heapq.heappush(self.min_heap, num)

    # Balance the heaps
    if len(self.max_heap) > len(self.min_heap) + 1:
      heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
    elif len(self.min_heap) > len(self.max_heap):
      heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

  def get_median(self):
    if len(self.max_heap) == len(self.min_heap):
      return (-self.max_heap[0] + self.min_heap[0]) / 2
    else:
      return -self.max_heap[0]


# Example usage
sequence = [2, 1, 5, 7, 2, 0, 5]
running_median_calculator = RunningMedian()

for num in sequence:
  running_median_calculator.add_number(num)
  print(running_median_calculator.get_median())
