# Backtracking Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| Subsets | all subsets | Do not use permutations when order does not matter |
| Combinations | choose k | Do not restart from zero after each choice |
| Permutations | arrangements | Do not sort-and-skip incorrectly when duplicates exist |
| Constraint Grid Search | grid | Do not use a global visited set when paths must be independent |
| Partition Backtracking | partition | Do not copy large substrings unnecessarily if indices are enough |
| Pruned Search | constraints | Do not prune on a condition that future choices could fix |

## Pattern: Subsets

### Beginner Intuition

At each item choose include or exclude, producing every subset once.

### When To Use It

Use when every element may be taken or skipped.

### When Not To Use It

Do not use permutations when order does not matter.

### Recognition Signals

- all subsets
- power set
- include exclude

### Example Problems

- Subsets
- Subsets II

### Common Mistakes

- Appending the live `path` list to the result; subsequent mutations corrupt every saved subset.
- Including the empty subset twice (once at start, once when no items are chosen); record exactly once at each leaf.
- For Subsets II, sorting and then using `if i > start and nums[i] == nums[i - 1]: continue` is the canonical duplicate skip; the `i > start` guard is essential.

### Pseudocode Or Template

```text
def dfs(i):
    if i == n: record(path); return
    dfs(i + 1)
    path.append(nums[i]); dfs(i + 1); path.pop()
```

### Complexity Notes

O(n * 2^n) including output.

### Interview Explanation

The decision tree has two branches per element.

## Pattern: Combinations

### Beginner Intuition

Build choices in increasing index order so order does not create duplicates.

### When To Use It

Use for choose k, combination sum, and unordered selections.

### When Not To Use It

Do not restart from zero after each choice.

### Recognition Signals

- choose k
- combinations
- start index

### Example Problems

- Combination Sum
- Combination Sum II

### Common Mistakes

- Restarting the inner loop from `0` instead of `start`, which produces every order of the same combination.
- For Combination Sum (LC 39), passing `i + 1` instead of `i` for the recurrence; the problem allows reuse, so stay at the same index.
- Pruning by `target < 0` only at the top of the recursion instead of also short-circuiting before recursing on an oversized candidate.

### Pseudocode Or Template

```text
def dfs(start):
    for i in range(start, n):
        choose nums[i]
        dfs(next_start)
        undo
```

### Complexity Notes

Exponential output, often pruned by target.

### Interview Explanation

The start index enforces a canonical order.

## Pattern: Permutations

### Beginner Intuition

Track used elements so each position chooses from remaining values.

### When To Use It

Use when order matters.

### When Not To Use It

Do not sort-and-skip incorrectly when duplicates exist.

### Recognition Signals

- arrangements
- order matters
- used set

### Example Problems

- Permutations
- Next Permutation

### Common Mistakes

- Forgetting `used[i] = False` after recursing; subsequent paths see stale "used" state.
- For Permutations II, skipping equal values without checking that the previous equal sibling is unused; the correct guard is `if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue`.
- Mutating `nums` in place via swap-based permutations and then expecting the original order back; either swap back on undo or use the index-based template.

### Pseudocode Or Template

```text
def dfs():
    if len(path) == n: record(path)
    for i in range(n):
        if used[i]: continue
        used[i] = True; path.append(nums[i])
        dfs()
        path.pop(); used[i] = False
```

### Complexity Notes

O(n * n!) time including output.

### Interview Explanation

Each depth fixes one position in the arrangement.

## Pattern: Constraint Grid Search

### Beginner Intuition

DFS through grid cells while marking visited for the current path.

### When To Use It

Use for word search and maze-style constraint traversal.

### When Not To Use It

Do not use a global visited set when paths must be independent.

### Recognition Signals

- grid
- path
- visited
- neighbors

### Example Problems

- Word Search
- Sudoku Solver

### Common Mistakes

- Using a global `visited` set when paths from different starting cells must explore independently.
- Forgetting to unmark a cell after the DFS subtree returns; later searches treat the cell as permanently used.
- Trying every starting cell even when an early prune (first character mismatch) could skip whole subtrees.

### Pseudocode Or Template

```text
mark cell
for neighbor in neighbors:
    dfs(neighbor)
unmark cell
```

### Complexity Notes

O(cells * branching^depth) before pruning.

### Interview Explanation

Visited means used in this current path, not forever.

## Pattern: Partition Backtracking

### Beginner Intuition

Cut the input into valid pieces and recurse on the suffix.

### When To Use It

Use for palindrome partitions, IP addresses, and expression generation.

### When Not To Use It

Do not copy large substrings unnecessarily if indices are enough.

### Recognition Signals

- partition
- cuts
- valid piece

### Example Problems

- Palindrome Partitioning
- Restore IP Addresses

### Common Mistakes

- Slicing the input string at every recursive call; pass `(start, end)` indices and slice only when recording.
- Recomputing `is_palindrome` per cut without memoization on a 2-D table; precompute for O(1) lookups.
- For Restore IP Addresses, accepting numbers with leading zeros (e.g., `"01"`) which are invalid octets.

### Pseudocode Or Template

```text
for end in valid_ends(start):
    piece = s[start:end]
    if valid(piece): choose and dfs(end)
```

### Complexity Notes

Exponential in number of valid cuts.

### Interview Explanation

Every branch chooses the next valid segment boundary.

## Pattern: Pruned Search

### Beginner Intuition

Use constraints to stop branches before they become complete failures.

### When To Use It

Use for N-Queens, Sudoku, and target sums.

### When Not To Use It

Do not prune on a condition that future choices could fix.

### Recognition Signals

- constraints
- early stop
- board

### Example Problems

- N-Queens
- Expression Add Operators

### Common Mistakes

- Pruning on a state that a future choice could legally repair (e.g., temporary partial sum exceeding target when negative numbers exist later).
- Re-running the full validity check from scratch at each call; maintain incremental state for O(1) updates.
- For N-Queens, encoding diagonals naively as sets of `(r, c)` instead of `r - c` and `r + c`, which costs more memory and lookups.

### Pseudocode Or Template

```text
if violates_constraints(state): return
continue search
```

### Complexity Notes

Same worst case, much better practical runtime.

### Interview Explanation

I state why the pruned branch cannot become valid.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
