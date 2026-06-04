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
- Identify the XOR Cancellation signal before choosing a template.
- State the invariant for Single Number: the baseline XOR cancellation problem.
- Handle zero, negative numbers, fixed bit width, overflow, and 2^n mask limits.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Single Number toward hash maps, arithmetic, dynamic programming, trie, or sorting?
- Which zero case would break the first implementation?
- Can the XOR Cancellation invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Number of 1 Bits

LeetCode: [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

Difficulty: Easy

Pattern: Bit Counting

Why It Matters: Tests low-bit clearing and binary representation.

Skills Tested:
- Identify the Bit Counting signal before choosing a template.
- State the invariant for Number of 1 Bits: tests low-bit clearing and binary representation.
- Handle zero, negative numbers, fixed bit width, overflow, and 2^n mask limits.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Number of 1 Bits toward hash maps, arithmetic, dynamic programming, trie, or sorting?
- Which zero case would break the first implementation?
- Can the Bit Counting invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Counting Bits

LeetCode: [Counting Bits](https://leetcode.com/problems/counting-bits/)

Difficulty: Easy

Pattern: DP Over Bits

Why It Matters: Builds counts using smaller states.

Skills Tested:
- Identify the DP Over Bits signal before choosing a template.
- State the invariant for Counting Bits: builds counts using smaller states.
- Handle zero, negative numbers, fixed bit width, overflow, and 2^n mask limits.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Counting Bits toward hash maps, arithmetic, dynamic programming, trie, or sorting?
- Which zero case would break the first implementation?
- Can the DP Over Bits invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Reverse Bits

LeetCode: [Reverse Bits](https://leetcode.com/problems/reverse-bits/)

Difficulty: Easy

Pattern: Bit Shifts

Why It Matters: Practices fixed-width bit movement.

Skills Tested:
- Identify the Bit Shifts signal before choosing a template.
- State the invariant for Reverse Bits: practices fixed-width bit movement.
- Handle zero, negative numbers, fixed bit width, overflow, and 2^n mask limits.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Reverse Bits toward hash maps, arithmetic, dynamic programming, trie, or sorting?
- Which zero case would break the first implementation?
- Can the Bit Shifts invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Missing Number

LeetCode: [Missing Number](https://leetcode.com/problems/missing-number/)

Difficulty: Easy

Pattern: XOR Or Sum

Why It Matters: Uses cancellation over a known range.

Skills Tested:
- Identify the XOR Or Sum signal before choosing a template.
- State the invariant for Missing Number: uses cancellation over a known range.
- Handle zero, negative numbers, fixed bit width, overflow, and 2^n mask limits.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Missing Number toward hash maps, arithmetic, dynamic programming, trie, or sorting?
- Which zero case would break the first implementation?
- Can the XOR Or Sum invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
