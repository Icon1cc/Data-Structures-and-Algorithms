# Bit Manipulation Easy Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Easy order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Single Number

LeetCode: [Single Number](https://leetcode.com/problems/single-number/)

Difficulty: Easy

Pattern: XOR Cancellation

Why It Matters: The baseline XOR cancellation problem.

Skills Tested:
- Recognize that XOR is associative, commutative, and `x ^ x == 0`, so XORing every element cancels paired duplicates and leaves only the unique element.
- State the invariant: at every step, the running XOR equals the XOR of all elements seen so far; at the end, it equals the unique value.
- Handle negative integers (XOR works on two's complement bit-by-bit).
- Time O(n), space O(1), and contrast with hash set (O(n) space) and sorting (O(n log n) time).

Common Follow-Ups:
- Single Number II (LC 137) extends to triplicates with bit-counts mod 3.
- Single Number III (LC 260) finds two unique elements via XOR partitioning by a bit.
- What if some elements appear `k` times and one appears once.

## 2. Number of 1 Bits

LeetCode: [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

Difficulty: Easy

Pattern: Brian Kernighan's Bit Trick

Why It Matters: Tests low-bit clearing and binary representation.

Skills Tested:
- Recognize that `n & (n - 1)` clears the lowest set bit, enabling a loop that runs once per set bit instead of 32 times.
- State the invariant: at each iteration, `n` has had its lowest set bit cleared; the count is incremented.
- Compare with the loop-32-times approach, which is O(32) regardless of bit count.
- Time O(set bits), space O(1).

Common Follow-Ups:
- Counting Bits (LC 338) computes popcount for every value `0..n` via DP.
- Hamming Distance (LC 461) uses popcount on `x ^ y`.
- What if the integer is 64-bit or arbitrary length.

## 3. Counting Bits

LeetCode: [Counting Bits](https://leetcode.com/problems/counting-bits/)

Difficulty: Easy

Pattern: DP Using `i >> 1` Or `i & (i - 1)`

Why It Matters: Builds counts using smaller states.

Skills Tested:
- Recognize the recurrence `count[i] = count[i >> 1] + (i & 1)` (or equivalently `count[i] = count[i & (i - 1)] + 1`).
- State the invariant: at index `i`, the smaller subproblem `count[i >> 1]` is already solved, so `count[i]` is one extra add.
- Choose the recurrence that matches the iteration order; both are O(n).
- Time O(n), space O(n) for the answer.

Common Follow-Ups:
- Number of 1 Bits (LC 191) is the per-value primitive.
- What if the values are very large (use lookup tables or vectorization).
- Generalize to popcount over a range.

## 4. Reverse Bits

LeetCode: [Reverse Bits](https://leetcode.com/problems/reverse-bits/)

Difficulty: Easy

Pattern: Bitwise Shift Loop

Why It Matters: Practices fixed-width bit movement.

Skills Tested:
- Recognize that reversing a 32-bit integer is a 32-step loop: shift the result left, OR in the LSB of the input, shift the input right.
- State the invariant: after `k` steps, the result holds the lowest `k` bits of the input in reversed order in its lowest `k` positions.
- Use byte-swap-and-cache for repeated calls (precompute reversed-byte lookup).
- Time O(32), space O(1) (or O(256) lookup).

Common Follow-Ups:
- Endianness conversion is a related byte-swap problem.
- Reverse only the bottom `k` bits, leaving high bits alone.
- Reverse a 64-bit integer.

## 5. Missing Number

LeetCode: [Missing Number](https://leetcode.com/problems/missing-number/)

Difficulty: Easy

Pattern: XOR Or Sum Over `0..n`

Why It Matters: Uses cancellation over a known range.

Skills Tested:
- Recognize that XORing every index `0..n` with every value yields the missing number, since paired values cancel.
- State the invariant: at every step, the running XOR equals the XOR of indices and values seen so far; at the end, only the missing value remains.
- Alternative: sum trick: `n * (n + 1) // 2 - sum(nums)` (watch for overflow on large `n`).
- Time O(n), space O(1).

Common Follow-Ups:
- Find All Numbers Disappeared in an Array (LC 448) returns all missing.
- Find All Duplicates in an Array (LC 442) returns duplicates with in-place marking.
- What if multiple numbers are missing.

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
