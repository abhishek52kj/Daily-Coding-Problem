def valid_utf8(data):
  num_following_bytes = 0

  for byte in data:
    if num_following_bytes == 0:
      if (byte >> 7) == 0b0:
        continue
      elif (byte >> 5) == 0b110:
        num_following_bytes = 1
      elif (byte >> 4) == 0b1110:
        num_following_bytes = 2
      elif (byte >> 3) == 0b11110:
        num_following_bytes = 3
      else:
        return False
    else:
      if (byte >> 6) != 0b10:
        return False
      num_following_bytes -= 1

  return num_following_bytes == 0


# Examples
print(valid_utf8([197, 130, 1]))  # True
print(valid_utf8([235, 140, 4]))  # True
print(valid_utf8([197, 129, 129]))  # False
print(valid_utf8([235, 140]))  # False
