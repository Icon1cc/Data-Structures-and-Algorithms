# Stack Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

A stack supports push, pop, and top in O(1). Monotonic stacks add an invariant that values are ordered from bottom to top.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Push or pop | O(1) |
| Full monotonic scan | O(n) amortized |
| Expression parse | O(n) |

## Space Table

| Case | Complexity |
|---|---:|
| Balanced delimiter stack | O(depth) |
| Monotonic stack | O(n) worst case |
| Expression stack | O(n) |

## Pattern Summary

| Pattern | Use When |
|---|---|
| LIFO Simulation | Use for collisions, undo, browser history, and simplified paths. |
| Balanced Delimiters | Use for parentheses, brackets, tags, and nested syntax. |
| Monotonic Increasing Stack | Use for previous smaller, histogram widths, and removing larger elements. |
| Monotonic Decreasing Stack | Use for next greater, temperatures, spans, and visibility. |
| Expression Stack | Use for RPN, calculators, and nested expression evaluation. |

## Recognition Hints

Look for nested delimiters, next greater, previous smaller, stock spans, histogram areas, collision simulation, or the phrase most recent unresolved item.

## Templates

### LIFO Simulation

```text
stack = []
for item in items:
    while stack and resolves(stack[-1], item):
        stack.pop()
    stack.append(item)
```

### Balanced Delimiters

```text
for ch in s:
    if ch in opens: stack.append(ch)
    else: require stack and stack.pop() matches ch
```

### Monotonic Increasing Stack

```text
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] > x:
        stack.pop()
    stack.append(i)
```

### Monotonic Decreasing Stack

```text
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        j = stack.pop()
        answer[j] = i - j
    stack.append(i)
```

## Common Traps

- Forgetting to process values left in the stack.
- Using a stack when a queue is required by order.
- Losing indices when distances or widths are needed.
- Breaking monotonic order after equal values.

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
