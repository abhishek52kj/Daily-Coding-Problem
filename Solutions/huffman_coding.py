import heapq
from collections import defaultdict


class Node:

  def __init__(self, char, freq):
    self.char = char
    self.freq = freq
    self.left = None
    self.right = None

  def __lt__(self, other):
    return self.freq < other.freq


def build_huffman_tree(freq):
  heap = [Node(char, freq) for char, freq in freq.items()]
  heapq.heapify(heap)
  while len(heap) > 1:
    lo = heapq.heappop(heap)
    hi = heapq.heappop(heap)
    merged = Node(None, lo.freq + hi.freq)
    merged.left = lo
    merged.right = hi
    heapq.heappush(heap, merged)
  return heap[0]


def print_huffman_tree(node, prefix=""):
  if node is None:
    return
  if node.char is not None:
    print(f"Character: {node.char}, Frequency: {node.freq}, Code: {prefix}")
  print_huffman_tree(node.left, prefix + "0")
  print_huffman_tree(node.right, prefix + "1")


def huffman_encoding(data):
  freq = defaultdict(int)
  for char in data:
    freq[char] += 1
  if len(freq) == 1:
    encoded_data = "0" * len(data)
    return encoded_data, None
  root = build_huffman_tree(freq)
  encoding_table = {}
  generate_encoding_table(root, encoding_table)
  encoded_data = ''.join(encoding_table[char] for char in data)
  return encoded_data, root


def generate_encoding_table(node, encoding_table, current_code=""):
  if node is None:
    return
  if node.char is not None:
    encoding_table[node.char] = current_code
    return
  generate_encoding_table(node.left, encoding_table, current_code + "0")
  generate_encoding_table(node.right, encoding_table, current_code + "1")


def huffman_decoding(encoded_data, root):
  if root is None:
    return ""
  if not encoded_data:
    return ""
  decoded_data = ""
  current_node = root
  for bit in encoded_data:
    if bit == "0":
      current_node = current_node.left
    else:
      current_node = current_node.right
    if current_node.char is not None:
      decoded_data += current_node.char
      current_node = root
  return decoded_data


# Example usage:
if __name__ == "__main__":
  data = "welcome to the future"
  encoded_data, root = huffman_encoding(data)
  print("Encoded data:", encoded_data)
  print("Huffman Tree:")
  print_huffman_tree(root)
  print("Decoded data:", huffman_decoding(encoded_data, root))
