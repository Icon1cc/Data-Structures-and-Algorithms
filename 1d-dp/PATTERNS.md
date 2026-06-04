# 1-D Dynamic Programming Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| State Definition | dp meaning | Do not code transitions before the state has a precise English meaning |
| Memoization | recursive | Do not use if recursion depth will exceed limits and bottom-up is simple |
| Tabulation | bottom up | Do not fill before dependencies are initialized |
| Transition Choice | choose skip | Do not include choices that violate problem constraints |
| Knapsack | capacity | Do not iterate capacity forward for 0/1 choices if it reuses the same item |
| Subsequence DP | subsequence | Do not require contiguity unless the problem says substring or subarray |
| State Compression | rolling | Do not compress when later transitions still need overwritten values |
| Kadane | maximum subarray | Do not use for subsequences or non-contiguous choices |

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

- Writing "dp[i] is the answer" without clarifying "answer using items 0..i" versus "answer ending at i"; these are different DPs with different recurrences.
- Conflating "best ending at i" with "best up to i"; for Maximum Subarray they differ critically.
- Defining state in terms of the answer instead of a structural property; the latter generalizes to harder variants.

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

- Caching by an incomplete state key; if the recurrence depends on `(i, remaining)`, the cache must use both.
- Mutating arguments stored in the cache key; mutable lists are unhashable and dicts of mutables silently fail.
- Hitting Python's default recursion limit on long inputs; either iterate bottom-up or `sys.setrecursionlimit`.

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

- Looping `for i in range(n)` and reading `dp[i + 1]` before it is computed; choose the loop direction so dependencies are already filled.
- Forgetting to seed the base cases (`dp[0] = 1`, etc.); the recurrence depends on a correct starting state.
- Sizing the array as `n` when the recurrence reads `dp[n]`; off-by-one indices are the most common bug.

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

- Taking `max` when the question counts ways (use sum), or summing when choices are mutually exclusive (use max).
- Forgetting one legal transition; House Robber has skip-then-take and skip-then-skip; missing one breaks the recurrence.
- Including a transition that violates a constraint (e.g., taking adjacent houses) without filtering.

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

- For 0/1 knapsack, iterating capacity from low to high; that lets the same item appear multiple times.
- Swapping the loop order between item and capacity in counting variants; outer item gives unordered counts (Coin Change II), outer capacity gives ordered counts (Combination Sum IV).
- Allocating O(n * capacity) when O(capacity) suffices; the rolling 1-D array always works for 0/1 if you iterate capacity in reverse.

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

- Reading the problem as "subarray" (contiguous) when it says "subsequence" (any order-preserving selection); the recurrences are different.
- For LIS, using strict `<` versus non-strict `<=`; pick the one matching the problem.
- Falling back to O(n^2) DP when O(n log n) patience-sort is available for LIS; mention the trade-off.

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

- Overwriting `prev` before reading it for the next iteration; assign in the right order or use a temporary.
- Compressing when the recurrence reaches back further than your window assumes; verify the dependency span before reducing memory.
- Believing the time complexity changes; compression only reduces space, never time.

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

- Initializing `best` to 0 instead of `nums[0]`; an all-negative array would otherwise return 0, which is not a valid subarray.
- Updating `best` before extending `best_end`; the order matters when the new element is the entire subarray.
- Trying to use Kadane on Maximum Product Subarray without tracking the running min; negatives flip sign on multiplication.

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
