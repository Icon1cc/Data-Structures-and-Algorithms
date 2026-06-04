# Math & Geometry Easy Problems

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

## 1. Palindrome Number

LeetCode: [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

Difficulty: Easy

Pattern: Half-Reverse Numeric

Why It Matters: Tests digit manipulation without string reliance.

Skills Tested:
- Recognize that a number is a palindrome iff its reverse equals itself, but you can stop after reversing only half the digits and compare halves.
- State the invariant: at every step, `reversed = reversed * 10 + x % 10`; stop when `reversed >= x`.
- Handle negative numbers (always non-palindrome) and trailing zeros (only `0` is palindromic).
- Time O(log10 n), space O(1), and contrast with string reversal which uses O(log10 n) memory.

Common Follow-Ups:
- Reverse Integer (LC 7) handles overflow at the boundary.
- What if the base is not 10.
- Generalize to palindromic check on a fixed bit-width integer.

## 2. Roman to Integer

LeetCode: [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

Difficulty: Easy

Pattern: Subtract-When-Smaller-Before-Larger

Why It Matters: Practices rule-based numeric parsing.

Skills Tested:
- Recognize that a Roman digit subtracts when it precedes a strictly larger one (e.g., `IV = 4`); otherwise it adds.
- State the invariant: scan left-to-right, accumulate `+value(c)` if `value(c) >= value(next)`, else `-value(c)`.
- Use a hash map of `{ 'I': 1, 'V': 5, ... }` rather than a switch.
- Time O(n), space O(1).

Common Follow-Ups:
- Integer to Roman (LC 12) is the inverse problem with greedy symbol construction.
- What if invalid Roman strings are possible (validation pass).
- Generalize to other numerical systems with subtractive notation.

## 3. Excel Sheet Column Number

LeetCode: [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

Difficulty: Easy

Pattern: Base-26 Conversion (1-Indexed)

Why It Matters: Converts alphabetic digits to base 26.

Skills Tested:
- Recognize that the alphabet maps `A=1, B=2, ..., Z=26`, so the value of `XYZ` is `26^2 * X + 26 * Y + Z` with each letter 1-indexed.
- State the invariant: at each char, `result = result * 26 + (ord(c) - ord('A') + 1)`.
- Note that this is base-26 with no zero digit, hence the `+ 1` at every position.
- Time O(n), space O(1).

Common Follow-Ups:
- Excel Sheet Column Title (LC 168) is the inverse problem.
- Why does this base have no zero digit (bijective base).
- Generalize to k-letter alphabets.

## 4. Add Digits

LeetCode: [Add Digits](https://leetcode.com/problems/add-digits/)

Difficulty: Easy

Pattern: Digital Root Modulo 9

Why It Matters: Introduces digital-root reasoning.

Skills Tested:
- Recognize that the digital root of `n > 0` is `1 + (n - 1) % 9`, and `0` for `n == 0`.
- State the invariant: digit-summing preserves residue mod 9, so the fixed point is the residue (with the special case for 0).
- Compare the loop-based O(log n) approach to the constant-time formula.
- Time O(1) closed form, space O(1).

Common Follow-Ups:
- What if the base is not 10 (digital root mod `base - 1`).
- Generalize to digital roots of products or factorials.
- Prove the modular property step by step.

## 5. Happy Number

LeetCode: [Happy Number](https://leetcode.com/problems/happy-number/)

Difficulty: Easy

Pattern: Cycle Detection On Digit-Square Map

Why It Matters: Combines arithmetic transform with seen-state detection.

Skills Tested:
- Recognize that the sum-of-squares transform always falls into a cycle (the values are bounded), so cycle detection (hash set or Floyd's tortoise-and-hare) decides happiness.
- State the invariant: a value is happy iff the cycle it enters contains 1; otherwise it cycles among non-1 values.
- Implement Floyd's cycle detection for O(1) extra space.
- Time O(log n) per step bounded by digit count, space O(1) Floyd or O(log n) set.

Common Follow-Ups:
- Linked List Cycle (LC 141) shares the cycle-detection algorithm.
- What if the transform is sum of cubes (different cycle structure).
- Generalize to "is the orbit eventually periodic with period 1".

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
