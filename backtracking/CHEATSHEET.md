# Backtracking Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

Backtracking is depth-first search over a state space with pruning. Correctness depends on complete candidate generation and precise state restoration.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Subsets | O(2^n) |
| Permutations | O(n!) |
| Combinations | O(C(n, k)) |
| Board search | O(cells * branching^depth) before pruning |

## Space Table

| Case | Complexity |
|---|---:|
| Recursion depth | O(depth) |
| Visited set or board marks | O(depth) or O(cells) |
| Output | Often exponential and counted separately |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Subsets | Use when every element may be taken or skipped. |
| Combinations | Use for choose k, combination sum, and unordered selections. |
| Permutations | Use when order matters. |
| Constraint Grid Search | Use for word search and maze-style constraint traversal. |
| Partition Backtracking | Use for palindrome partitions, IP addresses, and expression generation. |
| Pruned Search | Use for N-Queens, Sudoku, and target sums. |

## Recognition Hints

Look for all possible, generate, combinations, permutations, subsets, valid arrangements, board search, partition, or constraints that require trying choices.

## Pattern Choice Checklist

- Subsets decide include or exclude, or iterate next choices.
- Combinations advance the start index to prevent reuse.
- Permutations track used elements or swap in place.
- Grid search marks visited before recursion and unmarks after.

## Interview Calibration

- Say the brute force baseline and the exact wasted work.
- State the invariant before code, not after the solution works.
- Dry run duplicate choices, missing undo, invalid pruning, and output-size complexity before submitting.

## Templates

### Subsets

```text
def dfs(i):
    if i == n: record(path); return
    dfs(i + 1)
    path.append(nums[i]); dfs(i + 1); path.pop()
```

### Combinations

```text
def dfs(start):
    for i in range(start, n):
        choose nums[i]
        dfs(next_start)
        undo
```

### Permutations

```text
def dfs():
    if len(path) == n: record(path)
    for i in range(n):
        if used[i]: continue
        used[i] = True; path.append(nums[i])
        dfs()
        path.pop(); used[i] = False
```

### Constraint Grid Search

```text
mark cell
for neighbor in neighbors:
    dfs(neighbor)
unmark cell
```

## Common Traps

- Appending the live path instead of a copy.
- Forgetting to undo mutable state.
- Skipping duplicate logic after sorting.
- Pruning a branch that could still become valid.

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
