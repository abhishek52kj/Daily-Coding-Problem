def next_sparse_number(n):
  while True:
    bin_n = bin(n)[2:]  # Get the binary representation of n
    if '11' not in bin_n:  # Check if there are no adjacent ones
      return n
    # Find the position of the first pair of adjacent ones
    index = bin_n.find('11')
    # Set all bits after the first pair of adjacent ones to zero
    n += 2**(len(bin_n) - index - 1)


# Test the function
N = int(input("Enter a number N: "))
result = next_sparse_number(N)
print("The smallest sparse number greater than or equal to", N, "is:", result)
