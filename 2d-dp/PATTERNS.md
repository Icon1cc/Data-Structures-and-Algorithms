# 2-D Dynamic Programming Patterns

This file is the main pattern-recognition reference for 2-d dynamic programming. Each pattern explains why it works, when it fits, when to avoid it, and how to start coding it.

## Pattern: Grid Paths

### Intuition

Compute each cell from previously reachable neighbor cells.

### When To Use It

Use for unique paths, obstacles, and minimum path sum.

### When Not To Use It

Do not use simple grid DP if moves can create cycles.

### Recognition Signals

- grid paths
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Unique Paths
- Longest Common Subsequence

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
dp[r][c] = combine(dp[r-1][c], dp[r][c-1])
```

## Pattern: Two String DP

### Intuition

Use prefixes of two strings as the two state dimensions.

### When To Use It

Use for LCS, edit distance, interleaving, and distinct subsequences.

### When Not To Use It

Do not use greedy matching when edits or skips interact.

### Recognition Signals

- two string dp
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Longest Common Subsequence
- Edit Distance

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for i in range(n + 1):
    for j in range(m + 1):
        dp[i][j] = transition
```

## Pattern: Knapsack Table

### Intuition

Track item progress and remaining capacity or target.

### When To Use It

Use for subset sum, capacity, target sum, and 0-1 choices.

### When Not To Use It

Do not iterate capacity forward for 0-1 choices unless using a separate row.

### Recognition Signals

- knapsack table
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Edit Distance
- Unique Paths

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for item in items:
    for cap in reversed(range(weight, target + 1)):
        update dp[cap]
```

## Pattern: Interval DP

### Intuition

Solve ranges by splitting each interval into smaller intervals.

### When To Use It

Use for burst balloons, merge stones, and range optimization.

### When Not To Use It

Do not use interval DP when a one-dimensional recurrence captures the same state.

### Recognition Signals

- interval dp
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Unique Paths
- Longest Common Subsequence

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for length in range(1, n + 1):
    for left in range(...):
        right = left + length - 1
        try split points
```

## Pattern: Palindrome DP

### Intuition

Use inner substrings to decide whether larger substrings are palindromes or how costly they are.

### When To Use It

Use for palindrome subsequence, substring, cuts, and insertions.

### When Not To Use It

Do not build a table for a single palindrome check that two pointers can solve.

### Recognition Signals

- palindrome dp
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Longest Common Subsequence
- Edit Distance

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
dp[l][r] = s[l] == s[r] and dp[l+1][r-1]
```

## Pattern: State Compression

### Intuition

Reduce table dimensions when only recent rows, columns, or masks are needed.

### When To Use It

Use after the full recurrence is correct.

### When Not To Use It

Do not overwrite values that future transitions still need.

### Recognition Signals

- state compression
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Edit Distance
- Unique Paths

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
prev = old_row
curr = new_row
keep diagonal value if transition needs it
```
---

## Navigation

[Previous](../2d-dp/CHEATSHEET.md) | [Home](../README.md) | [Next](../2d-dp/easy.md)
