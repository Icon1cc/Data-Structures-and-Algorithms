# 1-D Dynamic Programming Cheatsheet

Fast revision before interviews.

## Complexity Tables

| Situation | Complexity |
|---|---:|
| One pass over input | O(n) |
| Sort before processing | O(n log n) |
| Recursive or iterative traversal | O(nodes + edges or states) |
| Exponential generation | O(number of generated candidates) |

## Formulas

- DP runtime = number of states times transition cost.
- Graph traversal runtime = vertices plus edges.
- Heap update runtime = logarithm of heap size.
- Recursive space includes the call stack.

## Common Templates

### Memoization

```text
state = initial_state
for candidate in input:
    if candidate can improve state:
        update state
    if state is valid:
        update answer
```

### Tabulation

```text
state = initial_state
for candidate in input:
    if candidate can improve state:
        update state
    if state is valid:
        update answer
```

### Rolling State

```text
state = initial_state
for candidate in input:
    if candidate can improve state:
        update state
    if state is valid:
        update answer
```

## Pattern Summary

| Pattern | Recognition Hint |
|---|---|
| Memoization | Use when the prompt matches memoization signals. |
| Tabulation | Use when the prompt matches tabulation signals. |
| Rolling State | Use when the prompt matches rolling state signals. |
| House Robber Choice | Use when the prompt matches house robber choice signals. |
| Coin Change | Use when the prompt matches coin change signals. |
| Longest Increasing Subsequence | Use when the prompt matches longest increasing subsequence signals. |

## Recognition Hints

- Read constraints before choosing the algorithm.
- Ask whether order, membership, reachability, optimality, or all possibilities is central.
- Search for words that imply a known invariant.

## Common Traps

- Missing boundary cases.
- Mutating state without rollback when recursion needs it.
- Using a faster-looking approach without a correctness proof.
- Forgetting external memory such as queues, stacks, maps, and memo tables.

## Interview Reminders

- Say brute force first.
- Name the pattern and invariant.
- Code the simplest correct version.
- Test edge cases before final complexity.

---

## Navigation

[Previous](../1d-dp/README.md) | [Home](../README.md) | [Next](../1d-dp/PATTERNS.md)
