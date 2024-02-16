def modified_radix_sort(data):

  def counting_sort_digit(data, exp):  # Helper for each digit position
    # ... (Similar to standard counting sort implementation)
    max_num = max(data)
    exp = 1
    while max_num // exp > 0:
      counting_sort_digit(data, exp)
      exp *= 10
