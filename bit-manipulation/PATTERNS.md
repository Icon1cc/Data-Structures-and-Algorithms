# Bit Manipulation Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern: XOR Cancellation

### Beginner Intuition

Equal values cancel, leaving the unmatched value or parity signal.

### When To Use It

Use for single-number and missing-number style problems.

### When Not To Use It

Do not use when duplicates appear more than twice unless adjusted.

### Recognition Signals

- single number
- cancel
- parity

### Example Problems

- Single Number
- Missing Number

### Common Mistakes

- Forgetting that XOR ignores order but not multiplicity.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
ans = 0
for x in nums:
    ans ^= x
```

### Complexity Notes

O(n) time, O(1) space.

### Interview Explanation

Pairs cancel to zero, so only unmatched bits remain.

## Pattern: Bit Counting

### Beginner Intuition

Count set bits directly or reuse smaller counts.

### When To Use It

Use for Hamming weight and counting bits ranges.

### When Not To Use It

Do not loop forever on negative values in fixed-width languages.

### Recognition Signals

- number of 1 bits
- hamming weight
- popcount

### Example Problems

- Number of 1 Bits
- Counting Bits

### Common Mistakes

- Using n >>= 1 on signed negative values without width control.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
while x:
    x &= x - 1
    count += 1
```

### Complexity Notes

O(number of set bits) for one value, O(n) for DP table.

### Interview Explanation

Clearing the lowest set bit makes progress one bit at a time.

## Pattern: Masks For Sets

### Beginner Intuition

Represent membership of small sets as bits in an integer.

### When To Use It

Use when n is small enough for 2^n states.

### When Not To Use It

Do not use masks when n is too large for exponential states.

### Recognition Signals

- subset
- mask
- permissions
- n <= 20

### Example Problems

- Subsets
- Smallest Sufficient Team

### Common Mistakes

- Confusing mask value with item index.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
mask |= 1 << i
if mask & (1 << i): present
```

### Complexity Notes

O(1) operations, O(2^n) for full mask DP.

### Interview Explanation

Each bit answers whether an item is included.

## Pattern: Single Bit Checks

### Beginner Intuition

Test powers of two, low bits, and flags with masks.

### When To Use It

Use for power-of-two and permission checks.

### When Not To Use It

Do not use modulo when bit logic is clearer for powers of two.

### Recognition Signals

- power of two
- flag
- low bit

### Example Problems

- Power of Two
- Reverse Bits

### Common Mistakes

- Not excluding zero for power-of-two tests.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
is_power_two = x > 0 and (x & (x - 1)) == 0
```

### Complexity Notes

O(1) time.

### Interview Explanation

A power of two has exactly one set bit.

## Pattern: Submask Enumeration

### Beginner Intuition

Iterate every submask of a mask efficiently.

### When To Use It

Use for subset DP and combinatorial optimization.

### When Not To Use It

Do not use when all 2^n masks are already too many.

### Recognition Signals

- submask
- subset dp
- mask loop

### Example Problems

- Partition to K Equal Sum Subsets
- Smallest Sufficient Team

### Common Mistakes

- Forgetting that submask 0 needs separate handling if required.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
sub = mask
while sub:
    process(sub)
    sub = (sub - 1) & mask
```

### Complexity Notes

O(3^n) over all masks, O(2^k) for one mask with k bits.

### Interview Explanation

The bit trick walks only subsets of the current mask.

## Pattern: Arithmetic Bit Tricks

### Beginner Intuition

Use shifts and masks for low-level arithmetic under constraints.

### When To Use It

Use for sum without plus, divide integers, and range bitwise AND.

### When Not To Use It

Do not ignore overflow and sign limits in fixed-width languages.

### Recognition Signals

- shift
- carry
- divide
- range and

### Example Problems

- Sum of Two Integers
- Bitwise AND of Numbers Range

### Common Mistakes

- Forgetting language-specific integer width.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
while carry:
    carry = (a & b) << 1
    a = a ^ b
    b = carry
```

### Complexity Notes

O(word_size) time.

### Interview Explanation

XOR adds without carry and AND shifted left carries.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
