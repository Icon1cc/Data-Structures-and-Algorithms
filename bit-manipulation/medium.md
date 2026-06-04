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

Pattern: Arithmetic Bit Tricks

Why It Matters: Adds without plus using carry logic.

Skills Tested:
- Identify the Arithmetic Bit Tricks signal before choosing a template.
- State the invariant for Sum of Two Integers: adds without plus using carry logic.
- Handle zero, negative numbers, fixed bit width, overflow, and 2^n mask limits.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Sum of Two Integers toward hash maps, arithmetic, dynamic programming, trie, or sorting?
- Which zero case would break the first implementation?
- Can the Arithmetic Bit Tricks invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Bitwise AND of Numbers Range

LeetCode: [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

Difficulty: Medium

Pattern: Common Prefix Bits

Why It Matters: Finds unchanged high-bit prefix.

Skills Tested:
- Identify the Common Prefix Bits signal before choosing a template.
- State the invariant for Bitwise AND of Numbers Range: finds unchanged high-bit prefix.
- Handle zero, negative numbers, fixed bit width, overflow, and 2^n mask limits.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Bitwise AND of Numbers Range toward hash maps, arithmetic, dynamic programming, trie, or sorting?
- Which zero case would break the first implementation?
- Can the Common Prefix Bits invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Single Number II

LeetCode: [Single Number II](https://leetcode.com/problems/single-number-ii/)

Difficulty: Medium

Pattern: Bit Counts Mod 3

Why It Matters: Extends cancellation to triplicates.

Skills Tested:
- Identify the Bit Counts Mod 3 signal before choosing a template.
- State the invariant for Single Number II: extends cancellation to triplicates.
- Handle zero, negative numbers, fixed bit width, overflow, and 2^n mask limits.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Single Number II toward hash maps, arithmetic, dynamic programming, trie, or sorting?
- Which zero case would break the first implementation?
- Can the Bit Counts Mod 3 invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Bitwise ORs of Subarrays

LeetCode: [Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/)

Difficulty: Medium

Pattern: Rolling Bitwise State Set

Why It Matters: Shows how the set of possible OR values stays bounded by bit width during a scan.

Skills Tested:
- Identify the Rolling Bitwise State Set signal before choosing a template.
- State the invariant for Bitwise ORs of Subarrays: shows how the set of possible OR values stays bounded by bit width during a scan.
- Handle zero, negative numbers, fixed bit width, overflow, and 2^n mask limits.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Bitwise ORs of Subarrays toward hash maps, arithmetic, dynamic programming, trie, or sorting?
- Which zero case would break the first implementation?
- Can the Rolling Bitwise State Set invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Minimum Flips to Make a OR b Equal to c

LeetCode: [Minimum Flips to Make a OR b Equal to c](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

Difficulty: Medium

Pattern: Per-Bit Constraint Counting

Why It Matters: Forces bit-by-bit reasoning about OR constraints instead of treating numbers as opaque integers.

Skills Tested:
- Identify the Per-Bit Constraint Counting signal before choosing a template.
- State the invariant for Minimum Flips to Make a OR b Equal to c: forces bit-by-bit reasoning about OR constraints instead of treating numbers as opaque integers.
- Handle zero, negative numbers, fixed bit width, overflow, and 2^n mask limits.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Minimum Flips to Make a OR b Equal to c toward hash maps, arithmetic, dynamic programming, trie, or sorting?
- Which zero case would break the first implementation?
- Can the Per-Bit Constraint Counting invariant survive streaming input, in-place restrictions, or lower memory limits?

## 6. UTF-8 Validation

LeetCode: [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/)

Difficulty: Medium

Pattern: Bit Prefix Checks

Why It Matters: Parses byte masks carefully.

Skills Tested:
- Identify the Bit Prefix Checks signal before choosing a template.
- State the invariant for UTF-8 Validation: parses byte masks carefully.
- Handle zero, negative numbers, fixed bit width, overflow, and 2^n mask limits.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push UTF-8 Validation toward hash maps, arithmetic, dynamic programming, trie, or sorting?
- Which zero case would break the first implementation?
- Can the Bit Prefix Checks invariant survive streaming input, in-place restrictions, or lower memory limits?

## 7. Gray Code

LeetCode: [Gray Code](https://leetcode.com/problems/gray-code/)

Difficulty: Medium

Pattern: Bit Pattern Generation

Why It Matters: Uses reflected binary code structure.

Skills Tested:
- Identify the Bit Pattern Generation signal before choosing a template.
- State the invariant for Gray Code: uses reflected binary code structure.
- Handle zero, negative numbers, fixed bit width, overflow, and 2^n mask limits.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Gray Code toward hash maps, arithmetic, dynamic programming, trie, or sorting?
- Which zero case would break the first implementation?
- Can the Bit Pattern Generation invariant survive streaming input, in-place restrictions, or lower memory limits?

## 8. Divide Two Integers

LeetCode: [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

Difficulty: Medium

Pattern: Shift Subtraction

Why It Matters: Performs division under overflow constraints.

Skills Tested:
- Identify the Shift Subtraction signal before choosing a template.
- State the invariant for Divide Two Integers: performs division under overflow constraints.
- Handle zero, negative numbers, fixed bit width, overflow, and 2^n mask limits.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Divide Two Integers toward hash maps, arithmetic, dynamic programming, trie, or sorting?
- Which zero case would break the first implementation?
- Can the Shift Subtraction invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
