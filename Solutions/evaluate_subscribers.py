class SegmentTree:

  def __init__(self, arr):
    self.arr = arr
    self.tree = [0] * (4 * len(arr))
    self.build_tree(0, 0, len(arr) - 1)

  def build_tree(self, node, start, end):
    if start == end:
      self.tree[node] = self.arr[start]
    else:
      mid = (start + end) // 2
      left_child = 2 * node + 1
      right_child = 2 * node + 2
      self.build_tree(left_child, start, mid)
      self.build_tree(right_child, mid + 1, end)
      self.tree[node] = self.tree[left_child] + self.tree[right_child]

  def update(self, node, start, end, idx, val):
    if start == end:
      self.arr[idx] += val
      self.tree[node] += val
    else:
      mid = (start + end) // 2
      left_child = 2 * node + 1
      right_child = 2 * node + 2
      if start <= idx <= mid:
        self.update(left_child, start, mid, idx, val)
      else:
        self.update(right_child, mid + 1, end, idx, val)
      self.tree[node] = self.tree[left_child] + self.tree[right_child]

  def query(self, node, start, end, left, right):
    if start > right or end < left:
      return 0
    if left <= start and end <= right:
      return self.tree[node]
    mid = (start + end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2
    return self.query(left_child, start, mid, left, right) + \
           self.query(right_child, mid + 1, end, left, right)


class Subscribers:

  def __init__(self, hours):
    self.segment_tree = SegmentTree([0] * 24)

  def update(self, hour, value):
    self.segment_tree.update(0, 0, 23, hour, value)

  def query(self, start, end):
    return self.segment_tree.query(0, 0, 23, start, end)


# Example usage:
subscribers = Subscribers(24)
subscribers.update(2, 5)
subscribers.update(5, 7)
print(subscribers.query(2, 5))  # Output should be 12 (5 + 7)
