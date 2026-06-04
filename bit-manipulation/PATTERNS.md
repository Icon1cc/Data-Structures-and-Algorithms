# Bit Manipulation Patterns

This file is the main pattern-recognition reference for bit manipulation. Each pattern explains why it works, when it fits, when to avoid it, and how to start coding it.

## Pattern: XOR Cancellation

### Intuition

Equal values cancel under XOR, leaving the value that appears odd or differs.

### When To Use It

Use for single number, missing number, and parity differences.

### When Not To Use It

Do not use when values appear arbitrary counts without bit counting.

### Recognition Signals

- xor cancellation
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Single Number
- Counting Bits

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
ans = 0
for x in nums:
    ans ^= x
```

## Pattern: Bit Counting

### Intuition

Count set bits directly or use recurrence over smaller numbers.

### When To Use It

Use for hamming weight, counting bits, and parity.

### When Not To Use It

Do not loop on signed negative numbers without fixed-width handling.

### Recognition Signals

- bit counting
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Counting Bits
- Shortest Path Visiting All Nodes

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
while x:
    x &= x - 1
    count += 1
```

## Pattern: Masks for Sets

### Intuition

Represent a small set as bits in an integer.

### When To Use It

Use for visited sets, skills, subsets, and compact state keys.

### When Not To Use It

Do not use when n is too large for exponential masks.

### Recognition Signals

- masks for sets
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Shortest Path Visiting All Nodes
- Single Number

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
mask | (1 << i)  # add item i
mask & ~(1 << i)  # remove item i
```

## Pattern: Subset Enumeration

### Intuition

Iterate masks or submasks to cover all subsets.

### When To Use It

Use for small-n exhaustive search and subset DP.

### When Not To Use It

Do not use beyond feasible n without pruning.

### Recognition Signals

- subset enumeration
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Single Number
- Counting Bits

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
sub = mask
while sub:
    process(sub)
    sub = (sub - 1) & mask
```

## Pattern: Bitwise Trie

### Intuition

Store numbers by bits and greedily follow opposite bits to maximize XOR.

### When To Use It

Use for maximum XOR and constrained XOR queries.

### When Not To Use It

Do not forget fixed bit width and query constraints.

### Recognition Signals

- bitwise trie
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Counting Bits
- Shortest Path Visiting All Nodes

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for bit in reversed(range(max_bit)):
    preferred = 1 - current_bit
    take preferred child if present
```

## Pattern: Bitmask DP

### Intuition

Use mask plus optional position as a state that records chosen or visited elements.

### When To Use It

Use for shortest path over subsets, teams, and games.

### When Not To Use It

Do not forget that state count grows exponentially.

### Recognition Signals

- bitmask dp
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Shortest Path Visiting All Nodes
- Single Number

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
dp[mask][last] = best value
transition by adding one unset bit
```
---

## Navigation

[Previous](../bit-manipulation/CHEATSHEET.md) | [Home](../README.md) | [Next](../bit-manipulation/easy.md)
