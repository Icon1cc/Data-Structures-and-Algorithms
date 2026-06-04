# 1-D Dynamic Programming Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern: State Definition

### Beginner Intuition

Write exactly what dp[i] means before choosing a recurrence.

### When To Use It

Use for every DP problem.

### When Not To Use It

Do not code transitions before the state has a precise English meaning.

### Recognition Signals

- dp meaning
- state
- recurrence

### Example Problems

- Climbing Stairs
- House Robber

### Common Mistakes

- Changing state meaning midway through code.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
dp[i] = answer for the prefix ending at i
# or answer using first i items
```

### Complexity Notes

Complexity equals number of states times transition cost.

### Interview Explanation

I start by defining state because recurrence and base cases follow from it.

## Pattern: Memoization

### Beginner Intuition

Keep recursive structure but cache each state result.

### When To Use It

Use when top-down choices are easier to express than fill order.

### When Not To Use It

Do not use if recursion depth will exceed limits and bottom-up is simple.

### Recognition Signals

- recursive
- cache
- overlapping

### Example Problems

- Word Break
- Coin Change

### Common Mistakes

- Caching by incomplete state keys.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
memo = {}
def solve(i):
    if i in memo: return memo[i]
    memo[i] = combine(next states)
    return memo[i]
```

### Complexity Notes

O(states * transition cost) time, O(states) space.

### Interview Explanation

Memoization turns exponential repeated recursion into one computation per state.

## Pattern: Tabulation

### Beginner Intuition

Fill states iteratively from base cases to final answer.

### When To Use It

Use when dependency order is clear.

### When Not To Use It

Do not fill before dependencies are initialized.

### Recognition Signals

- bottom up
- table
- fill order

### Example Problems

- Min Cost Climbing Stairs
- Decode Ways

### Common Mistakes

- Using dp[i-1] before it is defined.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
dp = [base values]
for i in fill_order:
    dp[i] = transition(previous states)
```

### Complexity Notes

O(states * transition cost) time.

### Interview Explanation

The table makes dependency order explicit and avoids recursion stack risk.

## Pattern: Transition Choice

### Beginner Intuition

List all legal previous choices that can lead to the current state.

### When To Use It

Use for min/max/counting DP.

### When Not To Use It

Do not include choices that violate problem constraints.

### Recognition Signals

- choose skip
- min cost
- max profit

### Example Problems

- House Robber
- Best Time to Buy and Sell Stock IV

### Common Mistakes

- Taking max when the problem asks for count, or sum when choices are exclusive.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
dp[i] = best(dp[i - 1], value[i] + dp[i - 2])
```

### Complexity Notes

Depends on number of choices per state.

### Interview Explanation

Each transition is one legal final move into the state.

## Pattern: Knapsack

### Beginner Intuition

Choose or skip items under a capacity or target constraint.

### When To Use It

Use for subset sum, partition, and bounded resource selection.

### When Not To Use It

Do not iterate capacity forward for 0/1 choices if it reuses the same item.

### Recognition Signals

- capacity
- target
- choose skip

### Example Problems

- Partition Equal Subset Sum
- Coin Change II

### Common Mistakes

- Using unbounded update order for a 0/1 problem.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
for item in items:
    for cap in reversed(range(item, target + 1)):
        dp[cap] |= dp[cap - item]
```

### Complexity Notes

O(n * capacity) time, O(capacity) space when compressed.

### Interview Explanation

Capacity dimension records what totals are reachable after considering items.

## Pattern: Subsequence DP

### Beginner Intuition

Optimize or count choices that preserve order but may skip elements.

### When To Use It

Use for LIS, word break variants, and sequence scoring.

### When Not To Use It

Do not require contiguity unless the problem says substring or subarray.

### Recognition Signals

- subsequence
- skip
- order preserved

### Example Problems

- Longest Increasing Subsequence
- Word Break

### Common Mistakes

- Confusing subsequence with substring.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
for i in range(n):
    for j in range(i):
        if can_extend(j, i): dp[i] = best(dp[i], dp[j] + 1)
```

### Complexity Notes

O(n^2) common, sometimes O(n log n).

### Interview Explanation

The current element can extend compatible earlier states.

## Pattern: State Compression

### Beginner Intuition

Keep only the previous states needed by the recurrence.

### When To Use It

Use when dp[i] depends on a fixed small window of earlier states.

### When Not To Use It

Do not compress when later transitions still need overwritten values.

### Recognition Signals

- rolling
- previous two
- space optimize

### Example Problems

- Climbing Stairs
- House Robber

### Common Mistakes

- Updating variables in the wrong order.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
prev2, prev1 = base0, base1
for i in range(2, n + 1):
    cur = transition(prev1, prev2)
    prev2, prev1 = prev1, cur
```

### Complexity Notes

Same time, reduced space often O(1).

### Interview Explanation

Compression is safe only after proving old states are never needed again.

## Pattern: Kadane

### Beginner Intuition

Track the best subarray ending here and the best seen anywhere.

### When To Use It

Use for maximum subarray and local extend-or-restart decisions.

### When Not To Use It

Do not use for subsequences or non-contiguous choices.

### Recognition Signals

- maximum subarray
- extend or restart

### Example Problems

- Maximum Subarray

### Common Mistakes

- Initializing best to zero when all values may be negative.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
best_end = best = nums[0]
for x in nums[1:]:
    best_end = max(x, best_end + x)
    best = max(best, best_end)
```

### Complexity Notes

O(n) time, O(1) space.

### Interview Explanation

At each index, the best ending here either starts here or extends the previous best ending.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
