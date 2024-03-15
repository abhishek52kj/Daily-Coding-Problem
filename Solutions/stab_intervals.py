def smallest_stabbing_points(intervals):
  intervals.sort(key=lambda x: x[1])  # Sort intervals by their end points
  points = []
  last_point = float('-inf')

  for interval in intervals:
    if interval[0] > last_point:
      points.append(interval[1])
      last_point = interval[1]

  return points


# Example usage:
intervals = [(1, 4), (4, 5), (7, 9), (9, 12)]
stabbing_points = smallest_stabbing_points(intervals)
print("Smallest set of stabbing points:", stabbing_points)
