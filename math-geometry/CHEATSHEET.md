# Math & Geometry Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

This topic covers modular arithmetic, divisibility, greatest common divisor, primes, coordinates, slopes, rotations, and matrix traversal.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Euclid GCD | O(log min(a,b)) |
| Sieve | O(n log log n) |
| Matrix traversal | O(mn) |
| Pairwise geometry | O(n^2) |

## Space Table

| Case | Complexity |
|---|---:|
| Formula only | O(1) |
| Sieve array | O(n) |
| Matrix output | O(mn) |
| Slope map | O(n) |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Modulo Arithmetic | Use for cyclic arrays, clocks, hashes, and large counts. |
| GCD And LCM | Use for fractions, slopes, grouping by ratio, and common periods. |
| Prime Sieve | Use when many prime queries share an upper bound. |
| Matrix Traversal | Use for spiral order, rotation, and diagonal traversal. |
| Coordinate Geometry | Use for lines, hulls, and nearest or collinear points. |
| Randomized Prefix | Use for weighted random pick and reservoir sampling variants. |

## Recognition Hints

Look for rotate matrix, spiral, lines, slopes, random weights, divisibility, primes, powers, palindrome numbers, or arithmetic overflow.

## Templates

### Modulo Arithmetic

```text
normalized = ((x % m) + m) % m
```

### GCD And LCM

```text
while b:
    a, b = b, a % b
```

### Prime Sieve

```text
is_prime = [True] * n
for p in range(2, sqrt(n)):
    if is_prime[p]: mark multiples
```

### Matrix Traversal

```text
top, bottom, left, right = bounds
while top <= bottom and left <= right:
    traverse edges and shrink
```

## Common Traps

- Comparing floating-point slopes directly.
- Ignoring negative modulo behavior.
- Using O(n^2) geometry without normalizing duplicates.
- Forgetting overflow in multiplication or exponentiation.

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
