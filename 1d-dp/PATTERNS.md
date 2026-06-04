# 1-D Dynamic Programming Patterns

This file is the main pattern-recognition reference for 1-d dynamic programming. Each pattern explains why it works, when it fits, when to avoid it, and how to start coding it.

## Pattern: Memoization

### Intuition

Cache recursive state results so repeated subproblems are solved once.

### When To Use It

Use when recursion revisits the same index, amount, or state.

### When Not To Use It

Do not cache mutable state without converting it to a stable key.

### Recognition Signals

- memoization
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- House Robber
- Coin Change

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
memo = {}
def solve(state):
    if state in memo: return memo[state]
    memo[state] = combine(children)
```

## Pattern: Tabulation

### Intuition

Fill a DP table from base cases toward larger states.

### When To Use It

Use when dependency order is clear and iterative code is simpler.

### When Not To Use It

Do not fill a state before its dependencies are ready.

### Recognition Signals

- tabulation
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Coin Change
- Longest Increasing Subsequence

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
dp[base] = value
for state in order:
    dp[state] = transition(previous states)
```

## Pattern: Rolling State

### Intuition

Keep only the last few states required by the recurrence.

### When To Use It

Use for Fibonacci-like, climbing stairs, and row-by-row DP.

### When Not To Use It

Do not compress before proving old states are no longer needed.

### Recognition Signals

- rolling state
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Longest Increasing Subsequence
- House Robber

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
prev2, prev1 = base0, base1
for i in range(2, n):
    curr = f(prev1, prev2)
    prev2, prev1 = prev1, curr
```

## Pattern: House Robber Choice

### Intuition

At each position, choose between taking current plus a non-adjacent state or skipping it.

### When To Use It

Use for non-adjacent selection and take-skip DP.

### When Not To Use It

Do not use it when conflicts are not limited to adjacency.

### Recognition Signals

- house robber choice
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- House Robber
- Coin Change

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
dp[i] = max(dp[i-1], dp[i-2] + value[i])
```

## Pattern: Coin Change

### Intuition

Build answers for amounts by trying coin transitions.

### When To Use It

Use for minimum coins, number of ways, and unbounded knapsack.

### When Not To Use It

Do not mix loop order for combinations and permutations accidentally.

### Recognition Signals

- coin change
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Coin Change
- Longest Increasing Subsequence

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for coin in coins:
    for amount in range(coin, target + 1):
        update dp[amount]
```

## Pattern: Longest Increasing Subsequence

### Intuition

Track the best increasing sequence ending at each value, or maintain patience-sorting tails.

### When To Use It

Use for ordered subsequence optimization.

### When Not To Use It

Do not confuse subsequences with contiguous subarrays.

### Recognition Signals

- longest increasing subsequence
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Longest Increasing Subsequence
- House Robber

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
tails = []
for x in nums:
    i = lower_bound(tails, x)
    replace or append x
```
---

## Navigation

[Previous](../1d-dp/CHEATSHEET.md) | [Home](../README.md) | [Next](../1d-dp/easy.md)
