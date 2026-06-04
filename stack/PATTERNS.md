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

- Stopping after one resolution per new item; one asteroid may annihilate many stack entries before settling.
- Forgetting to push the survivor when the new item wins a collision; the survivor must continue interacting with future items.
- Using a queue instead of a stack when the problem says "most recent"; FIFO breaks the LIFO invariant silently.

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

- Returning true when the loop ends with a non-empty stack; unmatched opens must fail validation.
- Popping from an empty stack on an unexpected closer; check `stack` before `stack.pop()`.
- Replacing the type-aware stack with a single counter when there are multiple bracket kinds; counters cannot detect `(]`.

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

- Storing values when indices are needed for widths; switch to indices and look up `nums[stack[-1]]` for the value.
- Forgetting the sentinel pass; without a final flush, indices left on the stack never compute their right boundary.
- Using `>` instead of `>=` (or vice versa) at the pop comparison; equal-value tie-breaking changes whether the algorithm finds the leftmost or rightmost occurrence.

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

- Computing `i - j` after popping but using the wrong popped variable, returning the distance from the wrong index.
- Treating ties as "not greater"; choose strict `<` or `<=` based on whether equal values count as warmer.
- Leaving unresolved indices in the stack with no default answer; for next-greater problems, default to 0 or `-1`.

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

- Reversing operand order on subtraction or division; pop the right operand first, then the left.
- Forgetting to push the running result onto the operator stack on `(`, then restore it on `)`.
- Treating Python's `//` as truncating toward zero; for negatives, use `int(a / b)` to match RPN semantics.

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
