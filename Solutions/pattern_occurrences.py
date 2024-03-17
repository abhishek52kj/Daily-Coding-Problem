def compute_lps_array(pattern):
  lps = [0] * len(pattern)
  j = 0
  i = 1
  while i < len(pattern):
    if pattern[i] == pattern[j]:
      j += 1
      lps[i] = j
      i += 1
    else:
      if j != 0:
        j = lps[j - 1]
      else:
        lps[i] = 0
        i += 1
  return lps


def kmp_search(text, pattern):
  occurrences = []
  lps = compute_lps_array(pattern)
  i, j = 0, 0
  while i < len(text):
    if text[i] == pattern[j]:
      i += 1
      j += 1
      if j == len(pattern):
        occurrences.append(i - j)
        j = lps[j - 1]
    else:
      if j != 0:
        j = lps[j - 1]
      else:
        i += 1
  return occurrences


text = "abracadabra"
pattern = "abr"
result = kmp_search(text, pattern)
print("Starting indices of pattern occurrences:", result)
