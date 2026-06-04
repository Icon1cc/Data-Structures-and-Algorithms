# Math & Geometry Patterns

This file is the main pattern-recognition reference for math & geometry. Each pattern explains why it works, when it fits, when to avoid it, and how to start coding it.

## Pattern: Modulo Arithmetic

### Intuition

Use remainders to reason about divisibility, cycles, and large numbers.

### When To Use It

Use for wraparound, huge counts, and divisibility constraints.

### When Not To Use It

Do not divide under modulo unless modular inverse rules apply.

### Recognition Signals

- modulo arithmetic
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Rotate Image
- Max Points on a Line

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
value = (value * base + digit) % mod
```

## Pattern: GCD and Number Theory

### Intuition

Use gcd, lcm, primes, and factors to normalize numeric relationships.

### When To Use It

Use for fractions, slopes, divisibility, and coprime checks.

### When Not To Use It

Do not brute force factors when sqrt or Euclid is enough.

### Recognition Signals

- gcd and number theory
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Max Points on a Line
- Erect the Fence

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
while b:
    a, b = b, a % b
```

## Pattern: Matrix Traversal

### Intuition

Move through matrix layers, rows, columns, or diagonals with explicit boundaries.

### When To Use It

Use for rotation, spiral order, and matrix transformations.

### When Not To Use It

Do not double-visit center rows or columns.

### Recognition Signals

- matrix traversal
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Erect the Fence
- Rotate Image

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
top, bottom, left, right = 0, rows - 1, 0, cols - 1
while top <= bottom and left <= right: traverse layer
```

## Pattern: Coordinate Hashing

### Intuition

Store points or normalized coordinate facts in sets and maps.

### When To Use It

Use for rectangles, squares, duplicate points, and fast point lookup.

### When Not To Use It

Do not use raw lists as keys or floating keys when integer tuples work.

### Recognition Signals

- coordinate hashing
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Rotate Image
- Max Points on a Line

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
points.add((x, y))
if needed_point in points: update answer
```

## Pattern: Line and Slope

### Intuition

Normalize slope as an integer pair using gcd and count equal slopes from each anchor.

### When To Use It

Use for collinearity and maximum points on a line.

### When Not To Use It

Do not use floating-point slopes due precision and vertical lines.

### Recognition Signals

- line and slope
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Max Points on a Line
- Erect the Fence

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
dx, dy = x2 - x1, y2 - y1
g = gcd(abs(dx), abs(dy))
key = (dx // g, dy // g)
```

## Pattern: Geometry Simulation

### Intuition

Update coordinates, direction, or area according to exact geometric rules.

### When To Use It

Use for robot movement, reflection, rectangles, and boundary simulation.

### When Not To Use It

Do not skip duplicate, zero-area, and overflow cases.

### Recognition Signals

- geometry simulation
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Erect the Fence
- Rotate Image

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
position += direction
if turn: direction = rotate(direction)
```
---

## Navigation

[Previous](../math-geometry/CHEATSHEET.md) | [Home](../README.md) | [Next](../math-geometry/easy.md)
