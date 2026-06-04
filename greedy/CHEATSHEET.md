# Greedy Cheatsheet

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

### Sort and Scan

```text
state = initial_state
for candidate in input:
    if candidate can improve state:
        update state
    if state is valid:
        update answer
```

### Interval Greedy

```text
state = initial_state
for candidate in input:
    if candidate can improve state:
        update state
    if state is valid:
        update answer
```

### Jump Greedy

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
| Sort and Scan | Use when the prompt matches sort and scan signals. |
| Interval Greedy | Use when the prompt matches interval greedy signals. |
| Jump Greedy | Use when the prompt matches jump greedy signals. |
| Heap Greedy | Use when the prompt matches heap greedy signals. |
| Exchange Argument | Use when the prompt matches exchange argument signals. |
| Greedy with Counts | Use when the prompt matches greedy with counts signals. |

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

[Previous](../greedy/README.md) | [Home](../README.md) | [Next](../greedy/PATTERNS.md)
