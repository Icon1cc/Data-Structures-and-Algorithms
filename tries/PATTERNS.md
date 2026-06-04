# Tries Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern: Prefix Insert And Search

### Beginner Intuition

Follow or create one edge per character and mark complete words.

### When To Use It

Use for dictionary insert, search, and startsWith.

### When Not To Use It

Do not build a trie for one-off exact membership checks.

### Recognition Signals

- prefix
- starts with
- dictionary

### Example Problems

- Implement Trie
- Replace Words

### Common Mistakes

- Forgetting the terminal marker.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
node = root
for ch in word:
    node = node.children.setdefault(ch, TrieNode())
node.is_word = True
```

### Complexity Notes

O(L) per word, O(total characters) space.

### Interview Explanation

The path represents the prefix and the terminal marker represents a full word.

## Pattern: Wildcard Trie DFS

### Beginner Intuition

Branch only when the query has a wildcard.

### When To Use It

Use for dot or unknown-character dictionary queries.

### When Not To Use It

Do not branch for normal characters.

### Recognition Signals

- wildcard
- dot
- branch
- dictionary

### Example Problems

- Design Add and Search Words Data Structure

### Common Mistakes

- Returning true for a prefix that is not terminal.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
def search(node, i):
    if i == len(word): return node.is_word
    if word[i] == '.': try all children
    else: follow one child
```

### Complexity Notes

O(branches explored), worst case exponential in wildcards.

### Interview Explanation

Trie pruning keeps ordinary characters cheap and wildcards explicit.

## Pattern: Board Search Trie Pruning

### Beginner Intuition

Use trie prefixes to stop DFS paths that cannot form any word.

### When To Use It

Use for word search with many target words.

### When Not To Use It

Do not restart a full word search for every word when the board is shared.

### Recognition Signals

- board
- many words
- prefix pruning

### Example Problems

- Word Search II

### Common Mistakes

- Not marking board cells visited during the current path.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
dfs(cell, trie_node):
    if char not in trie_node.children: return
    mark cell
    explore neighbors
    unmark cell
```

### Complexity Notes

Often far faster than words * board DFS; worst case still exponential.

### Interview Explanation

The trie answers whether the current path can still lead to a word.

## Pattern: Autocomplete Suggestions

### Beginner Intuition

Find a prefix node, then collect or maintain best suggestions below it.

### When To Use It

Use for search suggestions and top-k prefix queries.

### When Not To Use It

Do not DFS entire subtrees repeatedly if top results can be stored per node.

### Recognition Signals

- autocomplete
- suggestions
- prefix top k

### Example Problems

- Search Suggestions System

### Common Mistakes

- Returning unsorted suggestions when lexicographic order is required.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
node = follow(prefix)
collect up to k words below node in sorted order
```

### Complexity Notes

O(prefix length + output traversal), with optional stored top-k per node.

### Interview Explanation

I separate finding the prefix from ranking suggestions.

## Pattern: Bit Trie

### Beginner Intuition

Store binary bits from high to low to maximize or query XOR greedily.

### When To Use It

Use for maximum XOR and constrained XOR queries.

### When Not To Use It

Do not use a character trie for numeric bit choices.

### Recognition Signals

- xor
- bits
- maximum
- high bit

### Example Problems

- Maximum XOR of Two Numbers in an Array
- Maximum XOR With an Element From Array

### Common Mistakes

- Processing bits from low to high, which loses greedy significance.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
for bit from high to low:
    preferred = 1 - current_bit
    take preferred child if it exists
```

### Complexity Notes

O(n * word_bits) time and space.

### Interview Explanation

High bits dominate XOR value, so each greedy branch is locally safe.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
