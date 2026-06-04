# Tries Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

A trie is a rooted tree where each edge represents a character or token and terminal markers indicate complete keys.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Insert word length L | O(L) |
| Search word length L | O(L) |
| Wildcard search | O(branches explored) |
| Board search with trie | O(cells * branching) with pruning |

## Space Table

| Case | Complexity |
|---|---:|
| Trie nodes | O(total characters) |
| DFS stack | O(max word length) |
| Compressed trie | Less space when long single-child paths exist |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Prefix Insert And Search | Use for dictionary insert, search, and startsWith. |
| Wildcard Trie DFS | Use for dot or unknown-character dictionary queries. |
| Board Search Trie Pruning | Use for word search with many target words. |
| Autocomplete Suggestions | Use for search suggestions and top-k prefix queries. |
| Bit Trie | Use for maximum XOR and constrained XOR queries. |

## Recognition Hints

Look for prefix, dictionary, wildcard, autocomplete, word board, starts with, maximum XOR bit trie, or repeated string membership queries.

## Pattern Choice Checklist

- Exact search needs terminal markers.
- Prefix search can return before terminal markers.
- Wildcard search branches only on wildcard positions.
- Bit trie chooses opposite bits for maximum XOR when possible.

## Interview Calibration

- Say the brute force baseline and the exact wasted work.
- State the invariant before code, not after the solution works.
- Dry run empty strings, duplicate words, terminal markers, and large alphabets before submitting.

## Templates

### Prefix Insert And Search

```text
node = root
for ch in word:
    node = node.children.setdefault(ch, TrieNode())
node.is_word = True
```

### Wildcard Trie DFS

```text
def search(node, i):
    if i == len(word): return node.is_word
    if word[i] == '.': try all children
    else: follow one child
```

### Board Search Trie Pruning

```text
dfs(cell, trie_node):
    if char not in trie_node.children: return
    mark cell
    explore neighbors
    unmark cell
```

### Autocomplete Suggestions

```text
node = follow(prefix)
collect up to k words below node in sorted order
```

## Common Traps

- Treating every prefix as a complete word.
- Building a trie when a single hash set lookup is enough.
- Forgetting to prune found words on boards.
- Ignoring memory cost for large alphabets.

## Interview Reminders

- Say the brute force approach first in one or two sentences.
- State the invariant before coding.
- Test one normal case, one smallest case, and one adversarial case.
- Include auxiliary space, not only input and output size.
- Mention when the pattern assumptions would fail.

## Final Checklist

- [ ] I can define the topic in plain language.
- [ ] I can identify at least three recognition signals.
- [ ] I can write the main template from memory.
- [ ] I can explain time and space complexity.
- [ ] I can name two common mistakes and how to avoid them.

---

## Navigation

[Previous](README.md) | [Home](../README.md) | [Next](PATTERNS.md)
