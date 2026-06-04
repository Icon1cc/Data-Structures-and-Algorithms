# Backtracking Patterns

This file is the main pattern-recognition reference for backtracking. Each pattern explains why it works, when it fits, when to avoid it, and how to start coding it.

## Pattern: Subsets

### Intuition

For each element, branch into include and exclude choices.

### When To Use It

Use for power sets and all subset generation.

### When Not To Use It

Do not use when order matters and permutations are required.

### Recognition Signals

- subsets
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Subsets
- Combination Sum

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
def backtrack(i):
    if i == n: record path
    choose nums[i]; backtrack(i+1); undo
    backtrack(i+1)
```

## Pattern: Combinations

### Intuition

Choose elements in increasing index order to avoid duplicate orderings.

### When To Use It

Use for choose-k and target-sum combinations.

### When Not To Use It

Do not restart from zero after each choice unless reuse is allowed.

### Recognition Signals

- combinations
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Combination Sum
- Sudoku Solver

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for j in range(start, n):
    path.append(nums[j])
    backtrack(j + 1)
    path.pop()
```

## Pattern: Permutations

### Intuition

At each position, try every unused element.

### When To Use It

Use when arrangements with different orders are distinct.

### When Not To Use It

Do not use for combination problems where order should not matter.

### Recognition Signals

- permutations
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Sudoku Solver
- Subsets

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for i in range(n):
    if used[i]: continue
    used[i] = True
    backtrack()
    used[i] = False
```

## Pattern: Constraint Search

### Intuition

Carry constraint sets so invalid partial assignments are rejected immediately.

### When To Use It

Use for sudoku, n-queens, matchsticks, and equal partitioning.

### When Not To Use It

Do not recompute all constraints from scratch if incremental sets are simple.

### Recognition Signals

- constraint search
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Subsets
- Combination Sum

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
if candidate is valid:
    place candidate and mark constraints
    backtrack()
    undo
```

## Pattern: Board DFS

### Intuition

Move through neighboring cells while marking the current cell visited.

### When To Use It

Use for word search, grid paths, and board coverage.

### When Not To Use It

Do not allow revisits unless the prompt explicitly permits them.

### Recognition Signals

- board dfs
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Combination Sum
- Sudoku Solver

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
mark cell
for neighbor in directions: dfs(neighbor)
unmark cell
```

## Pattern: Partitioning

### Intuition

Choose a valid prefix, recurse on the suffix, and record complete decompositions.

### When To Use It

Use for palindrome cuts, IP addresses, and string splitting.

### When Not To Use It

Do not accept a piece without checking length and validity constraints.

### Recognition Signals

- partitioning
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Sudoku Solver
- Subsets

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for end in range(start + 1, n + 1):
    piece = s[start:end]
    if valid(piece): choose and recurse
```
---

## Navigation

[Previous](../backtracking/CHEATSHEET.md) | [Home](../README.md) | [Next](../backtracking/easy.md)
