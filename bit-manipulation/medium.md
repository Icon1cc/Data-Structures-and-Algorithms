# Bit Manipulation Medium Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Medium order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Sum of Two Integers

LeetCode: [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)

Difficulty: Medium

Pattern: XOR Sum Plus AND Carry

Why It Matters: Adds without plus using carry logic.

Skills Tested:
- Recognize that addition without `+` decomposes into `xor` (sum without carry) and `and shifted left by 1` (the carry); repeat until the carry is zero.
- State the invariant: at every iteration, the pair `(a, b)` represents a partial sum and remaining carry; after enough iterations, `b == 0`.
- Mask to 32 bits in languages without unsigned ints; convert back to signed at the end.
- Time O(32), space O(1).

Common Follow-Ups:
- Implement subtraction without `-`.
- Implement multiplication using shifts and adds.
- What if the integer width is unbounded (Python big-integers).

## 2. Bitwise AND of Numbers Range

LeetCode: [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

Difficulty: Medium

Pattern: Common High-Bit Prefix

Why It Matters: Finds unchanged high-bit prefix.

Skills Tested:
- Recognize that AND across a range zeros out any bit that flips somewhere in `[left, right]`; only the common high-bit prefix of `left` and `right` remains.
- State the invariant: shifting both `left` and `right` right by 1 until they are equal counts the bits to drop; the answer is `left << count`.
- Equivalent trick: `right & (right - 1)` clears low bits until `right < left`.
- Time O(log range), space O(1).

Common Follow-Ups:
- AND-bound subarray problems via the same prefix observation.
- Generalize to OR or XOR over a range (different structure).
- What if the range is very large (still log time).

## 3. Single Number II

LeetCode: [Single Number II](https://leetcode.com/problems/single-number-ii/)

Difficulty: Medium

Pattern: Bit Counts Modulo 3

Why It Matters: Extends cancellation to triplicates.

Skills Tested:
- Recognize that for each bit position, the count of 1s mod 3 is the bit of the unique number; this generalizes XOR's mod-2 cancellation.
- State the invariant: 32-bit bucket counts; for each bit, take `count % 3`; assemble the result bit-by-bit.
- Constant-space variant uses two 32-bit registers `ones, twos` updated bitwise.
- Time O(n), space O(1).

Common Follow-Ups:
- Single Number (LC 136) is the mod-2 case.
- Single Number III (LC 260) finds two unique using XOR plus a partition bit.
- What if some elements appear `k` times.

## 4. Bitwise ORs of Subarrays

LeetCode: [Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/)

Difficulty: Medium

Pattern: Rolling OR Frontier Set

Why It Matters: Shows how the set of possible OR values stays bounded by bit width during a scan.

Skills Tested:
- Recognize that ORs ending at index `i` form a set of size at most 32 because each new element can only set new bits (never clear).
- State the invariant: `current = {prev | nums[i] for prev in last_set} | {nums[i]}`; accumulate into a global result set.
- Use Python `set` operations; the running set is bounded by the bit width.
- Time O(n * 32), space O(n * 32).

Common Follow-Ups:
- Maximum AND of Subarrays uses similar bounded-state thinking.
- What if you need bitwise XORs (no monotonicity, set can grow without bound).
- Generalize to subarray bitwise queries with a sparse table.

## 5. Minimum Flips to Make a OR b Equal to c

LeetCode: [Minimum Flips to Make a OR b Equal to c](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

Difficulty: Medium

Pattern: Per-Bit Constraint Counting

Why It Matters: Forces bit-by-bit reasoning about OR constraints instead of treating numbers as opaque integers.

Skills Tested:
- Recognize that each bit is independent: for bit `k`, if `c_k == 0` then both `a_k` and `b_k` must be 0 (count their set bits as flips); if `c_k == 1` then at least one of `a_k` and `b_k` must be 1.
- State the invariant: total flips is the sum over bits of the per-bit flip count.
- Walk all 32 (or 64) bits explicitly using `(x >> k) & 1` extractions.
- Time O(32), space O(1).

Common Follow-Ups:
- Adapt for AND or XOR target equality.
- What if some bits cannot be flipped (constraint mask).
- Generalize to multi-operand bit equations.

## 6. UTF-8 Validation

LeetCode: [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/)

Difficulty: Medium

Pattern: Bit Prefix State Machine

Why It Matters: Parses byte masks carefully.

Skills Tested:
- Recognize that UTF-8 bytes have prefix patterns: `0xxxxxxx` (1 byte), `110xxxxx` (start of 2), `1110xxxx` (start of 3), `11110xxx` (start of 4), `10xxxxxx` (continuation).
- State the invariant: a counter `expected_continuation` tracks how many continuation bytes must follow; each byte is checked against the expected prefix.
- Decrement on a valid continuation, set on a valid leader, fail on a mismatch.
- Time O(n), space O(1).

Common Follow-Ups:
- UTF-16 validation has a different surrogate-pair structure.
- Stream-validate UTF-8 across chunks.
- Generalize to arbitrary prefix-coded byte streams.

## 7. Gray Code

LeetCode: [Gray Code](https://leetcode.com/problems/gray-code/)

Difficulty: Medium

Pattern: Reflected-Binary Code Formula

Why It Matters: Uses reflected binary code structure.

Skills Tested:
- Recognize the formula `gray(i) = i ^ (i >> 1)` produces the i-th Gray code where consecutive codes differ by exactly one bit.
- State the invariant: iterating `i` from 0 to `2^n - 1` and emitting `gray(i)` yields a valid sequence covering every n-bit value once.
- Alternative: build by reflection (append reversed list with the high bit set).
- Time O(2^n), space O(1) extra.

Common Follow-Ups:
- Decode a Gray code back to its index.
- Circular Gray-code sequences over arbitrary alphabets.
- What if you need a Gray-like code with k-bit transitions instead of 1-bit.

## 8. Divide Two Integers

LeetCode: [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

Difficulty: Medium

Pattern: Shift-And-Subtract Long Division

Why It Matters: Performs division under overflow constraints.

Skills Tested:
- Recognize that integer division can be done by repeatedly subtracting the largest power-of-two multiple of the divisor that fits in the remaining dividend.
- State the invariant: after each subtraction, `remainder >= 0` and the quotient is incremented by `2^k` for the chosen `k`.
- Handle the overflow case `dividend == INT_MIN, divisor == -1` (return `INT_MAX`); take signs separately and operate on absolute values.
- Time O(log n), space O(1).

Common Follow-Ups:
- Implement modulo without `%`.
- Big-integer division.
- What if the result must be a fraction (no truncation).

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
