# 1-D Dynamic Programming Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

Dynamic programming applies when optimal substructure and overlapping subproblems exist. A 1-D DP state usually depends on earlier indices or capacities.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Linear recurrence | O(n) |
| Capacity DP | O(n * capacity) |
| LIS quadratic | O(n^2) |
| LIS with binary search | O(n log n) |

## Space Table

| Case | Complexity |
|---|---:|
| Full table | O(n) or O(n * capacity) |
| Rolling variables | O(1) |
| Memo recursion | O(states) plus call stack |

## Pattern Summary

| Pattern | Use When |
|---|---|
| State Definition | Use for every DP problem. |
| Memoization | Use when top-down choices are easier to express than fill order. |
| Tabulation | Use when dependency order is clear. |
| Transition Choice | Use for min/max/counting DP. |
| Knapsack | Use for subset sum, partition, and bounded resource selection. |
| Subsequence DP | Use for LIS, word break variants, and sequence scoring. |
| State Compression | Use when dp[i] depends on a fixed small window of earlier states. |
| Kadane | Use for maximum subarray and local extend-or-restart decisions. |

## Recognition Hints

Look for count ways, min cost, max profit, can reach, choose or skip, subsequence, partition, coin change, or repeated recursion over indices.

## Pattern Choice Checklist

- Memoization is easier when recursion expresses choices naturally.
- Tabulation is easier when fill order is obvious.
- Knapsack needs item and capacity or compressed capacity order.
- Kadane keeps best subarray ending here and best overall.

## Interview Calibration

- Say the brute force baseline and the exact wasted work.
- State the invariant before code, not after the solution works.
- Dry run base cases, invalid states, iteration order, and memory compression direction before submitting.

## Templates

### State Definition

```text
dp[i] = answer for the prefix ending at i
# or answer using first i items
```

### Memoization

```text
memo = {}
def solve(i):
    if i in memo: return memo[i]
    memo[i] = combine(next states)
    return memo[i]
```

### Tabulation

```text
dp = [base values]
for i in fill_order:
    dp[i] = transition(previous states)
```

### Transition Choice

```text
dp[i] = best(dp[i - 1], value[i] + dp[i - 2])
```

## Common Traps

- Coding before defining the state.
- Mixing ending-at with up-to-index states.
- Using wrong fill direction for 0/1 knapsack.
- Forgetting impossible-state sentinels.

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
