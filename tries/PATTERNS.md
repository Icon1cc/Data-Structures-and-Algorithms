# Tries Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| Prefix Insert And Search | prefix | Do not build a trie for one-off exact membership checks |
| Wildcard Trie DFS | wildcard | Do not branch for normal characters |
| Board Search Trie Pruning | board | Do not restart a full word search for every word when the board is shared |
| Autocomplete Suggestions | autocomplete | Do not DFS entire subtrees repeatedly if top results can be stored per node |
| Bit Trie | xor | Do not use a character trie for numeric bit choices |

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

- Forgetting `is_word` so `search("app")` returns true even when only "apple" was inserted.
- Confusing `search` with `startsWith`; the former requires `is_word` at the end, the latter does not.
- Building 26-array nodes for sparse alphabets; the memory dwarfs a hash-map child table.

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

- Returning `True` at the end of the query without checking `is_word`; that accepts any prefix as a hit.
- Branching on every character instead of only on `'.'`; the search degenerates to a full-trie DFS.
- Failing to short-circuit; once any branch returns `True`, the recursion can stop exploring siblings.

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

- Failing to mark and unmark board cells during DFS, which causes the same letter to be reused along the path.
- Adding the same word to the result twice; clear `is_word` after the first match or use a set.
- Skipping trie pruning of dead branches; popping leaf nodes whose subtree is exhausted keeps later searches fast.

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

- Re-walking the trie from the root on every keystroke; advance from the previous node instead.
- Building lists in arrival order when the spec wants lexicographic order; insert from a sorted product list to keep order automatically.
- Storing the full word at every node when only the top-3 prefix matches are needed; trim the per-node cache to the answer size.

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

- Inserting bits from least-significant to most-significant; greedy search needs the high bits at the root.
- Forgetting to fall back to the same-bit child when the opposite-bit child does not exist.
- Using a fixed bit width that cannot hold the largest input; size the depth to `ceil(log2(max_value)) + 1`.

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
