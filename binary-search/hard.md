# Binary Search Hard Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Hard order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Median of Two Sorted Arrays

LeetCode: [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

Difficulty: Hard

Pattern: Binary Search Partition

Why It Matters: High-value boundary partition problem.

Skills Tested:
- Identify the Binary Search Partition signal before choosing a template.
- State the invariant for Median of Two Sorted Arrays: high-value boundary partition problem.
- Handle single-element ranges, equality handling, duplicate ambiguity, and excluded boundaries.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Median of Two Sorted Arrays toward linear scan, two pointers, heap selection, or direct math?
- Which single-element ranges case would break the first implementation?
- Can the Binary Search Partition invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Split Array Largest Sum

LeetCode: [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)

Difficulty: Hard

Pattern: Binary Search On Answer

Why It Matters: Minimizes the largest partition sum with monotonic feasibility.

Skills Tested:
- Identify the Binary Search On Answer signal before choosing a template.
- State the invariant for Split Array Largest Sum: minimizes the largest partition sum with monotonic feasibility.
- Handle single-element ranges, equality handling, duplicate ambiguity, and excluded boundaries.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Split Array Largest Sum toward linear scan, two pointers, heap selection, or direct math?
- Which single-element ranges case would break the first implementation?
- Can the Binary Search On Answer invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Find Minimum in Rotated Sorted Array II

LeetCode: [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

Difficulty: Hard

Pattern: Rotated Search With Duplicates

Why It Matters: Shows how duplicates weaken logarithmic guarantees.

Skills Tested:
- Identify the Rotated Search With Duplicates signal before choosing a template.
- State the invariant for Find Minimum in Rotated Sorted Array II: shows how duplicates weaken logarithmic guarantees.
- Handle single-element ranges, equality handling, duplicate ambiguity, and excluded boundaries.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Find Minimum in Rotated Sorted Array II toward linear scan, two pointers, heap selection, or direct math?
- Which single-element ranges case would break the first implementation?
- Can the Rotated Search With Duplicates invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Kth Smallest Number in Multiplication Table

LeetCode: [Kth Smallest Number in Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/)

Difficulty: Hard

Pattern: Binary Search Counting

Why It Matters: Searches answer value using a counting predicate.

Skills Tested:
- Identify the Binary Search Counting signal before choosing a template.
- State the invariant for Kth Smallest Number in Multiplication Table: searches answer value using a counting predicate.
- Handle single-element ranges, equality handling, duplicate ambiguity, and excluded boundaries.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Kth Smallest Number in Multiplication Table toward linear scan, two pointers, heap selection, or direct math?
- Which single-element ranges case would break the first implementation?
- Can the Binary Search Counting invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
