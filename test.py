from WayTrie import WayTrie

if __name__ == '__main__':
  trie = WayTrie()
  
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

  print('testing count_keys_with_prefix')
  print('a: ', trie.count_keys_with_prefix('a'))
  print('ab:', trie.count_keys_with_prefix('ab'))
  print('c:', trie.count_keys_with_prefix('c'))
  print('ca:', trie.count_keys_with_prefix('ca'))
  print('te:', trie.count_keys_with_prefix('te'))

  print('')
  print('testing longest_key_of')
  print('abril: ', trie.longest_key_of('abril'))
  print('casa: ', trie.longest_key_of('casa'))
  print('sapo: ', trie.longest_key_of('sapo'))
  print('abrilhantado: ', trie.longest_key_of('abrilhantado'))
  print('casamento: ', trie.longest_key_of('casamento'))
  print('sapataria: ', trie.longest_key_of('sapataria'))
  print('canil: ', trie.longest_key_of('canil'))

  print('')
  print('testing keys_by_pattern')
  pattern_trie = WayTrie()
  pattern_trie.insert('pata', 'paw')
  pattern_trie.insert('pato', 'duck')
  pattern_trie.insert('pote', 'jar')
  pattern_trie.insert('pate', 'pate')

  print('p.t. :', pattern_trie.keys_by_pattern('p.t.'))
  print('pat. :', pattern_trie.keys_by_pattern('pat.'))
  print('.... :', pattern_trie.keys_by_pattern('....'))
  print('...  :', pattern_trie.keys_by_pattern('...'))

