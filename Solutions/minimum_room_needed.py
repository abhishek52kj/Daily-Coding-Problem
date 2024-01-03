import heapq


def minMeetingRooms(intervals):
  if not intervals:
    return 0

  # Sort the intervals based on the start time
  intervals.sort(key=lambda x: x[0])

  # Use a min-heap to keep track of the end times of ongoing meetings
  end_times = []
  heapq.heappush(end_times, intervals[0][1])

  # Iterate through the remaining intervals
  for i in range(1, len(intervals)):
    # If the current interval's start time is greater than or equal to the earliest end time
    # among ongoing meetings, then allocate the same room by updating the end time
    if intervals[i][0] >= end_times[0]:
      heapq.heappop(end_times)
    heapq.heappush(end_times, intervals[i][1])

  # The size of the min-heap represents the minimum number of rooms required
  return len(end_times)


# Example usage
intervals = [(30, 75), (0, 50), (45, 150)]
result = minMeetingRooms(intervals)
print(result)
