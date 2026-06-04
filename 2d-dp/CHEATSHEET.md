# 2-D Dynamic Programming Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

A 2-D DP table stores solutions for pairs of positions, capacities, or interval endpoints. Transitions refer to already computed neighboring or smaller interval states.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| m by n table | O(mn) |
| Interval DP | O(n^3) common |
| Two-string DP | O(mn) |
| Compressed row | Same time, lower space |

## Space Table

| Case | Complexity |
|---|---:|
| Full table | O(mn) |
| Two rows | O(n) |
| Interval table | O(n^2) |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Grid DP | Use for unique paths, minimum path sum, and obstacle grids. |
| Two String DP | Use for LCS, edit distance, interleaving, and distinct subsequences. |
| Knapsack Table | Use when item choices interact with a numeric limit. |
| Interval DP | Use for burst balloons, matrix-chain style costs, and palindrome intervals. |
| Path Counting With Obstacles | Use for grids with barriers or forbidden transitions. |
| State Compression | Use for grid and string DP after full table is understood. |
| Game DP | Use for take-from-ends games and optimal play. |

## Recognition Hints

Look for two strings, grid paths, edit distance, subsequences, palindromes, matrix costs, intervals, or choices involving two moving indices.

## Pattern Choice Checklist

- Grid DP usually reads from top and left, or from all valid directions.
- Two-string DP compares prefixes ending at i and j.
- Knapsack table separates item choice from capacity.
- Interval DP fills by increasing interval length.

## Interview Calibration

- Say the brute force baseline and the exact wasted work.
- State the invariant before code, not after the solution works.
- Dry run empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites before submitting.

## Templates

### Grid DP

```text
for r in range(rows):
    for c in range(cols):
        dp[r][c] = combine(dp[r-1][c], dp[r][c-1])
```

### Two String DP

```text
for i in range(1, m + 1):
    for j in range(1, n + 1):
        compare text1[i-1], text2[j-1]
```

### Knapsack Table

```text
dp[i][cap] = dp[i-1][cap]
if cap >= weight: dp[i][cap] = best(dp[i][cap], dp[i-1][cap-weight])
```

### Interval DP

```text
for length in range(1, n + 1):
    for left in range(n - length + 1):
        right = left + length - 1
        try split points
```

## Common Traps

- Leaving base row or column undefined.
- Overwriting a row before it is no longer needed.
- Using substring DP when subsequence DP is required.
- Filling interval DP in the wrong length order.

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
