# Bit Manipulation Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| XOR Cancellation | single number | Do not use when duplicates appear more than twice unless adjusted |
| Bit Counting | number of 1 bits | Do not loop forever on negative values in fixed-width languages |
| Masks For Sets | subset | Do not use masks when n is too large for exponential states |
| Single Bit Checks | power of two | Do not use modulo when bit logic is clearer for powers of two |
| Submask Enumeration | submask | Do not use when all 2^n masks are already too many |
| Arithmetic Bit Tricks | shift | Do not ignore overflow and sign limits in fixed-width languages |

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

- Applying XOR to Single Number II (each value appears three times); pure XOR fails because three copies do not cancel. Use bit counts mod 3 instead.
- For Single Number III (two unique values), failing to partition by a differing bit; the XOR of all values gives `a ^ b`, then split inputs by any set bit of that XOR.
- Initializing the running XOR to a non-zero value; the identity is 0.

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

- Using `n >>= 1` on a signed negative integer in C or Java; the sign bit shifts in and the loop never terminates. Use unsigned shift or mask first.
- Iterating 32 times when Brian Kernighan's `n &= n - 1` runs in popcount steps.
- For Counting Bits DP, choosing `count[i] = count[i / 2] + (i & 1)` but indexing as `count[i // 2]` outside Python; integer division semantics differ.

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

- Computing `1 << i` for `i >= 31` in Java or C without `1L`; the literal is `int` and overflows silently.
- Iterating `for mask in range(1 << n)` when `n > 20` and expecting it to terminate in interview time.
- Using `mask & i` to test bit `i` instead of `mask & (1 << i)`; the former tests against the value of `i`, not its bit position.

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

- Returning `True` for `x == 0` in `x & (x - 1) == 0`; zero is not a power of two, so guard with `x > 0`.
- Confusing `x & -x` (lowest set bit value) with `x ^ (x - 1)` (mask of low bits up to the lowest set bit).
- Using arithmetic `% 2` for parity in tight loops; the bitwise `& 1` is equivalent and often slightly faster.

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

- Forgetting that the empty submask `0` is excluded by the loop condition `while sub:`; if you need it, handle it before the loop.
- Iterating submasks in lexicographic order without realizing the `(sub - 1) & mask` trick visits them in descending integer order.
- Misanalyzing the total cost; summing `2^popcount(mask)` over all masks of `[0, 2^n)` gives `3^n`, not `4^n`.

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

- Implementing add-without-plus and forgetting to mask both operands to 32 bits in languages without arbitrary-precision integers.
- For Divide Two Integers, ignoring the overflow case `INT_MIN / -1`; return `INT_MAX` per the spec.
- Using `<<` on a Python int that is negative; the result keeps the sign and may differ from C semantics.

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
