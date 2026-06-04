# Stack Patterns

Patterns are the bridge between theory and interview execution. Read these before solving the curated problems.
## Pattern: Balanced Delimiters

### Intuition

Push opening tokens and require matching closing tokens.

### When To Use It

Use for parentheses, tags, and nested syntax.

### When Not To Use It

Do not use for crossing dependencies that are not nested.

### Recognition Signals

- parentheses
- brackets
- nested

### Problem Examples

- Valid Parentheses
- Remove Outermost Parentheses

### Common Mistakes

- Accepting leftover openings
- Not checking mismatched types

### Reusable Template Or Pseudocode

```text
for ch in s:
    if ch in opens: stack.append(ch)
    else: verify stack.pop() matches ch
```

## Pattern: Expression Evaluation

### Intuition

Use stacks to defer operations until precedence or closing tokens allow evaluation.

### When To Use It

Use for RPN, calculators, and encoded strings.

### When Not To Use It

Do not use when a grammar parser would be clearer for a large language.

### Recognition Signals

- calculator
- expression
- RPN
- decode

### Problem Examples

- Evaluate Reverse Polish Notation
- Basic Calculator

### Common Mistakes

- Incorrect operator precedence
- Not handling unary minus

### Reusable Template Or Pseudocode

```text
for token in tokens:
    if number: stack.append(number)
    else: apply operator to top operands
```

## Pattern: Monotonic Increasing Stack

### Intuition

Keep stack values increasing so smaller previous candidates remain available.

### When To Use It

Use for previous smaller, histogram, and subarray minimums.

### When Not To Use It

Do not use when comparisons are not transitive or values can become stale without indices.

### Recognition Signals

- previous smaller
- histogram
- minimums

### Problem Examples

- Largest Rectangle in Histogram
- Sum of Subarray Minimums

### Common Mistakes

- Using > instead of >= with duplicates
- Forgetting sentinel values

### Reusable Template Or Pseudocode

```text
for i, x in enumerate(values):
    while stack and values[stack[-1]] > x:
        j = stack.pop()
```

## Pattern: Monotonic Decreasing Stack

### Intuition

Keep stack values decreasing so greater previous candidates remain available.

### When To Use It

Use for next greater element and temperatures.

### When Not To Use It

Do not use when there is no nearest greater or dominance relation.

### Recognition Signals

- next greater
- warmer day
- span

### Problem Examples

- Daily Temperatures
- Next Greater Element II

### Common Mistakes

- Returning values instead of distances
- Ignoring circular traversal

### Reusable Template Or Pseudocode

```text
for i, x in enumerate(values):
    while stack and values[stack[-1]] < x:
        j = stack.pop()
```

## Pattern: Simulation Stack

### Intuition

Model operations exactly with a stack when the last operation is undone first.

### When To Use It

Use for path simplification, asteroid collisions, and editor-like commands.

### When Not To Use It

Do not use when the real system is FIFO or priority ordered.

### Recognition Signals

- collisions
- undo
- path
- logs

### Problem Examples

- Asteroid Collision
- Simplify Path

### Common Mistakes

- Not resolving repeated collisions
- Keeping no-op tokens

### Reusable Template Or Pseudocode

```text
for item in stream:
    while stack and conflict(stack[-1], item): resolve
    maybe push item
```

## Pattern: Auxiliary Stack

### Intuition

Keep a second stack of derived facts such as minimum values.

### When To Use It

Use when the stack must answer extra queries in O(1).

### When Not To Use It

Do not use if the derived fact can be recomputed cheaply and queries are rare.

### Recognition Signals

- min stack
- max stack
- constant query

### Problem Examples

- Min Stack
- Maximum Frequency Stack

### Common Mistakes

- Not syncing auxiliary stack on pop
- Not handling duplicate minima

### Reusable Template Or Pseudocode

```text
values.append(x)
mins.append(min(x, mins[-1] if mins else x))
```

---

## Navigation

[Previous](../stack/CHEATSHEET.md) | [Home](../README.md) | [Next](../stack/easy.md)
