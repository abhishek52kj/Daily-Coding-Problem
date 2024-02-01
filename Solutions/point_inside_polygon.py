def point_inside_polygon(polygon, p):
  n = len(polygon)
  p_x, p_y = p
  inside = False

  for i in range(n):
    x1, y1 = polygon[i]
    x2, y2 = polygon[(i + 1) % n]

    # Check if the point is on the edge
    if (p_x == x1 and p_y == y1) or (p_x == x2 and p_y == y2):
      return False

    # Check if the point is above, below, or on the edge
    if (y1 < p_y <= y2
        or y2 < p_y <= y1) and p_x < (x2 - x1) * (p_y - y1) / (y2 - y1) + x1:
      inside = not inside

  return inside


# Example usage:
polygon = [(4, 2), (6, 4), (4, 4), (2, 4)]
point = (5, 3)
print(point_inside_polygon(polygon, point))  # Output: False
