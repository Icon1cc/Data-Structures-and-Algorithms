# Stack Cheatsheet

Fast revision notes for stack before interviews.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| Monotonic scan | O(n) total |

## Formulas And Invariants

- Define the invariant before writing loops or recursion.
- Track exactly what state means at each step.
- Prefer deterministic boundary rules over intuition.
- Re-check empty input, one item, duplicate values, and maximum-size constraints.

## Pattern Summary

| Pattern | Use When |
|---|---|
| Balanced Delimiters | Use for parentheses, tags, and nested syntax. |
| Expression Evaluation | Use for RPN, calculators, and encoded strings. |
| Monotonic Increasing Stack | Use for previous smaller, histogram, and subarray minimums. |
| Monotonic Decreasing Stack | Use for next greater element and temperatures. |
| Simulation Stack | Use for path simplification, asteroid collisions, and editor-like commands. |
| Auxiliary Stack | Use when the stack must answer extra queries in O(1). |

## Common Templates

### Balanced Delimiters

```text
for ch in s:
    if ch in opens: stack.append(ch)
    else: verify stack.pop() matches ch
```

### Expression Evaluation

```text
for token in tokens:
    if number: stack.append(number)
    else: apply operator to top operands
```

### Monotonic Increasing Stack

```text
for i, x in enumerate(values):
    while stack and values[stack[-1]] > x:
        j = stack.pop()
```

## Recognition Hints

Look for nested parentheses, next greater or previous smaller values, reversible operations, path simplification, or resolving recent items first.

## Common Traps

- Not checking empty stack before peek.
- Using stack order when queue order is required.
- Forgetting that monotonic stacks are amortized linear.

## Interview Reminders

- Say the brute force solution first.
- Explain why the optimized pattern removes repeated work.
- Test at least one normal case, one edge case, and one failure case.
- Include auxiliary space in the final complexity.


---

## Navigation

[Previous](../stack/README.md) | [Home](../README.md) | [Next](../stack/PATTERNS.md)
