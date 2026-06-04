# Bit Manipulation Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

Bit manipulation operates on the binary representation of integers using AND, OR, XOR, NOT, shifts, and masks.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Single bit operation | O(1) |
| Scan word bits | O(word_size) |
| Submask enumeration | O(3^n) across all masks |
| Bitmask DP | O(n * 2^n) common |

## Space Table

| Case | Complexity |
|---|---:|
| Single mask | O(1) |
| Mask DP table | O(2^n) |
| Bit count table | O(n) |

## Pattern Summary

| Pattern | Use When |
|---|---|
| XOR Cancellation | Use for single-number and missing-number style problems. |
| Bit Counting | Use for Hamming weight and counting bits ranges. |
| Masks For Sets | Use when n is small enough for 2^n states. |
| Single Bit Checks | Use for power-of-two and permission checks. |
| Submask Enumeration | Use for subset DP and combinatorial optimization. |
| Arithmetic Bit Tricks | Use for sum without plus, divide integers, and range bitwise AND. |

## Recognition Hints

Look for single number, parity, powers of two, subset masks, permissions, turn bits on or off, XOR ranges, or constraints with n <= 20.

## Templates

### XOR Cancellation

```text
ans = 0
for x in nums:
    ans ^= x
```

### Bit Counting

```text
while x:
    x &= x - 1
    count += 1
```

### Masks For Sets

```text
mask |= 1 << i
if mask & (1 << i): present
```

### Single Bit Checks

```text
is_power_two = x > 0 and (x & (x - 1)) == 0
```

## Common Traps

- Confusing bit index with bit value.
- Forgetting signed integer behavior in fixed-width languages.
- Using addition where XOR without carry is intended.
- Missing parentheses around shifts and masks.

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
