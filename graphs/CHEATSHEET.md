# Graphs Cheatsheet

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

### BFS Traversal

```text
state = initial_state
for candidate in input:
    if candidate can improve state:
        update state
    if state is valid:
        update answer
```

### DFS Traversal

```text
state = initial_state
for candidate in input:
    if candidate can improve state:
        update state
    if state is valid:
        update answer
```

### Connected Components

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
| BFS Traversal | Use when the prompt matches bfs traversal signals. |
| DFS Traversal | Use when the prompt matches dfs traversal signals. |
| Connected Components | Use when the prompt matches connected components signals. |
| Grid Graphs | Use when the prompt matches grid graphs signals. |
| Union Find | Use when the prompt matches union find signals. |
| Topological Sort | Use when the prompt matches topological sort signals. |

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

[Previous](../graphs/README.md) | [Home](../README.md) | [Next](../graphs/PATTERNS.md)
