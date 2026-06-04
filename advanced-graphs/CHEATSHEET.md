# Advanced Graphs Cheatsheet

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

### Dijkstra Shortest Path

```text
state = initial_state
for candidate in input:
    if candidate can improve state:
        update state
    if state is valid:
        update answer
```

### Bellman-Ford

```text
state = initial_state
for candidate in input:
    if candidate can improve state:
        update state
    if state is valid:
        update answer
```

### Floyd-Warshall

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
| Dijkstra Shortest Path | Use when the prompt matches dijkstra shortest path signals. |
| Bellman-Ford | Use when the prompt matches bellman-ford signals. |
| Floyd-Warshall | Use when the prompt matches floyd-warshall signals. |
| Minimum Spanning Tree | Use when the prompt matches minimum spanning tree signals. |
| Tarjan Bridges | Use when the prompt matches tarjan bridges signals. |
| Topological DP | Use when the prompt matches topological dp signals. |

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

[Previous](../advanced-graphs/README.md) | [Home](../README.md) | [Next](../advanced-graphs/PATTERNS.md)
