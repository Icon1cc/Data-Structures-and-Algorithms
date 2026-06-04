# Tries Patterns

This file is the main pattern-recognition reference for tries. Each pattern explains why it works, when it fits, when to avoid it, and how to start coding it.

## Pattern: Prefix Tree

### Intuition

Share common prefixes so word and prefix queries walk one character at a time.

### When To Use It

Use for dictionaries, prefix search, replace words, and suggestions.

### When Not To Use It

Do not build a trie for one exact lookup when a set is simpler.

### Recognition Signals

- prefix tree
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Implement Trie Prefix Tree
- Word Search II

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
node = root
for ch in word:
    node = node.children.setdefault(ch, TrieNode())
node.is_word = True
```

## Pattern: Wildcard Trie DFS

### Intuition

Branch through children only where the pattern contains a wildcard.

### When To Use It

Use for dot wildcard searches and pattern dictionaries.

### When Not To Use It

Do not expand all paths when the fixed prefix already fails.

### Recognition Signals

- wildcard trie dfs
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Word Search II
- Maximum XOR of Two Numbers in an Array

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
def search(node, i):
    if pattern[i] == wildcard: try each child
    else: follow exact child
```

## Pattern: Autocomplete Suggestions

### Intuition

Walk to the prefix node, then collect a bounded number of ordered completions.

### When To Use It

Use for search suggestions and top prefix matches.

### When Not To Use It

Do not collect an entire subtree if only a small number of suggestions is needed.

### Recognition Signals

- autocomplete suggestions
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Maximum XOR of Two Numbers in an Array
- Implement Trie Prefix Tree

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
node = walk(prefix)
dfs children in sorted order until k results
```

## Pattern: Word Search Trie Pruning

### Intuition

Combine grid DFS with trie prefixes so impossible word paths stop early.

### When To Use It

Use when many words are searched on the same board.

### When Not To Use It

Do not run full board DFS for every word if a trie can share prefixes.

### Recognition Signals

- word search trie pruning
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Implement Trie Prefix Tree
- Word Search II

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
dfs(r, c, node):
    if board[r][c] not in node.children: return
    mark visited and continue
```

## Pattern: Bitwise Trie

### Intuition

Store numbers by bits and greedily follow opposite bits to maximize XOR.

### When To Use It

Use for maximum XOR and constrained XOR queries.

### When Not To Use It

Do not forget fixed bit width and query constraints.

### Recognition Signals

- bitwise trie
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Word Search II
- Maximum XOR of Two Numbers in an Array

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for bit in reversed(range(max_bit)):
    preferred = 1 - current_bit
    take preferred child if present
```

## Pattern: Compressed Trie Awareness

### Intuition

Compress chains of single-child nodes to reduce memory in large static prefix structures.

### When To Use It

Use as a concept for suffix trees, radix trees, and memory-heavy dictionaries.

### When Not To Use It

Do not implement compression during interviews unless the prompt requires it.

### Recognition Signals

- compressed trie awareness
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Maximum XOR of Two Numbers in an Array
- Implement Trie Prefix Tree

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
store edge labels as strings instead of one character per edge
```
---

## Navigation

[Previous](../tries/CHEATSHEET.md) | [Home](../README.md) | [Next](../tries/easy.md)
