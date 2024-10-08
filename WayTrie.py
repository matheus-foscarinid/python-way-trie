# Grupo 3
# Nomes: Matheus Foscarini Dias, Enzo Boadas e Mirágini Victória Silveira Malgarizi

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

  def count_keys_with_prefix(self, prefix: str):
    count = 0

    def count_keys_with_prefix(current: Node):
      nonlocal count
      if current is None:
        return
      if current.value is not None:
        count += 1
      for i in range(WayTrie.R):
        count_keys_with_prefix(current.next[i])

    node: Node = self._search(self._root, prefix, 0)
    count_keys_with_prefix(node)
    return count

  def longest_key_of(self, query: str):
    def longest_key_of(current: Node, query: str, index: int, length: int) -> int:
      # if there is no node, return the current length
      if current is None:
        return length

      # if the current node has a value, update the length
      if current.value is not None:
          length = index

      # if we reached the end of the query, return the length
      if index == len(query):
        return length

      # just continue the search ;)
      character_code: int = ord(query[index])
      next_node = current.next[character_code]
      return longest_key_of(next_node, query, index + 1, length)

    max_length = longest_key_of(self._root, query, 0, 0)
    
    # we return the substring of the query with the max_length
    return query[:max_length] if max_length > 0 else None

  def keys_by_pattern(self, pattern: str) -> List[str]:
    def keys_by_pattern(current: Node, prefix: str, index: int, pattern: str, results: List[str]) -> None:
      # if there is no node, just finish the search
      if current is None:
        return
        
      # if we reached the end of the pattern, we need to check if the current node has a value
      if index == len(pattern):
        # if it has a value, we append the prefix to the results :D
        if current.value is not None:
          results.append(prefix)
        # and then we finish the search
        return

      char = pattern[index]
      # if using "." we need to iterate over all the possible characters in the trie
      if char == '.':
        for i in range(WayTrie.R):
          if current.next[i] is not None:
            curr_word = prefix + chr(i)
            keys_by_pattern(current.next[i], curr_word, index + 1, pattern, results)
      # if it is a normal character, we just need to go to the next node
      else:
        c = ord(char)
        if current.next[c] is not None:
          curr_word = prefix + char
          keys_by_pattern(current.next[c], curr_word, index + 1, pattern, results)

    results: List[str] = []
    keys_by_pattern(self._root, "", 0, pattern, results)

    return results if results else None
