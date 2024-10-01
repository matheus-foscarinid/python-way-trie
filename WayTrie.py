from TrieADT import TrieADT
from typing import List

class Node:
  def __init__(self) -> None:
    self.value = None
    self.next = [None] * WayTrie.R

class WayTrie(TrieADT):
  R: int = 256
  def __init__(self) -> None:
    self._root = None

  def clear(self) -> None:
    self._root = None

  def is_empty(self) -> bool:
    return self._root is None

  def search(self, key: object) -> object:
    node: Node = self._search(self._root, key, 0)
    return node.value if node is not None else None

  def _search(self, current: Node, key: object, index: int) -> Node:
    if current is None:
      return None
    elif index == len(key):
      return current
    return self._search(current.next[ord(key[index])], key, index + 1)

  def insert(self, key: object, value: object) -> None:
    def insert(current: Node, key: object, value: object, index: int) -> None:
      if current is None:
        current = Node()
      if index == len(key):
        current.value = value
        return current
      c: int = ord(key[index])
      current.next[c] = insert(current.next[c], key, value, index + 1)
      return current

    self._root = insert(self._root, key, value, 0)

  def delete(self, key: object) -> None:
    def delete(current: Node, key: object, index: int) -> Node:
      if current is None:
        return None
      if index == len(key):
        current.value = None
      else:
        c: int = ord(key[index])
        current.next[c] = delete(current.next[c], key, index + 1)
      if current.value is not None:
        return current
      for i in range(WayTrie.R):
        if current.next[i] is not None:
          return current
      return None

    self._root = delete(self._root, key, 0)

  def keys_with_prefix(self, prefix: str) -> List[str]:
    def keys_with_prefix(current: Node, prefix: str, results: List[str]) -> None:
      if current is None:
        return
      if current.value is not None:
        results.append(prefix)
      for i in range(WayTrie.R):
        prefix += chr(i)
        keys_with_prefix(current.next[i], prefix, results)
        prefix = prefix[:-1]

    results: List[str] = []
    node: Node = self._search(self._root, prefix, 0)
    keys_with_prefix(node, prefix, results)
    return results

  def count_keys_with_prefix(self):
    # TODO
    pass

  def longest_key_of(self):
    # TODO
    pass

  def keys_by_pattern(self):
    # TODO
    pass

if __name__ == '__main__':
  trie = WayTrie()
  
  # inserting some words based on slides from WayTrie class
  trie.insert('abelha', 'bee')
  trie.insert('abril', 'april')
  trie.insert('acre', 'acre')
  trie.insert('aluno', 'student')

  trie.insert('cabo', 'cable')
  trie.insert('capa', 'cover')
  trie.insert('capeta', 'devil')
  trie.insert('casa', 'house')

  trie.insert('salario', 'salary')
  trie.insert('sapo', 'frog')

  # searching for some words
  print(trie.search('abril'))
  print(trie.search('aluno'))
  print(trie.search('casa'))
  print(trie.search('foo'))

  # deleting some words
  trie.delete('abril')
  trie.delete('casa')
  print(trie.search('abril'))
  print(trie.search('casa'))

  # getting all keys with prefix 'ca'
  print(trie.keys_with_prefix('ca'))



