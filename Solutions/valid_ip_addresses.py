def restore_ip_addresses(s):

  def backtrack(start, parts):
    if len(parts) == 4 and start == len(s):
      result.append(".".join(parts))
      return
    elif len(parts) == 4 or start == len(s):
      return

    for i in range(1, 4):
      if start + i > len(s):
        break

      part = s[start:start + i]
      if (len(part) > 1 and part[0] == '0') or int(part) > 255:
        break

      backtrack(start + i, parts + [part])

  result = []
  backtrack(0, [])
  return result


# Test the function
input_str = "2542540123"
print(restore_ip_addresses(input_str))
