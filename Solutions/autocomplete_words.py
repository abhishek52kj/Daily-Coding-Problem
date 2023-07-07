class TrieNode:

  def __init__(self):
    self.children = {}
    self.is_word_end = False


class AutocompleteSystem:

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root
    for char in word:
      if char not in node.children:
        node.children[char] = TrieNode()
      node = node.children[char]
    node.is_word_end = True

  def search(self, query):
    node = self.root
    result = []
    prefix = ""

    for char in query:
      if char not in node.children:
        return result
      node = node.children[char]
      prefix += char

    self._find_words(node, prefix, result)

    return result

  def _find_words(self, node, prefix, result):
    if node.is_word_end:
      result.append(prefix)

    for char, child_node in node.children.items():
      self._find_words(child_node, prefix + char, result)

  # def print_trie(self):
  #   self._print_node(self.root, "")

  # def _print_node(self, node, prefix):
  #   if node.is_word_end:
  #     print(prefix)

  #   for char, child_node in node.children.items():
  #     self._print_node(child_node, prefix + char)


if __name__ == "__main__":

  autocomplete = AutocompleteSystem()

  words = ['dog', 'deer', 'deal']
  for word in words:
    autocomplete.insert(word)

  # autocomplete.print_trie()

  query = 'do'
  autocomplete_result = autocomplete.search(query)
  print(autocomplete_result)
