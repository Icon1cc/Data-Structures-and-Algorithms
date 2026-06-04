# Trees Cheatsheet

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

### Recursive DFS

```text
state = initial_state
for candidate in input:
    if candidate can improve state:
        update state
    if state is valid:
        update answer
```

### Iterative DFS

```text
state = initial_state
for candidate in input:
    if candidate can improve state:
        update state
    if state is valid:
        update answer
```

### Level Order BFS

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
| Recursive DFS | Use when the prompt matches recursive dfs signals. |
| Iterative DFS | Use when the prompt matches iterative dfs signals. |
| Level Order BFS | Use when the prompt matches level order bfs signals. |
| BST Invariant | Use when the prompt matches bst invariant signals. |
| Lowest Common Ancestor | Use when the prompt matches lowest common ancestor signals. |
| Tree DP | Use when the prompt matches tree dp signals. |

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

[Previous](../trees/README.md) | [Home](../README.md) | [Next](../trees/PATTERNS.md)
