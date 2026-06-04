# Stack Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| LIFO Simulation | most recent | Do not use when the oldest item must leave first |
| Balanced Delimiters | balanced | Do not use counts alone when delimiter type and order matter |
| Monotonic Increasing Stack | previous smaller | Do not use if the nearest unresolved relationship is not ordered |
| Monotonic Decreasing Stack | next greater | Do not use if every item can be resolved independently without order |
| Expression Stack | operators | Do not use ad hoc string parsing without a precedence model |

## Pattern: LIFO Simulation

### Beginner Intuition

Model a process where the newest unresolved item must be handled first.

### When To Use It

Use for collisions, undo, browser history, and simplified paths.

### When Not To Use It

Do not use when the oldest item must leave first.

### Recognition Signals

- most recent
- undo
- collision
- path

### Example Problems

- Asteroid Collision
- Simplify Path

### Common Mistakes

- Forgetting that multiple stack items may be resolved by one new item.
- Ignoring the exclusion case for LIFO Simulation: Do not use when the oldest item must leave first.
- Failing to test empty stack, equal values, sentinel handling, and index versus value storage against the stated invariant.

### Pseudocode Or Template

```text
stack = []
for item in items:
    while stack and resolves(stack[-1], item):
        stack.pop()
    stack.append(item)
```

### Complexity Notes

O(n) time, O(n) space.

### Interview Explanation

The stack mirrors the process order, so top is the only unresolved item that can interact now.

## Pattern: Balanced Delimiters

### Beginner Intuition

Push open tokens and require closing tokens to match the top.

### When To Use It

Use for parentheses, brackets, tags, and nested syntax.

### When Not To Use It

Do not use counts alone when delimiter type and order matter.

### Recognition Signals

- balanced
- nested
- brackets
- close matches open

### Example Problems

- Valid Parentheses

### Common Mistakes

- Accepting the string when the stack still has opens.
- Ignoring the exclusion case for Balanced Delimiters: Do not use counts alone when delimiter type and order matter.
- Failing to test empty stack, equal values, sentinel handling, and index versus value storage against the stated invariant.

### Pseudocode Or Template

```text
for ch in s:
    if ch in opens: stack.append(ch)
    else: require stack and stack.pop() matches ch
```

### Complexity Notes

O(n) time, O(depth) space.

### Interview Explanation

Order matters, so every close must match the most recent unmatched open.

## Pattern: Monotonic Increasing Stack

### Beginner Intuition

Keep indices whose values increase so smaller previous elements remain available.

### When To Use It

Use for previous smaller, histogram widths, and removing larger elements.

### When Not To Use It

Do not use if the nearest unresolved relationship is not ordered.

### Recognition Signals

- previous smaller
- histogram
- increasing stack

### Example Problems

- Largest Rectangle in Histogram
- Remove Duplicate Letters

### Common Mistakes

- Storing values when indices are needed for widths.
- Ignoring the exclusion case for Monotonic Increasing Stack: Do not use if the nearest unresolved relationship is not ordered.
- Failing to test empty stack, equal values, sentinel handling, and index versus value storage against the stated invariant.

### Pseudocode Or Template

```text
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] > x:
        stack.pop()
    stack.append(i)
```

### Complexity Notes

O(n) amortized time, O(n) space.

### Interview Explanation

Each popped item has found the first value that makes it impossible to remain a candidate.

## Pattern: Monotonic Decreasing Stack

### Beginner Intuition

Keep indices whose values decrease so greater future values can resolve them.

### When To Use It

Use for next greater, temperatures, spans, and visibility.

### When Not To Use It

Do not use if every item can be resolved independently without order.

### Recognition Signals

- next greater
- warmer day
- stock span

### Example Problems

- Daily Temperatures
- Online Stock Span

### Common Mistakes

- Forgetting to compute distance before popping the index.
- Ignoring the exclusion case for Monotonic Decreasing Stack: Do not use if every item can be resolved independently without order.
- Failing to test empty stack, equal values, sentinel handling, and index versus value storage against the stated invariant.

### Pseudocode Or Template

```text
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        j = stack.pop()
        answer[j] = i - j
    stack.append(i)
```

### Complexity Notes

O(n) amortized time, O(n) space.

### Interview Explanation

The current value resolves all smaller unresolved values on top of the stack.

## Pattern: Expression Stack

### Beginner Intuition

Use stacks to delay operators or operands until precedence and parentheses are known.

### When To Use It

Use for RPN, calculators, and nested expression evaluation.

### When Not To Use It

Do not use ad hoc string parsing without a precedence model.

### Recognition Signals

- operators
- operands
- calculator
- precedence

### Example Problems

- Evaluate Reverse Polish Notation
- Basic Calculator

### Common Mistakes

- Dropping the sign before entering a parenthesized expression.
- Ignoring the exclusion case for Expression Stack: Do not use ad hoc string parsing without a precedence model.
- Failing to test empty stack, equal values, sentinel handling, and index versus value storage against the stated invariant.

### Pseudocode Or Template

```text
for token in tokens:
    if number: values.push(number)
    elif operator: apply according to precedence
```

### Complexity Notes

O(n) time, O(n) space.

### Interview Explanation

I separate parsing from evaluation state so precedence is explicit.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
