def merge_intervals(intervals):
  if not intervals:
    return []

  # Sort intervals based on the start values
  intervals.sort(key=lambda x: x[0])

  merged = [intervals[0]]

  for interval in intervals[1:]:
    # Check for overlap and merge if necessary
    if interval[0] <= merged[-1][1]:
      merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
    else:
      merged.append(interval)

  return merged


# Example usage
input_intervals = [(1, 3), (5, 11), (4, 10), (3, 25)]
result = merge_intervals(input_intervals)
print(result)
